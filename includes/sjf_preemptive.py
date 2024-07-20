
STATS = ('criado', 'pronto', 'executando', 'bloqueado', 'encerrado')

def sjf_preemptive(processes):
    # Inicialização de variáveis
    n = len(processes)
    remaining_times = [process['burst_times'][0] for process in processes]  # Tempos restantes de cada processo
    complete = 0  # Número de processos completos
    t = 0  # Tempo corrente
    min_remaining_time = float('inf')
    shortest = 0
    check = False

    wait_time = [0] * n  # Lista de tempos de espera para cada processo

    # Loop até que todos os processos sejam completados
    while complete != n:
        # Encontrar o processo com o menor tempo de execução restante que tenha chegado
        for j in range(n):
            if (processes[j]['arrival_time'] <= t and
                remaining_times[j] < min_remaining_time and
                remaining_times[j] > 0):
                min_remaining_time = remaining_times[j]
                shortest = j
                check = True

        if not check:
            t += 1
            continue

        # Reduzir o tempo restante do processo encontrado
        remaining_times[shortest] -= 1

        # Atualizar o menor tempo restante
        min_remaining_time = remaining_times[shortest]
        if min_remaining_time == 0:
            min_remaining_time = float('inf')

        # Se o processo é completado
        if remaining_times[shortest] == 0:
            complete += 1
            check = False

            # Calcular tempo de espera
            finish_time = t + 1
            wait_time[shortest] = (finish_time - processes[shortest]['burst_times'][0] -
                                   processes[shortest]['arrival_time'])

            if wait_time[shortest] < 0:
                wait_time[shortest] = 0

        # Incrementar o tempo corrente
        t += 1

    # Calcular e imprimir o tempo médio de espera
    total_wait_time = sum(wait_time)
    avg_wait_time = total_wait_time / n
    print(f"Tempo médio de espera: {avg_wait_time:.2f}")

    sjf_preemptive(processes)