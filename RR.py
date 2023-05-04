import queue
from operator import itemgetter

# rr스케줄링 실행 함수
def round_robin_scheduling(processes, quantum):
    # 프로세스를 정장할 큐 초기화
    process_queue = queue.Queue()
    # 현재 시간을 0으로 초기화
    current_time = 0
    # 완료된 프로세스를 저장할 목록 초기화
    completed_processes = []

    # 도착 시간별로 입력 프로세스 정렬
    processes = sorted(processes, key=itemgetter('arrival_time'))

    # 프로세스 대기열에 첫 번째 프로세스 추가
    process_queue.put(processes.pop(0))

    # 프로세스 대기열이 비워질 때까지 rr 진행
    while not process_queue.empty():
       # 대기열에서 다음 프로세스 가져오기
        current_process = process_queue.get()

        # 현재 프로세스의 실행 시간 결정
        execution_time = min(quantum, current_process['remaining_time'])
        # 프로세스의 남은 시간 업데이트
        current_process['remaining_time'] -= execution_time
       # 프로세스 실행 후 현재 시간 업데이트
        current_time += execution_time

        # 새 프로세스가 도착했는지 확인하고 대기열에 추가
        while processes and processes[0]['arrival_time'] <= current_time:
            process_queue.put(processes.pop(0))

        # 현재 프로세스에 남은 시간이 있으면 대기열에 다시 추가
        if current_process['remaining_time'] > 0:
            # 대기열에 있는 다른 프로세스의 대기 시간 업데이트
            for process in list(process_queue.queue):
                process['waiting_time'] += execution_time
            process_queue.put(current_process)
        else:
            # 완료된 프로세스의 소요 시간, 종료 시간 및 NTT 계산
            current_process['turnaround_time'] = current_time - current_process['arrival_time']
            current_process['end_time'] = current_time
            current_process['NTT'] = current_process['turnaround_time'] / current_process['burst_time']
            # 완료된 프로세스 목록에 완료된 프로세스 추가
            completed_processes.append(current_process)

        # 완료된 프로세스 목록 반환
    return completed_processes

# 프로세스를 저장할 빈 목록 초기화
processes = []
quantum = 2


if __name__ == '__main__':

    process_id = 0
    while True:
        process_info = input(f"Enter Arrival Time and Burst Time for Process {process_id} (-1 to finish): ")
        if process_info.strip() == "-1":
            break
        else:
            arrival_time, burst_time = map(int, process_info.split())
            processes.append({'id': process_id, 'arrival_time': arrival_time, 'burst_time': burst_time, 'remaining_time': burst_time, 'waiting_time': 0})
            process_id += 1

    # Allow users to specify the time quantum directly
    quantum = int(input("Enter the time quantum: "))

    # rr 스케줄링 함수 호출
    completed_processes = round_robin_scheduling(processes, quantum)

    # 프로세스 ID별로 완료된 프로세스 정렬
    completed_processes = sorted(completed_processes, key=itemgetter('id'))

    
    print(f"{'Process ID':<12} {'Burst time':<12} {'Arrival time':<20} {'Waiting time':<20} {'End time':<12} {'Turnaround time':<20} {'NTT':<12}")

    # 완료된 프로세스를 반복하여 세부 정보를 인쇄합니다
    for process in completed_processes:
        print("{:<12} {:<12} {:<20} {:<20} {:<12} {:<20} {:<12.1f}".format(process['id'], process['burst_time'], process['arrival_time'], process['waiting_time'], process['end_time'], process['turnaround_time'], process['NTT']))

