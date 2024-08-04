from utils.visualizer import print_table_sjf, print_execution_order

def sjf_non_preemptive(processes, context_switch_time):
    # Cópia para exibição dos resultados
    original_processes = processes.copy()

    # Ordenar os processos pelo tempo de chegada e tempo de burst
    processes.sort(key=lambda x: (x["arrival_time"], x["burst_times"][0]))

    # Inicialização
    current_time = 0
    total_waiting_time = 0
    table_data = []
    execution_order = []

    while processes:
        # Filtrar processos que chegaram até o tempo atual
        available_processes = [p for p in processes if p["arrival_time"] <= current_time]
        
        # Selecionar o processo com menor tempo de burst
        if available_processes:
            current_process = min(available_processes, key=lambda x: x["burst_times"][0])
            processes.remove(current_process)

            # Adiciona o tempo de troca de contexto, se não for o primeiro processo
            if execution_order:
                current_time += context_switch_time

            current_process["start_time"] = current_time  # Define o tempo de início do processo atual
            current_process["finish_time"] = current_time + current_process["burst_times"][0]  # Calcula o tempo de término do processo atual
            current_process["wait_time"] = current_process["start_time"] - current_process["arrival_time"]  # Calcula o tempo de espera do processo atual
            
            execution_order.append(current_process["pid"])

            # Atualiza `current_time`, incrementa `total_waiting_time`
            current_time = current_process["finish_time"]
            total_waiting_time += current_process["wait_time"]
        else:
            current_time += 1

    # Exibir resultados
    for p in original_processes:
        table_data.append({  # Cria a tabela com os dados
                "pid": p["pid"],
                "arrival_time": p["arrival_time"],
                "burst_time": p["burst_times"][0],
                "start_time": p.get("start_time", "N/A"),
                "finish_time": p.get("finish_time", "N/A"),
                "wait_time": p.get("wait_time", "N/A"),
                "turnaround_time": (p.get("finish_time", 0) - p["arrival_time"]) if p.get("finish_time") != "N/A" else "N/A"
        })

    if original_processes:  # Evita ZeroDivisionError
        average_waiting_time = total_waiting_time / len(original_processes)
    else:
        print("No processes to calculate the average waiting time.")
    
    total_exec_time = current_time
    print(); print_table_sjf(table_data, average_waiting_time, total_exec_time)
    print_execution_order(execution_order)