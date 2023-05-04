def HRRN(processes, p_cores, e_cores):
    n_processes = len(processes)
    waiting_time = [0] * n_processes
    turnaround_time = [0] * n_processes
    normalized_turnaround_time = [0] * n_processes
    executed_processes = []
    quantum = 1

    queue = PriorityQueue()
    for i in range(n_processes):
        queue.put(processes[i])

    while not queue.empty():
        # 프로세스에 코어 할당합니다
        n_cores = min(p_cores + e_cores, queue.qsize())
        p_processes = [queue.get() for _ in range(min(p_cores, n_cores))]
        e_processes = [queue.get() for _ in range(min(e_cores, n_cores - p_cores))]
        for process in p_processes:
            process.core = "P"
        for process in e_processes:
            process.core = "E"
        assigned_processes = p_processes + e_processes

        # 프로세스를 실행합니다
        for process in assigned_processes:
            process.execute(quantum)
            if process.remaining_time == 0:
                executed_processes.append(process)
            else:
                queue.put(process)

        # waiting_time을 업데이트합니다
        for process in queue.queue:
            process.waiting_time += quantum

    for i, process in enumerate(executed_processes):
        waiting_time[i] = process.waiting_time
        turnaround_time[i] = process.turnaround_time
        normalized_turnaround_time[i] = turnaround_time[i] / process.burst_time

    return waiting_time, turnaround_time, normalized_turnaround_time