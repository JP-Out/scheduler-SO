from includes.fcfs import fcfs
from includes.sjf_non_preemptive import sjf_non_preemptive
from includes.sjf_preemptive import sjf_preemptive
from includes.round_robin import round_robin

STATS = ('criado', 'pronto', 'executando', 'bloqueado', 'encerrado')

def create_process(algorithm):
    burst_times_all = []  # Array com todos os tempos de rajada
    arrival_times_all = []  # Array com todos os tempos de chegada
    
    pids = list(map(str, input("\nInforme os PIDs:\neg.: 000 111 222\n").split()))  # Adiciona todos os valores no array `pids[]`

    for pid in pids:
        if algorithm == 'sjf' or algorithm == 'sjf-preemptive':
            arrival_input = input(f"\nTempo de CHEGADA para processo {pid}: ")
            arrival_times_all.append(int(arrival_input))  # Adicionando todos os valores no array `arrival_times_all[]`
        else:
            arrival_times_all.append(0)  # Definindo tempo de chegada padrão o como 0 para FCFS
        
        burst_input = input(f"Tempo de RAJADA para processo {pid}: ")
        burst_times_all.append(list(map(int, burst_input.split())))  # Adicionando todos os valores no array `burst_times_all[]`
        
    processes = [{'pid': pid, 'burst_times': burst_times, 'arrival_time': arrival_time, 'stats': STATS[0]} 
                 for pid, burst_times, arrival_time in zip(pids, burst_times_all, arrival_times_all)]  # Adicionando em um dicionário de processos

    return processes

def switch_case_option(op):
    if op == '1':
        return 'fcfs'
    elif op == '2':
        return 'sjf'
    elif op == '3':
        return 'sjf-preemptive'
    elif op == '4':
        return 'round_robin'
    else:
        raise ValueError("Opção inválida! Escolha 1 ou 2.")

def main():
    print('Escolha um método de escalonamento: ')
    print('1 - FCFS')    
    print('2 - SJF Não-preemptivo')
    print('3 - SJF Preemptivo')
    print('4 - Round Robin')
    option = input('>>> ')
    
    algorithm = switch_case_option(option)
    
    processes = create_process(algorithm)
    
    if algorithm == 'fcfs':
        fcfs(processes)
    elif algorithm == 'sjf':
        sjf_non_preemptive(processes)
    elif algorithm == 'sjf-preemptive':
        sjf_preemptive(processes)
    elif algorithm == 'round_robin':
        quantum = int(input("Informe o quantum de tempo para o Round Robin: "))
        round_robin(processes, quantum)

if __name__ == "__main__":
    main()