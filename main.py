from includes.fcfs import fcfs
from includes.sjf_non_preemptive import sjf_non_preemptive
from includes.sjf_preemptive import sjf_preemptive
from includes.round_robin import round_robin
from termcolor import colored

def create_process(algorithm):
    """
    Função para criar processos com base no algoritmo selecionado.
    
    Parâmetros:
    algorithm (str): O algoritmo de escalonamento selecionado ('fcfs', 'sjf', 'sjf-preemptive', 'round_robin').

    Retorna:
    list: Uma lista de dicionários contendo informações dos processos.
    """
    burst_times_all = []  # Lista com todos os tempos de rajada
    arrival_times_all = []  # Lista com todos os tempos de chegada
    printed_once = False  # Variável para garantir quebra de linha uma única vez
    
    pids = list(map(str, input(colored("\nInforme os PIDs:\neg.: 000 111 222\n", 'cyan')).split()))  # Adiciona todos os PIDs na lista `pids`
    
    for pid in pids:
        if algorithm in ['sjf', 'sjf-preemptive']:
            print()
            arrival_input = input(colored("Tempo de ", 'yellow') + colored("CHEGADA", 'magenta') + colored(" para processo ", 'yellow') + colored(f"{pid}: ", 'green'))
            arrival_times_all.append(int(arrival_input))  # Adiciona todos os tempos de chegada na lista `arrival_times_all`
        else:
            arrival_times_all.append(0)  # Define tempo de chegada padrão como 0 para FCFS
        
        if algorithm in ['fcfs', 'round_robin'] and not printed_once:
            print()
            printed_once = True
        
        burst_input = input(colored("Tempo de ", 'yellow') + colored("RAJADA", 'magenta') + colored(" para processo ", 'yellow') + colored(f"{pid}: ", 'green'))
        burst_times_all.append(list(map(int, burst_input.split())))  # Adiciona todos os tempos de rajada na lista `burst_times_all`
    
    # Cria uma lista de dicionários com informações dos processos
    processes = [{'pid': pid, 'burst_times': burst_times, 'arrival_time': arrival_time} 
                 for pid, burst_times, arrival_time in zip(pids, burst_times_all, arrival_times_all)]

    return processes

def switch_case_option(op):
    """
    Função para selecionar o algoritmo de escalonamento com base na opção do usuário.

    Parâmetros:
    op (str): A opção selecionada pelo usuário.

    Retorna:
    str: O algoritmo de escalonamento correspondente.
    """
    options = {
        '1': 'fcfs',
        '2': 'sjf',
        '3': 'sjf-preemptive',
        '4': 'round_robin'
    }
    
    if op in options:
        return options[op]
    else:
        raise ValueError(colored("Opção inválida! Escolha 1, 2, 3 ou 4.", 'red'))

def main():
    """
    Função principal que gerencia a interação com o usuário e executa o algoritmo de escalonamento selecionado.
    """
    print(colored('\nEscolha um método de escalonamento:', 'cyan'))
    print(colored('1 - FCFS', 'blue'))
    print(colored('2 - SJF Não-preemptivo', 'blue'))
    print(colored('3 - SJF Preemptivo', 'blue'))
    print(colored('4 - Round Robin', 'blue'))
    
    option = input(colored('>>> ', 'magenta'))
    algorithm = switch_case_option(option)
    processes = create_process(algorithm)
    
    if algorithm == 'fcfs':
        context_switch_time = int(input(colored("\nInforme o ", 'yellow') + colored("TEMPO DE TROCA DE CONTEXTO", 'blue') + colored(": ", 'yellow'))); print()
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
