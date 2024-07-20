# STATS = ('criado', 'pronto', 'executando', 'bloqueado', 'encerrado')

def fcfs(processes):
    avg_wt_add = 0

    print("╒" + "═" * 7 + "╤" + "═" * 17 + "╤" + "═" * 15 + "╕")
    print(f"│ {'PID':<5} │ {'Tempo de Espera':<15} │ {'Burst Time':<13} │") # Cabeçalho da Tabela
    print("╞" + "═" * 7 + "╪" + "═" * 17 + "╪" + "═" * 15 + "╡")
    
    for index, process in enumerate(processes):
        if index == 0:  # Se for o primeiro processo
            wait_time = 0
        else:
            avg_wt_add += wait_time  # Acumula o total do tempo de espera dos processos  
                   
        burst_time = sum(process['burst_times'])  # `burst_time` soma o tempo de rajada do processo
        print(f"│ {process['pid']:<5} │ {wait_time:<15} │ {burst_time:<13} │")
        wait_time += burst_time  # `wait_time` acumula o valor de `burst_time` e soma com valor total
    
    print("╘" + "═" * 7 + "╧" + "═" * 17 + "╧" + "═" * 15 + "╛")
    avg_wait_time = avg_wt_add / (len(processes) - 1)  # Cálculo do tempo de espera médio, excluindo o primeiro processo
    print(f'\nTempo de espera médio: {avg_wait_time:.2f}')
