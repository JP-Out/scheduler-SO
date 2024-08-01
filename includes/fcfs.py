from utils.visualizer import print_table_fcfs, print_execution_order

def fcfs(processes, context_switch_time):
    avg_wt_add = 0
    tabela_dados = []
    ordem_execucao = []
    current_time = 0
    start_time = 0

    for index, process in enumerate(processes):
        if index == 0:  # Se for o primeiro processo
            wait_time = 0
            start_time = process['arrival_time']  
        else:
            wait_time = current_time - process['arrival_time']
            wait_time = max(wait_time, 0)  # Garantir que o tempo de espera não seja negativo
        
        avg_wt_add += wait_time
        
        burst_time = sum(process['burst_times'])
        finish_time = current_time + burst_time
        turnaround_time = finish_time - process['arrival_time']
        
        tabela_dados.append({
            'pid': process['pid'],
            'tempo_espera': wait_time,
            'burst_time': burst_time,
            'turnaround_time': turnaround_time,
            'finish_time': finish_time
        })
        
        ordem_execucao.append(process['pid'])
        current_time = finish_time + context_switch_time  # Atualiza o tempo atual incluindo o tempo de troca de contexto
        
    avg_wait_time = avg_wt_add / len(processes)  # Cálculo do tempo de espera médio
    total_execution_time = finish_time - start_time  # Cálculo do tempo total de execução
    
    print_table_fcfs(tabela_dados, avg_wait_time, total_execution_time)
    print_execution_order(ordem_execucao)
