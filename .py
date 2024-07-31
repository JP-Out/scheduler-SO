from termcolor import colored

def print_table_fcfs(dados, avg, total_exec_time):
    average = f"Tempo Médio: {avg:.2f} u.t"
    avg_time_half_length_string = ((43 - len(average))//2)
    double_avg_time_half_length_string = (avg_time_half_length_string * 2)
    
    total_time_str = f"Tempo Total de Execução: {total_exec_time} u.t"
    total_time_half_length_string = ((43 - len(total_time_str))//2)
    double_total_time_half_length_string = (total_time_half_length_string * 2)

    
    print(colored("╒" + "═" * 7 + "╤" + "═" * 17 + "╤" + "═" * 15 + "╤" + "═" * 17 + "╕", 'blue'))
    print(colored("│", 'blue') + colored(f" {'PID':<5} ", 'yellow') + colored("│", 'blue') + colored(f" {'Tempo de Espera':<15} ", 'yellow') + colored("│", 'blue') + colored(f" {'Burst Time':<13} ", 'yellow') + colored("│", 'blue') + colored(f" {'Tempo Execução':<15} ", 'yellow') + colored("│", 'blue'))
    print(colored("╞" + "═" * 7 + "╪" + "═" * 17 + "╪" + "═" * 15 + "╪" + "═" * 17 + "╡", 'blue'))
    
    for item in dados:
        print(colored("│", 'blue') + colored(f" {item['pid']:<5} ", 'green') + colored("│", 'blue') + colored(f" {item['tempo_espera']:<15} ", 'green') + colored("│", 'blue') + colored(f" {item['burst_time']:<13} ", 'green') + colored("│", 'blue') + colored(f" {item['tempo_execucao']:<15} ", 'green') + colored("│", 'blue'))
    
    print(colored("╞" + "═" * 7 + "╧" + "═" * 17 + "╧" + "═" * 15 + "╧" + "═" * 17 + "╡", 'blue'))
    print(colored("│" + " " * (double_total_time_half_length_string) + f"{total_time_str}" + " " * (double_total_time_half_length_string) + "│", 'cyan'))
    print(colored("╞" + "═" * 7 + "═" + "═" * 17 + "═" + "═" * 15 + "═" + "═" * 17 + "╡", 'blue'))
    print(colored("│" + (" " * (double_avg_time_half_length_string))  + f"{average}" + (" " * (double_avg_time_half_length_string)) + "│", 'cyan'))
    print(colored("╘" + "═" * 7 + "═" + "═" * 17 + "═" + "═" * 15 + "═" + "═" * 17 + "╛", 'blue'))

# Exemplo de dados
dados = [
    {"pid": "A", "tempo_espera": 0, "burst_time": 24, "tempo_execucao": 24},
    {"pid": "B", "tempo_espera": 24, "burst_time": 3, "tempo_execucao": 27},
    {"pid": "C", "tempo_espera": 27, "burst_time": 3, "tempo_execucao": 30}
]

# Chamando a função com os dados, tempo médio e tempo total de execução
print_table_fcfs(dados, avg=17, total_exec_time=30)
