# tabela.py
def print_tabela_fcfs(dados):
    print("╒" + "═" * 7 + "╤" + "═" * 17 + "╤" + "═" * 15 + "╕")
    print(f"│ {'PID':<5} │ {'Tempo de Espera':<15} │ {'Burst Time':<13} │")
    print("╞" + "═" * 7 + "╪" + "═" * 17 + "╪" + "═" * 15 + "╡")
    
    for item in dados:
        print(f"│ {item['pid']:<5} │ {item['tempo_espera']:<15} │ {item['burst_time']:<13} │")
    
    print("╘" + "═" * 7 + "╧" + "═" * 17 + "╧" + "═" * 15 + "╛")

def print_tabela_sjf(dados):
    print("╒" + "═" * 7 + "╤" + "═" * 17 + "╤" + "═" * 18 + "╤" + "═" * 17 + "╕")
    print(f"│ {'PID':<5} │ {'Tempo de Início':<15} │ {'Tempo de Término':<15} │ {'Tempo de Espera':<15} │")
    print("╞" + "═" * 7 + "╪" + "═" * 17 + "╪" + "═" * 18 + "╪" + "═" * 17 + "╡")
    
    for item in dados:
        print(f"│ {item['pid']:<5} │ {item.get('tempo_inicio', 'N/A'):<15} │ {item.get('tempo_termino', 'N/A'):<15} │ {item.get('tempo_espera', 'N/A'):<15} │")
    
    print("╘" + "═" * 7 + "╧" + "═" * 17 + "╧" + "═" * 18 + "╧" + "═" * 17 + "╛")
