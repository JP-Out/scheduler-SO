from termcolor import colored

def print_table_fcfs(dados, avg):
    average = f"Tempo Médio: {avg:.2f} u.t"
    half_length_string = ((43 - len(average))//2)
    
    print(colored("╒" + "═" * 7 + "╤" + "═" * 17 + "╤" + "═" * 15 + "╕", 'blue'))
    print(colored("│", 'blue') + colored(f" {'PID':<5} ", 'yellow') + colored("│", 'blue') + colored(f" {'Tempo de Espera':<15} ", 'yellow') + colored("│", 'blue') + colored(f" {'Burst Time':<13} ", 'yellow') + colored("│", 'blue'))
    print(colored("╞" + "═" * 7 + "╪" + "═" * 17 + "╪" + "═" * 15 + "╡", 'blue'))
    
    for item in dados:
        print(colored("│", 'blue') + colored(f" {item['pid']:<5} ", 'green') + colored("│", 'blue') + colored(f" {item['tempo_espera']:<15} ", 'green') + colored("│", 'blue') + colored(f" {item['burst_time']:<13} ", 'green') + colored("│", 'blue'))
    
    print(colored("╘" + "═" * 7 + "╧" + "═" * 17 + "╧" + "═" * 15 + "╛", 'blue'))
    print(colored(" " * half_length_string + f"{average}", 'magenta'))

def print_table_sjf(dados, avg):
    average = f"Tempo Médio: {avg:.2f} u.t"
    half_length_string = ((64 - len(average))//2)
    
    print(colored("╒" + "═" * 7 + "╤" + "═" * 17 + "╤" + "═" * 18 + "╤" + "═" * 17 + "╕", 'blue'))
    print(colored("│", 'blue') + colored(f" {'PID':<5} ", 'yellow') + colored("│", 'blue') + colored(f" {'Tempo de Início':<15} ", 'yellow') + colored("│", 'blue') + colored(f" {'Tempo de Término':<15} ", 'yellow') + colored("│", 'blue') + colored(f" {'Tempo de Espera':<15} ", 'yellow') + colored("│", 'blue'))
    print(colored("╞" + "═" * 7 + "╪" + "═" * 17 + "╪" + "═" * 18 + "╪" + "═" * 17 + "╡", 'blue'))
    
    for item in dados:
        print(colored("│", 'blue') + colored(f" {item['pid']:<3}   ", 'green') + colored("│", 'blue') + colored(f" {item.get('tempo_inicio', 'N/A'):<15} ", 'green') + colored("│", 'blue') + colored(f" {item.get('tempo_termino', 'N/A'):<15}  ", 'green') + colored("│", 'blue') + colored(f" {item.get('tempo_espera', 'N/A'):<15} ", 'green') + colored("│", 'blue'))
    
    print(colored("╘" + "═" * 7 + "╧" + "═" * 17 + "╧" + "═" * 18 + "╧" + "═" * 17 + "╛", 'blue'))
    print(colored(" " * half_length_string + f"{average}", 'magenta'))

def print_table_round_robin(dados, avg):
    average = f"Tempo Médio: {avg:.2f} u.t"
    half_length_string = ((64 - len(average))//2)
    
    print(colored("╒" + "═" * 7 + "╤" + "═" * 17 + "╤" + "═" * 18 + "╤" + "═" * 17 + "╕", 'blue'))
    print(colored("│", 'blue') + colored(f" {'PID':<5} ", 'yellow') + colored("│", 'blue') + colored(f" {'Tempo de Início':<15} ", 'yellow') + colored("│", 'blue') + colored(f" {'Tempo de Término':<15} ", 'yellow') + colored("│", 'blue') + colored(f" {'Tempo de Espera':<15} ", 'yellow') + colored("│", 'blue'))
    print(colored("╞" + "═" * 7 + "╪" + "═" * 17 + "╪" + "═" * 18 + "╪" + "═" * 17 + "╡", 'blue'))
    
    for item in dados:
        print(colored("│", 'blue') + colored(f" {item['pid']:<3}   ", 'green') + colored("│", 'blue') + colored(f" {item.get('tempo_inicio', 'N/A'):<15} ", 'green') + colored("│", 'blue') + colored(f" {item.get('tempo_termino', 'N/A'):<15}  ", 'green') + colored("│", 'blue') + colored(f" {item.get('tempo_espera', 'N/A'):<15} ", 'green') + colored("│", 'blue'))
    
    print(colored("╘" + "═" * 7 + "╧" + "═" * 17 + "╧" + "═" * 18 + "╧" + "═" * 17 + "╛", 'blue'))
    print(colored(" " * half_length_string + f"{average}", 'magenta'))

def print_execution_order(order):
    # Calcular o comprimento máximo da linha
    formatted_order = ' ➔  '.join(order)
    max_length = len(formatted_order) + 2  # 1 espaços de cada lado

    # Criação da borda superior
    border = colored('┌' + '─' * max_length + '┐', 'blue')

    # Criação da borda inferior
    bottom_border = colored('└' + '─' * max_length + '┘', 'blue')

    # Impressão do cabeçalho
    print(colored("\n  Ordem de Execução dos Processos:", 'yellow'))
    print(border)

    # Impressão da ordem com margens
    print(colored('│', 'blue') + colored(' ' + formatted_order + ' ', 'green') + colored('│', 'blue'))

    # Impressão da borda inferior
    print(bottom_border)
    print()
