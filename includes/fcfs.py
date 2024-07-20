from utils.visualizer import print_table_fcfs

def fcfs(processes):
    avg_wt_add = 0
    tabela_dados = []

    
    for index, process in enumerate(processes):
        if index == 0:  # Se for o primeiro processo
            wait_time = 0
        else:
            avg_wt_add += wait_time  # Acumula o total do tempo de espera dos processos  
                   
        burst_time = sum(process['burst_times'])  # `burst_time` soma o tempo de rajada do processo
        tabela_dados.append({
            'pid': process['pid'],
            'tempo_espera': wait_time,
            'burst_time': burst_time
        })
        wait_time += burst_time  # `wait_time` acumula o valor de `burst_time` e soma com valor total
    
    avg_wait_time = avg_wt_add / (len(processes) - 1)  # Cálculo do tempo de espera médio, excluindo o primeiro processo
    print('\n')
    print_table_fcfs(tabela_dados, avg_wait_time)
