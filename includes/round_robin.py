from collections import deque
from utils.visualizer import print_table_rr, print_execution_order

def round_robin(processes, quantum, context_switch_time):
    # Cópia para exibição dos resultados
    processos_originais = processes.copy()
    
    # Inicializando variáveis
    tempo_atual = 0
    tempo_espera_total = 0
    tabela_dados = []
    ordem_execucao = []
    fila = deque()
    process_index = 0
    n = len(processes)
    
    start_times = {}
    end_times = {}
    wait_times = {process['pid']: 0 for process in processes}
    burst_remaining = {process['pid']: process['burst_times'][0] for process in processes}
    
    # Adicionar os processos na fila quando eles chegam
    while process_index < n and processes[process_index]['arrival_time'] <= tempo_atual:
        fila.append(processes[process_index])
        process_index += 1

    last_pid = None  # Para acompanhar o último processo executado

    while fila or process_index < n:
        if fila:
            current_process = fila.popleft()  # Obtém o próximo processo da fila
            current_pid = current_process['pid']
            
            # Adiciona o PID à ordem de execução
            ordem_execucao.append(current_pid)
            
            # Se o processo está começando pela primeira vez
            if current_pid not in start_times:
                start_times[current_pid] = tempo_atual  # Registra o tempo de início do processo
            
            # Se houve troca de processo, adiciona o tempo de troca de contexto
            if last_pid is not None and last_pid != current_pid:
                tempo_atual += context_switch_time

            last_pid = current_pid  # Atualiza o último processo executado
            
            # Executa o processo pelo tempo do quantum ou até ser completado
            execute_time = min(quantum, burst_remaining[current_pid])
            burst_remaining[current_pid] -= execute_time
            tempo_atual += execute_time
            
            # Se o processo foi completado
            if burst_remaining[current_pid] == 0:
                end_times[current_pid] = tempo_atual
                wait_times[current_pid] = end_times[current_pid] - current_process['arrival_time'] - current_process['burst_times'][0]
                tempo_espera_total += wait_times[current_pid]
            else:
                # Adiciona processos que chegaram enquanto o atual estava executando
                while process_index < n and processes[process_index]['arrival_time'] <= tempo_atual:
                    fila.append(processes[process_index])
                    process_index += 1
                fila.append(current_process)  # Re-adiciona o processo atual no final da fila
        else:
            # Se a fila estiver vazia, incrementa o tempo atual para esperar pela chegada de novos processos
            tempo_atual += 1
            # Adiciona processos que chegaram até o tempo atual na fila
            while process_index < n and processes[process_index]['arrival_time'] <= tempo_atual:
                fila.append(processes[process_index])
                process_index += 1
    
    # Exibir resultados
    for p in processos_originais:
        pid = p['pid']
        burst_time = p['burst_times'][0]
        turnaround_time = end_times.get(pid, 'N/A') - p['arrival_time']
        tabela_dados.append({
            'pid': pid,
            'burst_time': burst_time,
            'wait_time': wait_times.get(pid, 'N/A'),
            'turnaround_time': turnaround_time,
            'finish_time': end_times.get(pid, 'N/A')
        })

    # Calcular tempo de espera médio
    if processos_originais:  # Verifica se há processos para evitar ZeroDivisionError
        tempo_espera_medio = sum(wait_times.values()) / len(processos_originais)
    else:
        tempo_espera_medio = 0

    # Tempo total de execução
    tempo_total_execucao = max(end_times.values(), default=0)
    
    # Chama a função para imprimir a tabela com o tempo total de execução
    print()
    print_table_rr(tabela_dados, tempo_espera_medio, tempo_total_execucao)
    print_execution_order(ordem_execucao)