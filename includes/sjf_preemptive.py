import heapq
from utils.visualizer import print_table_sjf, print_execution_order

def sjf_preemptive(processes):
    # Manter uma cópia dos processos originais para exibição dos resultados
    processos_originais = processes.copy()

    # Ordenar os processos pelo tempo de chegada
    processes.sort(key=lambda x: x["arrival_time"])

    # Incializando as variaveis
    ordem_execucao = []
    tempo_atual = 0 
    tempo_espera_total = 0 
    tabela_dados = [] 
    min_heap = [] 
    process_index = 0
    n = len(processes)
    burst_remaining = {process['pid']: process['burst_times'][0] for process in processes} 
    start_times = {} 
    end_times = {}
    wait_times = {process['pid']: 0 for process in processes} 
    completed = 0 

    while completed < n:
        while process_index < n and processes[process_index]['arrival_time'] <= tempo_atual: # Adiciona processos que chegaram até o tempo atual na heap
            heapq.heappush(min_heap, (burst_remaining[processes[process_index]['pid']], processes[process_index]['pid']))
            process_index += 1

        if min_heap:
            _,current_pid = heapq.heappop(min_heap) # Obtém o processo com o menor tempo de rajada restante
            if current_pid not in start_times: # Primeira vez que o processo roda
                start_times[current_pid] = tempo_atual # Registra o tempo de início do processo
                
            ordem_execucao.append(current_pid)
            
            tempo_atual += 1 # Incrementa o tempo atual (simula a execução do processo por uma unidade de tempo)
            burst_remaining[current_pid] -= 1 # Decrementa o tempo de rajada restante do processo

            if burst_remaining[current_pid] == 0: # Processo completado
                completed += 1 # Incrementa o contador de processos completados
                end_times[current_pid] = tempo_atual # Registra o tempo de término do processo
                processo_atual = next(p for p in processes if p['pid'] == current_pid) # Obtém o processo atual da lista original
                wait_times[current_pid] = end_times[current_pid] - processo_atual['arrival_time'] - processo_atual['burst_times'][0] # Calcula o tempo de espera do processo
                tempo_espera_total += wait_times[current_pid] # Acumula o tempo de espera no total
            else:
                heapq.heappush(min_heap, (burst_remaining[current_pid], current_pid)) # Se o processo não for completado, o re-adiciona na heap com o novo tempo de rajada restante
        else:
            tempo_atual += 1 # Se não houver processos na heap, incrementa o tempo atual para esperar pela chegada de novos processos

    # Exibir resultados
    for p in processos_originais:
        tabela_dados.append({
            'pid': p['pid'],
            'tempo_inicio': start_times.get(p['pid'], 'N/A'),
            'tempo_termino': end_times.get(p['pid'], 'N/A'),
            'tempo_espera': wait_times.get(p['pid'], 'N/A')
        })


    if processos_originais:  # Evitar ZeroDivisionError
        tempo_espera_medio = tempo_espera_total / len(processos_originais)
    else:
        print("Não há processos para calcular o tempo de espera médio.")
    
    print('\n')
    print_table_sjf(tabela_dados, tempo_espera_medio)
    print_execution_order(ordem_execucao)