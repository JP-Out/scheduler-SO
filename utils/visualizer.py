from termcolor import colored
FCFS_MAX_WIDTH = 68
SJF_MAX_WIDTH = 64
RR_MAX_WIDTH = 64

def format_column(value, width):
    """Formata o valor com a largura especificada."""
    str_value = str(value)
    if len(str_value) > width:
        return f" {str_value[:width - 3]}... "
    return f" {str(value):<{width}} "

def print_table_fcfs(dados, avg, total_exec_time):
    average_str = f"Tempo Médio: {avg:.2f} u.t"  # Armazena o tempo médio em uma string
    total_time_str = f"Tempo Total de Execução: {total_exec_time:.2f} u.t"

    # Calcula os espaços de preenchimento à esquerda e à direita
    avg_padding = (FCFS_MAX_WIDTH - len(average_str)) // 2
    total_time_padding = (FCFS_MAX_WIDTH - len(total_time_str)) // 2

    # Certifica-se de que os preenchimentos não sejam negativos
    avg_padding_left = max(avg_padding, 0)
    avg_padding_right = FCFS_MAX_WIDTH - len(average_str) - avg_padding_left
    total_time_padding_left = max(total_time_padding, 0)
    total_time_padding_right = FCFS_MAX_WIDTH - len(total_time_str) - total_time_padding_left

    # Definindo os comprimentos das colunas
    col_widths = {
        'PID': 6,
        'Wait Time': 10,
        'Burst Time': 11,
        'Turnaround Time': 15,
        'Finish Time': 12
    }
    
    # Impressão do cabeçalho da tabela
    print(colored("╒" + "═" * 8 + "╤" + "═" * 12 + "╤" + "═" * 13 + "╤" + "═" * 17 + "╤" + "═" * 14 + "╕", 'blue'))
    print(colored("│", 'blue') + colored(format_column('PID', col_widths['PID']), 'yellow') + colored("│", 'blue') +
          colored(format_column('Wait Time', col_widths['Wait Time']), 'yellow') + colored("│", 'blue') +
          colored(format_column('Burst Time', col_widths['Burst Time']), 'yellow') + colored("│", 'blue') +
          colored(format_column('Turnaround Time', col_widths['Turnaround Time']), 'yellow') + colored("│", 'blue') +
          colored(format_column('Finish Time', col_widths['Finish Time']), 'yellow') + colored("│", 'blue'))
    print(colored("╞" + "═" * 8 + "╪" + "═" * 12 + "╪" + "═" * 13 + "╪" + "═" * 17 + "╪" + "═" * 14 + "╡", 'blue'))
    
    # Impressão dos resultados na tabela
    for item in dados:
        item['tempo_execucao'] = 'Null'
        print(colored("│", 'blue') + colored(format_column(item['pid'], col_widths['PID']), 'green') +
              colored("│", 'blue') + colored(format_column(item['tempo_espera'], col_widths['Wait Time']), 'green') +
              colored("│", 'blue') + colored(format_column(item['burst_time'], col_widths['Burst Time']), 'green') +
              colored("│", 'blue') + colored(format_column(item['turnaround_time'], col_widths['Turnaround Time']), 'green') +
              colored("│", 'blue') + colored(format_column(item['finish_time'], col_widths['Finish Time']), 'green') +
              colored("│", 'blue'))   
    
    # Impressão do Tempo Total de Execução
    print(colored("╞" + "═" * 8 + "╧" + "═" * 12 + "╧" + "═" * 13 + "╧" + "═" * 17 + "╧" + "═" * 14 + "╡", 'blue'))
    print(colored(colored("│", 'blue') + colored(" " * total_time_padding_left + f"{total_time_str}" + " " * total_time_padding_right, 'cyan') + colored("│", 'blue'), 'cyan'))
    print(colored("╞" + "═" * (FCFS_MAX_WIDTH) + "╡", 'blue'))

    # Impressão do Tempo Médio
    print(colored("│", 'blue') + colored(" " * avg_padding_left + f"{average_str}" + " " * avg_padding_right, 'cyan') + colored("│", 'blue'))
    print(colored("╘" + "═" * (FCFS_MAX_WIDTH) + "╛", 'blue'))

def print_table_sjf(dados, avg):
    average = f"Tempo Médio: {avg:.2f} u.t"
    half_length_string = ((SJF_MAX_WIDTH - len(average))//2)
    
    print(colored("╒" + "═" * 7 + "╤" + "═" * 17 + "╤" + "═" * 18 + "╤" + "═" * 17 + "╕", 'blue'))
    print(colored("│", 'blue') + colored(f" {'PID':<5} ", 'yellow') + colored("│", 'blue') + colored(f" {'Tempo de Início':<15} ", 'yellow') + colored("│", 'blue') + colored(f" {'Tempo de Término':<15} ", 'yellow') + colored("│", 'blue') + colored(f" {'Tempo de Espera':<15} ", 'yellow') + colored("│", 'blue'))
    print(colored("╞" + "═" * 7 + "╪" + "═" * 17 + "╪" + "═" * 18 + "╪" + "═" * 17 + "╡", 'blue'))
    
    for item in dados:
        print(colored("│", 'blue') + colored(f" {item['pid']:<3}   ", 'green') + colored("│", 'blue') + colored(f" {item.get('tempo_inicio', 'N/A'):<15} ", 'green') + colored("│", 'blue') + colored(f" {item.get('tempo_termino', 'N/A'):<15}  ", 'green') + colored("│", 'blue') + colored(f" {item.get('tempo_espera', 'N/A'):<15} ", 'green') + colored("│", 'blue'))
    
    print(colored("╘" + "═" * 7 + "╧" + "═" * 17 + "╧" + "═" * 18 + "╧" + "═" * 17 + "╛", 'blue'))
    print(colored(" " * half_length_string + f"{average}", 'magenta'))

def print_table_round_robin(dados, avg):
    average = f"Tempo Médio: {avg:.2f} u.t"
    half_length_string = ((RR_MAX_WIDTH - len(average))//2)
    
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
