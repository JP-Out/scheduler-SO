from termcolor import colored

def print_table_fcfs(dados, avg, total_exec_time):
    average_str = f"Tempo Médio: {avg:.2f} u.t" # Armazena o tempo médio em uma string
    avg_time_half_length_string = ((93 - len(average_str))//2) # Pega o tamanho da `average_str`, subtrai pelo largura da tabela (93) e divide por 2, para conseguir a tabela responsiva
    
    total_time_str = f"Tempo Total de Execução: {total_exec_time} u.t"
    total_time_half_length_string = ((93 - len(total_time_str))//2)

    # Impressão do cabeçalho da tabela
    print(colored("╒" + "═" * 7 + "╤" + "═" * 17 + "╤" + "═" * 15 + "╤" + "═" * 17 + "╤" + "═" * 17 + "╤" + "═" * 13 + "╕", 'blue'))
    print(colored("│", 'blue') + colored(f" {'PID':<5} ", 'yellow') + colored("│", 'blue') + colored(f" {'Wait Time':<15} ", 'yellow') + colored("│", 'blue') + colored(f" {'Burst Time':<13} ", 'yellow') + colored("│", 'blue') + colored(f" {'Execution Time':<15} ", 'yellow') + colored("│", 'blue') + colored(f" {'Turnaround Time':<15} ", 'yellow') + colored("│", 'blue') + colored(f" {'Finish Time':<10} ", 'yellow') + colored("│", 'blue'))
    print(colored("╞" + "═" * 7 + "╪" + "═" * 17 + "╪" + "═" * 15 + "╪" + "═" * 17 + "╪" + "═" * 17 + "╪" + "═" * 13 + "╡", 'blue'))

    
    # Impressão dos resultados na tabela
    for item in dados:
        item['turnaround_time'] = item['tempo_espera'] + item['burst_time']  # Calcula Turnaround Time
        item['finish_time'] = item['tempo_execucao']  # Finish Time (valor fictício igual a Execution Time)

        print(colored("│", 'blue') + colored(f" {item['pid']:<5} ", 'green') +
              colored("│", 'blue') + colored(f" {item['tempo_espera']:<15} ", 'green') +
              colored("│", 'blue') + colored(f" {item['burst_time']:<13} ", 'green') +
              colored("│", 'blue') + colored(f" {item['tempo_execucao']:<15} ", 'green') +
              colored("│", 'blue') + colored(f" {item['turnaround_time']:<15} ", 'green') +
              colored("│", 'blue') + colored(f" {item['finish_time']:<11} ", 'green') +
              colored("│", 'blue'))    
        
    # Impressão do Tempo Total de Execução
    print(colored("╞" + "═" * 7 + "╧" + "═" * 17 + "╧" + "═" * 15 + "╧" + "═" * 17 + "╧" + "═" * 17 + "╧" + "═" * 13 + "╡", 'blue'))
    print(colored("│" + " " * (total_time_half_length_string) + f"{total_time_str}" + " " * ((total_time_half_length_string)-2) + "│", 'cyan'))
    print(colored("╞" + "═" * 91 + "╡", 'blue'))

    
    # Impressão do Tempo Médio
    print(colored("│" + (" " * (avg_time_half_length_string))  + f"{average_str}" + (" " * ((avg_time_half_length_string)-1)) + "│", 'cyan'))
    print(colored("╘" + "═" * 91 + "╛", 'blue'))

# Exemplo de dados
dados = [
    {"pid": "A", "tempo_espera": 0, "burst_time": 24, "tempo_execucao": 24},
    {"pid": "B", "tempo_espera": 24, "burst_time": 3, "tempo_execucao": 27},
    {"pid": "C", "tempo_espera": 27, "burst_time": 3, "tempo_execucao": 30}
]

# Chamando a função com os dados, tempo médio e tempo total de execução
print_table_fcfs(dados, avg=17, total_exec_time=30)