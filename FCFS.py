from queue import Queue
from operator import itemgetter

def fcfs(processes):
    # 실행 시간, 종료 시간, 대기 시간을 저장할 리스트를 생성합니다.
    end_times = []
    waiting_times = []

    # Assign process IDs automatically in the order of their appearance
    for i, process in enumerate(processes):
        process['id'] = i

    # arrival_time으로 정렬함
    data = sorted(processes, key=itemgetter('arrival_time'))

    queue = Queue()
    current_time = 0
    idx = 0

    while not queue.empty() or idx < len(data):
        # arrival_time에 맞춰서 큐에 프로세스를 추가합니다.
        while idx < len(data) and data[idx]['arrival_time'] <= current_time:
            process = data[idx]
            queue.put(process)
            idx += 1

        if not queue.empty():
            process = queue.get()

            # 프로세스의 대기 시간을 계산합니다.
            waiting_time = current_time - process['arrival_time']

            # 프로세스를 실행합니다.
            print(f"현재 시간: {current_time}")
            print(f"프로세스 {process['id']} 실행 중...")
            for _ in range(process['burst_time']):
                current_time += 1

                # arrival_time에 맞춰서 큐에 프로세스를 추가합니다.
                while idx < len(data) and data[idx]['arrival_time'] <= current_time:
                    new_process = data[idx]
                    queue.put(new_process)
                    idx += 1

            # 프로세스의 종료 시간, 대기 시간을 저장합니다.
            process['end_time'] = current_time
            process['waiting_time'] = waiting_time
            process['turnaround_time'] = process['end_time'] - process['arrival_time']
            process['NTT'] = process['turnaround_time'] / process['burst_time']

            # 종료된 프로세스는 결과 리스트에 추가합니다.
            end_times.append(process['end_time'])
            waiting_times.append(process['waiting_time'])
        else:
            current_time += 1

    # 결과를 출력합니다.
    print(f"{'Process ID':<12} {'Burst time':<12} {'Arrival time':<20} {'Waiting time':<20} {'End time':<12} {'turnaround time':<20} {'NTT':<12}")
    for process in processes:
        print(f"{process['id']:<12} {process['burst_time']:<12} {process['arrival_time']:<20} {process['waiting_time']:<20} {process['end_time']:<12} {process['turnaround_time']:<20} {process['NTT']:<12.1f}")

    # 결과를 반환합니다.
    return end_times, waiting_times


def get_user_input():
    processes = []  
    process_id = 0
    while True:
        process_info = input(f"Enter Arrival Time and Burst Time for Process {process_id} (-1 to finish): ")
        if process_info.strip() == "-1":
            break
        else:
            arrival_time, burst_time = map(int, process_info.split())
            processes.append({'id': process_id, 'arrival_time': arrival_time, 'burst_time': burst_time, 'remaining_time': burst_time, 'waiting_time': 0})
            process_id += 1

    return processes

# 예제를 실행합니다.
if __name__ == '__main__':
    processes = get_user_input()
    end_times, waiting_times = fcfs(processes)
    print(f"Average waiting time: {sum(waiting_times)/len(waiting_times)}")
    print(f"Average turnaround time: {sum(end_times)/len(end_times)}")

