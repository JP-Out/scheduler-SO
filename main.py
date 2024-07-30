from includes.fcfs import fcfs
from includes.sjf_non_preemptive import sjf_non_preemptive
from includes.sjf_preemptive import sjf_preemptive
from includes.round_robin import round_robin
from termcolor import colored

def create_process(algorithm):
    burst_times_all = []  # Array com todos os tempos de rajada
    arrival_times_all = []  # Array com todos os tempos de chegada
    
    pids = list(map(str, input(colored("\nInforme os PIDs:\neg.: 000 111 222\n", 'cyan')).split()))  # Adiciona todos os valores no array `pids[]`

    for pid in pids:
        if algorithm == 'sjf' or algorithm == 'sjf-preemptive':
            arrival_input = input(colored("\nTempo de ", 'yellow') + colored("CHEGADA", 'magenta') + colored(" para processo ", 'yellow') + colored(f"{pid}: ", 'green'))
            arrival_times_all.append(int(arrival_input))  # Adicionando todos os valores no array `arrival_times_all[]`
        else:
            arrival_times_all.append(0)  # Definindo tempo de chegada padrão o como 0 para FCFS
        
        burst_input = input(colored("Tempo de ", 'yellow') + colored("RAJADA", 'magenta') + colored(" para processo ", 'yellow') + colored(f"{pid}: ", 'green'))
        burst_times_all.append(list(map(int, burst_input.split())))  # Adicionando todos os valores no array `burst_times_all[]`
        
    processes = [{'pid': pid, 'burst_times': burst_times, 'arrival_time': arrival_time} 
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
        raise ValueError(colored("Opção inválida! Escolha 1, 2, 3 ou 4.", 'red'))

def main():
    print(colored('\nEscolha um método de escalonamento:', 'cyan'))
    print(colored('1 - FCFS', 'blue'))
    print(colored('2 - SJF Não-preemptivo', 'blue'))
    print(colored('3 - SJF Preemptivo', 'blue'))
    print(colored('4 - Round Robin', 'blue'))
    
    option = input(colored('>>> ', 'magenta'))
    
    algorithm = switch_case_option(option)
    
    processes = create_process(algorithm)
    
    if algorithm == 'fcfs':
        context_switch_time = int(input(colored("\nInforme o ", 'yellow') + colored("TEMPO DE TROCA DE CONTEXTO", 'blue') + colored(": ", 'yellow')))
        fcfs(processes, context_switch_time)
    elif algorithm == 'sjf':
        sjf_non_preemptive(processes)
    elif algorithm == 'sjf-preemptive':
        sjf_preemptive(processes)
    elif algorithm == 'round_robin':
        quantum = int(input(colored("\nInforme o ", 'yellow') + colored("QUANTUM", 'blue') + colored(" do ", 'yellow') + colored("Round-Robin", 'blue') + colored(": ", 'yellow')))
        round_robin(processes, quantum)

if __name__ == "__main__":
    main()
