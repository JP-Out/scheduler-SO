from termcolor import colored

FCFS_MAX_WIDTH = 68
SJF_MAX_WIDTH = 84
RR_MAX_WIDTH = 68

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
        'Burst Time': 11,
        'Wait Time': 10,
        'Turnaround Time': 15,
        'Finish Time': 12
    }
    
    # Impressão do cabeçalho da tabela
    print(colored("╒" + "═" * 8 + "╤" + "═" * 13 + "╤" + "═" * 12 + "╤" + "═" * 17 + "╤" + "═" * 14 + "╕", 'blue'))
    print(colored("│", 'blue') + colored(format_column('PID', col_widths['PID']), 'yellow') + colored("│", 'blue') +
          colored(format_column('Burst Time', col_widths['Burst Time']), 'yellow') + colored("│", 'blue') +
          colored(format_column('Wait Time', col_widths['Wait Time']), 'yellow') + colored("│", 'blue') +
          colored(format_column('Turnaround Time', col_widths['Turnaround Time']), 'yellow') + colored("│", 'blue') +
          colored(format_column('Finish Time', col_widths['Finish Time']), 'yellow') + colored("│", 'blue'))
    print(colored("╞" + "═" * 8 + "╪" + "═" * 13 + "╪" + "═" * 12 + "╪" + "═" * 17 + "╪" + "═" * 14 + "╡", 'blue'))
    
    # Impressão dos resultados na tabela
    for item in dados:
        item['tempo_execucao'] = 'Null'
        print(colored("│", 'blue') + colored(format_column(item['pid'], col_widths['PID']), 'green') +
              colored("│", 'blue') + colored(format_column(item['wait_time'], col_widths['Wait Time']), 'green') +
              colored("│", 'blue') + colored(format_column(item['burst_time'], col_widths['Burst Time']), 'green') +
              colored("│", 'blue') + colored(format_column(item['turnaround_time'], col_widths['Turnaround Time']), 'green') +
              colored("│", 'blue') + colored(format_column(item['finish_time'], col_widths['Finish Time']), 'green') +
              colored("│", 'blue'))   
    
    # Impressão do Tempo Total de Execução
    print(colored("╞" + "═" * 8 + "╧" + "═" * 13 + "╧" + "═" * 12 + "╧" + "═" * 17 + "╧" + "═" * 14 + "╡", 'blue'))
    print(colored(colored("│", 'blue') + colored(" " * total_time_padding_left + f"{total_time_str}" + " " * total_time_padding_right, 'cyan') + colored("│", 'blue'), 'cyan'))
    print(colored("╞" + "═" * FCFS_MAX_WIDTH + "╡", 'blue'))

    # Impressão do Tempo Médio
    print(colored("│", 'blue') + colored(" " * avg_padding_left + f"{average_str}" + " " * avg_padding_right, 'cyan') + colored("│", 'blue'))
    print(colored("╘" + "═" * FCFS_MAX_WIDTH + "╛", 'blue'))

def print_table_sjf(dados, avg, total_exec_time):
    average_str = f"Tempo Médio: {avg:.2f} u.t"  # Armazena o tempo médio em uma string
    total_time_str = f"Tempo Total de Execução: {total_exec_time:.2f} u.t"

    # Calcula os espaços de preenchimento à esquerda e à direita
    avg_padding = (SJF_MAX_WIDTH - len(average_str)) // 2
    total_time_padding = (SJF_MAX_WIDTH - len(total_time_str)) // 2

    # Certifica-se de que os preenchimentos não sejam negativos
    avg_padding_left = max(avg_padding, 0)
    avg_padding_right = SJF_MAX_WIDTH - len(average_str) - avg_padding_left
    total_time_padding_left = max(total_time_padding, 0)
    total_time_padding_right = SJF_MAX_WIDTH - len(total_time_str) - total_time_padding_left

    # Definindo os comprimentos das colunas
    col_widths = {
        'PID': 6,
        'Arrival Time': 13,
        'Burst Time': 11,
        'Wait Time': 10,
        'Turnaround Time': 15,
        'Finish Time': 12
    }
    
    # Impressão do cabeçalho da tabela
    print(colored("╒" + "═" * 8 + "╤" + "═" * 15 + "╤" + "═" * 13 + "╤" + "═" * 12 + "╤" + "═" * 17 + "╤" + "═" * 14 + "╕", 'blue'))
    print(colored("│", 'blue') + colored(format_column('PID', col_widths['PID']), 'yellow') + colored("│", 'blue') +
          colored(format_column('Arrival Time', col_widths['Arrival Time']), 'yellow') + colored("│", 'blue') +
          colored(format_column('Burst Time', col_widths['Burst Time']), 'yellow') + colored("│", 'blue') +
          colored(format_column('Wait Time', col_widths['Wait Time']), 'yellow') + colored("│", 'blue') +
          colored(format_column('Turnaround Time', col_widths['Turnaround Time']), 'yellow') + colored("│", 'blue') +
          colored(format_column('Finish Time', col_widths['Finish Time']), 'yellow') + colored("│", 'blue'))
    print(colored("╞" + "═" * 8 + "╪" + "═" * 15 + "╪" + "═" * 13 + "╪" + "═" * 12 + "╪" + "═" * 17 + "╪" + "═" * 14 + "╡", 'blue'))
    
    # Impressão dos resultados na tabela
    for item in dados:
        item['tempo_execucao'] = 'Null'
        print(colored("│", 'blue') + colored(format_column(item['pid'], col_widths['PID']), 'green') +
              colored("│", 'blue') + colored(format_column(item['arrival_time'], col_widths['Arrival Time']), 'green') +
              colored("│", 'blue') + colored(format_column(item['burst_time'], col_widths['Burst Time']), 'green') +
              colored("│", 'blue') + colored(format_column(item['wait_time'], col_widths['Wait Time']), 'green') +
              colored("│", 'blue') + colored(format_column(item['turnaround_time'], col_widths['Turnaround Time']), 'green') +
              colored("│", 'blue') + colored(format_column(item['finish_time'], col_widths['Finish Time']), 'green') +
              colored("│", 'blue'))   
    
    # Impressão do Tempo Total de Execução
    print(colored("╞" + "═" * 8 + "╧" + "═" * 15 + "╧" + "═" * 13 + "╧" + "═" * 12 + "╧" + "═" * 17 + "╧" + "═" * 14 + "╡", 'blue'))
    print(colored(colored("│", 'blue') + colored(" " * total_time_padding_left + f"{total_time_str}" + " " * total_time_padding_right, 'cyan') + colored("│", 'blue'), 'cyan'))
    print(colored("╞" + "═" * (SJF_MAX_WIDTH) + "╡", 'blue'))

    # Impressão do Tempo Médio
    print(colored("│", 'blue') + colored(" " * avg_padding_left + f"{average_str}" + " " * avg_padding_right, 'cyan') + colored("│", 'blue'))
    print(colored("╘" + "═" * (SJF_MAX_WIDTH) + "╛", 'blue'))

def print_table_rr(dados, avg, total_exec_time):
    average_str = f"Tempo Médio: {avg:.2f} u.t"
    total_exec_time_str = f"Tempo Total de Execução: {total_exec_time:.2f} u.t"

    # Calcula os espaços de preenchimento à esquerda e à direita
    avg_padding = (RR_MAX_WIDTH - len(average_str)) // 2
    total_exec_time_padding = (RR_MAX_WIDTH - len(total_exec_time_str)) // 2

    # Certifica-se de que os preenchimentos não sejam negativos
    avg_padding_left = max(avg_padding, 0)
    avg_padding_right = RR_MAX_WIDTH - len(average_str) - avg_padding_left
    total_exec_time_padding_left = max(total_exec_time_padding, 0)
    total_exec_time_padding_right = RR_MAX_WIDTH - len(total_exec_time_str) - total_exec_time_padding_left

    # Definindo os comprimentos das colunas
    col_widths = {
        'PID': 6,
        'Burst Time': 11,
        'Wait Time': 10,
        'Turnaround Time': 15,
        'Finish Time': 12
    }
    
    # Impressão do cabeçalho da tabela
    print(colored("╒" + "═" * 8 + "╤" + "═" * 13 + "╤" + "═" * 12 + "╤" + "═" * 17 + "╤" + "═" * 14 + "╕", 'blue'))
    print(colored("│", 'blue') + colored(format_column('PID', col_widths['PID']), 'yellow') + colored("│", 'blue') +
          colored(format_column('Burst Time', col_widths['Burst Time']), 'yellow') + colored("│", 'blue') +
          colored(format_column('Wait Time', col_widths['Wait Time']), 'yellow') + colored("│", 'blue') +
          colored(format_column('Turnaround Time', col_widths['Turnaround Time']), 'yellow') + colored("│", 'blue') +
          colored(format_column('Finish Time', col_widths['Finish Time']), 'yellow') + colored("│", 'blue'))
    print(colored("╞" + "═" * 8 + "╪" + "═" * 13 + "╪" + "═" * 12 + "╪" + "═" * 17 + "╪" + "═" * 14 + "╡", 'blue'))
    
    # Impressão dos resultados na tabela
    for item in dados:
        print(colored("│", 'blue') + colored(format_column(item['pid'], col_widths['PID']), 'green') +
              colored("│", 'blue') + colored(format_column(item['burst_time'], col_widths['Burst Time']), 'green') +
              colored("│", 'blue') + colored(format_column(item['wait_time'], col_widths['Wait Time']), 'green') +
              colored("│", 'blue') + colored(format_column(item['turnaround_time'], col_widths['Turnaround Time']), 'green') +
              colored("│", 'blue') + colored(format_column(item['finish_time'], col_widths['Finish Time']), 'green') +
              colored("│", 'blue'))   
    
    # Impressão do Tempo Total de Execução
    print(colored("╞" + "═" * 8 + "╧" + "═" * 13 + "╧" + "═" * 12 + "╧" + "═" * 17 + "╧" + "═" * 14 + "╡", 'blue'))
    print(colored(colored("│", 'blue') + colored(" " * total_exec_time_padding_left + f"{total_exec_time_str}" + " " * total_exec_time_padding_right, 'cyan') + colored("│", 'blue'), 'cyan'))
    
    # Impressão do Tempo Médio
    print(colored("╞" + "═" * RR_MAX_WIDTH + "╡", 'blue'))
    print(colored(colored("│", 'blue') + colored(" " * avg_padding_left + f"{average_str}" + " " * avg_padding_right, 'cyan') + colored("│", 'blue'), 'cyan'))
    
    print(colored("╘" + "═" * RR_MAX_WIDTH + "╛", 'blue'))

def print_execution_order(order):
    # Configurações
    max_line_length = 190

    # Criar a string de ordem formatada
    formatted_order = ' ➔  '.join(order)

    # Verificar se a linha é longa demais
    if len(formatted_order) > max_line_length:
        # Dividir a string em múltiplas linhas
        lines = [formatted_order[i:i + max_line_length] for i in range(0, len(formatted_order), max_line_length)]
        
        # Impressão do cabeçalho
        print(colored("\n  Ordem de Execução dos Processos:", 'yellow'))

        # Impressão de cada linha
        for line in lines:
            print(colored('│', 'blue') + colored(' ' + line + ' ', 'green') + colored('│', 'blue'))
    else:
        # Comprimento da linha
        max_length = len(formatted_order) + 2  # 1 espaço de cada lado

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
        print(bottom_border); print()

