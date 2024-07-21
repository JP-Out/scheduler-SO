from collections import deque
from utils.visualizer import print_table_round_robin, print_execution_order

def round_robin(processes, quantum):
    # Manter uma cópia dos processos originais para exibição dos resultados
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

    while fila or process_index < n:
        if fila:
            current_process = fila.popleft()  # Obtém o próximo processo da fila
            current_pid = current_process['pid']
            
            # Adiciona o PID à ordem de execução
            ordem_execucao.append(current_pid)
            
            # Se o processo está começando pela primeira vez
            if current_pid not in start_times:
                start_times[current_pid] = tempo_atual  # Registra o tempo de início do processo
            
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
        tabela_dados.append({
            'pid': p['pid'],
            'tempo_inicio': start_times.get(p['pid'], 'N/A'),
            'tempo_termino': end_times.get(p['pid'], 'N/A'),
            'tempo_espera': wait_times.get(p['pid'], 'N/A')
        })

    # Calcular tempo de espera médio
    if processos_originais:  # Verifica se há processos para evitar ZeroDivisionError
        tempo_espera_medio = sum(wait_times.values()) / len(processos_originais)
    else:
        print("Não há processos para calcular o tempo de espera médio.")
    print('\n')
    print_table_round_robin(tabela_dados, tempo_espera_medio)
    
    print_execution_order(ordem_execucao)
