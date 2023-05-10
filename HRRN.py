def hrrn_scheduling(processes):
    time = 0
    completed_processes = []
    process_queue = []

    while True:
        # 현재시간보다 도착시간이 빠른 프로세스를 queue에 저장
        for process in processes:
            if process.arrival_time <= time and process not in completed_processes and process not in process_queue:
                process_queue.append(process)

        # queue에 프로세스 없을 시 스케줄링 종료
        if not process_queue:
            break

        # the response ratio 계산 및 가장 높은 프로세스 선택
        for process in process_queue:
            process.response_ratio = 1 + (time - process.arrival_time) / process.burst_time
        selected_process = max(process_queue, key=lambda x: x.response_ratio)

        # 실행시간 측정
        selected_process.waiting_time = time - selected_process.arrival_time
        selected_process.turnaround_time = selected_process.waiting_time + selected_process.burst_time
        selected_process.normalized_turnaround_time = selected_process.turnaround_time / selected_process.burst_time

        # result 출력
        print(f"Process {selected_process.pid} is completed.")
        print(f"\tWaiting Time: {selected_process.waiting_time}")
        print(f"\tTurnaround Time: {selected_process.turnaround_time}")
        print(f"\tNormalized Turnaround Time: {selected_process.normalized_turnaround_time}")

        # 완료한 프로세스 처리
        completed_processes.append(selected_process)
        process_queue.remove(selected_process)

        # current time 업데이트
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