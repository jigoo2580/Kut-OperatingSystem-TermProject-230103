def hrrn_scheduling(processes):
    time = 0
    completed_processes = []
    process_queue = []

    while True:
        # ����ð����� �����ð��� ���� ���μ����� queue�� ����
        for process in processes:
            if process.arrival_time <= time and process not in completed_processes and process not in process_queue:
                process_queue.append(process)

        # queue�� ���μ��� ���� �� �����ٸ� ����
        if not process_queue:
            break

        # the response ratio ��� �� ���� ���� ���μ��� ����
        for process in process_queue:
            process.response_ratio = 1 + (time - process.arrival_time) / process.burst_time
        selected_process = max(process_queue, key=lambda x: x.response_ratio)

        # ����ð� ����
        selected_process.waiting_time = time - selected_process.arrival_time
        selected_process.turnaround_time = selected_process.waiting_time + selected_process.burst_time
        selected_process.normalized_turnaround_time = selected_process.turnaround_time / selected_process.burst_time

        # result ���
        print(f"Process {selected_process.pid} is completed.")
        print(f"\tWaiting Time: {selected_process.waiting_time}")
        print(f"\tTurnaround Time: {selected_process.turnaround_time}")
        print(f"\tNormalized Turnaround Time: {selected_process.normalized_turnaround_time}")

        # �Ϸ��� ���μ��� ó��
        completed_processes.append(selected_process)
        process_queue.remove(selected_process)

        # current time ������Ʈ
        time += selected_process.burst_time

    return completed_processes

'''
n = int(input("Enter the number of processes: "))
processes = []
for i in range(n):
    pid = i + 1
    arrival_time = int(input(f"Enter the arrival time for process {pid}: "))
    burst_time = int(input(f"Enter the burst time for process {pid}: "))
    processes.append(Process(pid, arrival_time, burst_time))
'''