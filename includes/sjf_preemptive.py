import heapq
from utils.visualizer import print_table_sjf, print_execution_order

def sjf_preemptive(processes):
    # Cópia para exibição dos resultados
    original_processes = processes.copy()

    # Ordenar os processos pelo tempo de chegada
    processes.sort(key=lambda x: x["arrival_time"])

    # Inicializando as variáveis
    execution_order = []
    current_time = 0
    total_waiting_time = 0
    table_data = []
    min_heap = []
    process_index = 0
    n = len(processes)
    burst_remaining = {process['pid']: process['burst_time'] for process in processes}
    start_times = {}
    end_times = {}
    wait_times = {process['pid']: 0 for process in processes}
    completed = 0

    while completed < n:
        while process_index < n and processes[process_index]['arrival_time'] <= current_time:
            heapq.heappush(min_heap, (burst_remaining[processes[process_index]['pid']], processes[process_index]['pid']))
            process_index += 1

        if min_heap:
            _, current_pid = heapq.heappop(min_heap)  # Obtém o processo com o menor tempo de burst restante
            if current_pid not in start_times:
                start_times[current_pid] = current_time  # Registra o tempo de início do processo

            execution_order.append(current_pid)

            current_time += 1  # Incrementa o tempo atual (simula a execução do processo por uma unidade de tempo)
            burst_remaining[current_pid] -= 1  # Decrementa o tempo de burst restante do processo

            if burst_remaining[current_pid] == 0:  # Processo completado
                completed += 1  # Incrementa o contador de processos completados
                end_times[current_pid] = current_time  # Registra o tempo de término do processo
                current_process = next(p for p in processes if p['pid'] == current_pid)  # Obtém o processo atual da lista original
                wait_times[current_pid] = end_times[current_pid] - current_process['arrival_time'] - current_process['burst_time']  # Calcula o tempo de espera do processo
                total_waiting_time += wait_times[current_pid]  # Acumula o tempo de espera no total
            else:
                heapq.heappush(min_heap, (burst_remaining[current_pid], current_pid))  # Se o processo não for completado, o re-adiciona na heap com o novo tempo de burst restante
        else:
            current_time += 1  # Se não houver processos na heap, incrementa o tempo atual para esperar pela chegada de novos processos

    # Exibir resultados
    for p in original_processes:
        table_data.append({
            'pid': p['pid'],
            'arrival_time': p['arrival_time'],
            'burst_time': p['burst_time'],
            'start_time': start_times.get(p['pid'], 'N/A'),
            'finish_time': end_times.get(p['pid'], 'N/A'),
            'wait_time': wait_times.get(p['pid'], 'N/A'),
            'turnaround_time': end_times.get(p['pid'], 'N/A') - p['arrival_time'] if end_times.get(p['pid'], 'N/A') != 'N/A' else 'N/A'
        })

    if original_processes:  # Evitar ZeroDivisionError
        average_waiting_time = total_waiting_time / len(original_processes)
    else:
        print("No processes to calculate the average waiting time.")

    total_exec_time = current_time  # Assume que o total_exec_time é o tempo final do último processo
    print(); print_table_sjf(table_data, average_waiting_time, total_exec_time)
    print_execution_order(execution_order)
