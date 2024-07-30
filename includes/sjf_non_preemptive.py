from utils.visualizer import print_table_sjf, print_execution_order

def sjf_non_preemptive(processes):
    # Cópia para exibição dos resultados
    processos_originais = processes.copy()

    # Ordenar os processos pelo tempo de chegada e tempo de rajada
    processes.sort(key=lambda x: (x["arrival_time"], x["burst_times"][0]))

    # Inicialização
    tempo_atual = 0
    tempo_espera_total = 0
    tabela_dados = []
    ordem_execucao = []

    while processes:

        # Filtrar processos que chegaram até o tempo atual
        processos_disponiveis = [
            p for p in processes if p["arrival_time"] <= tempo_atual
        ]
        
        
        # Selecionar o processo com menor tempo de execução
        if processos_disponiveis:
            processo_atual = min(
                processos_disponiveis, key=lambda x: x["burst_times"][0]
            )
            processes.remove(processo_atual)

            processo_atual["tempo_inicio"] = (
                tempo_atual  # Define o tempo de início do processo atual.
            )
            processo_atual["tempo_termino"] = (
                tempo_atual + processo_atual["burst_times"][0]  # Calcula o tempo de término do processo atual.
            )
            processo_atual["tempo_espera"] = (
                processo_atual["tempo_inicio"] - processo_atual["arrival_time"]  # Calcula o tempo de espera do processo atual.
            )
            
            ordem_execucao.append(processo_atual["pid"])

            # Atualiza `tempo_atual`, incrementa `tempo_espera_total`
            tempo_atual = processo_atual["tempo_termino"]
            tempo_espera_total += processo_atual["tempo_espera"]
        else:
            tempo_atual += 1

    # Exibir resultados
    for p in processos_originais:
        tabela_dados.append({ # Cria a tabela com os dados
                "pid": p["pid"],
                "tempo_inicio": p.get("tempo_inicio", "N/A"),
                "tempo_termino": p.get("tempo_termino", "N/A"),
                "tempo_espera": p.get("tempo_espera", "N/A"),
        })

    if processos_originais:  # Evita ZeroDivisionError
        tempo_espera_medio = tempo_espera_total / len(processos_originais)
    else:
        print("Não há processos para calcular o tempo de espera médio.")
    
    print('\n')
    print_table_sjf(tabela_dados, tempo_espera_medio)
    print_execution_order(ordem_execucao)