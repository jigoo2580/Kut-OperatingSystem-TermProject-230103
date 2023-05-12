import queue
import scheduling_al
import process as Pro
import processor as Prosor
import time

input_list = []
process_list = []
undone_list = []
done_list = []
processor_1 = Prosor.processor()
processor_2 = Prosor.processor()
processor_3 = Prosor.processor()
processor_4 = Prosor.processor()
processor_list = [processor_1, processor_2, processor_3, processor_4]
full_power_cosume = 0
current_time = 0
ready_queue = queue.Queue()
scheduling_method = 'FCFS'
start_flag = 0 #시작 플래그
flag_2 = 0 #프로세스 도착 플래그
test = False

#프로세서가 이미 코어에 들어가 있는지 확인.
def processor_check(proc = Pro.process(), flag = [], lst = []) :
  for i in range(4) :
    if lst[i].on_check() != False :
      flag[i] = 1
    if flag[i] == 0 and lst[i].in_check() and proc == lst[i].in_proc :
      flag[i] = 1

#0번 부터 순차적으로 켜져있고 비어있는 프로세서를 찾아 넣는다.
def processor_allocate(que = queue.Queue(), lst = []) :
  flag_processor_can_work = [0, 0, 0, 0] #들어갈 수 있으면 0 못들어 가면 1
  for i in range(4) :
    proc = que.get()
    print(f'{proc}+ :proc')
    que.get() #큐에서 받아오기
    print(f'{i}+i')
    print(flag_processor_can_work)
    processor_check(proc = proc, flag = flag_processor_can_work, lst = lst) #들어갈 수 있는 공간이 있는지 확인
    for j in range(4) :
      print(f'{j}+j')
      if flag_processor_can_work[j] == 0 :
        lst[j].put_in(proc)
        flag_processor_can_work[j] = 1
        j = 1
      else : 
        pass
      if 0 not in flag_processor_can_work : #모든 프로세서에 들어갈 수 없으면, 끝낸다.
        return 0

#입력에서 데이터를 받아 프로세스를 선언한다.
def definition(list_proc = [], lst2 = []) :
  for i in range(len(list_proc)) :
    Pro.proc_add(name = list_proc[i][0], arr_time = list_proc[i][1], bst_time = list_proc[i][2], lst = lst2)

#요소들을 리셋한다.
def reset_all() :
  current_time = 0
  del process_list[0:len(process_list)]
  del done_list[0:len(done_list)]
  full_power_cosume = 0
  ready_queue = queue.Queue()

#AT와 수행시간을 비교해서 AT가 된 프로세스를 아직 안 끝난 프로세스 리스트에 가져온다.
def come_in(arr_time = 0, proc_list = [], un_done = [], flag = 0):
    for i, v in enumerate(proc_list) :
      if v.a_time == arr_time :
        un_done.append(v)
        flag = 1
      else : 
        pass
    return flag


#정렬된 리스트를 레디 큐에 집어넣기
def into_Q(proc_list = [], que = queue.Queue()) :
  for i in range(len(proc_list)) :
    que.put(proc_list[i])

#본 프로그램 함수
def start_sequence(signal = 0) :
  global current_time
  global process_list
  global flag_2
  global done_list
  global undone_list
  global scheduling_method
  global ready_queue
  global processor_list
  
  print(processor_list)

  reset_all()
  definition(input_list, process_list)

  while signal == 1 :
    #프로세스 리스트와 다 끝난 리스트의 길이가 같으면 반복을 종료.
    print(len(done_list), len(process_list))
    if len(done_list) == len(process_list) :
      break

    #들어올 프로세스가 있는 지 확인.
    print(current_time)
    flag_2 = come_in(arr_time = current_time, proc_list = process_list, un_done = undone_list, flag = flag_2)
    #프로세스가 들어오면 스케쥴링 기법을 시행.
    print(flag_2)
    if flag_2 == 1 :
      flag_2 = 0
      if scheduling_method == 'FCFS' :
        scheduling_al.FCFS(lst = undone_list)
      elif scheduling_method == 'RR' :
        pass
      elif scheduling_method == 'SRN' :
        scheduling_al.SPN(undone_list)
        ready_queue.queue.clear()
      elif scheduling_method == 'SRTN' :
        scheduling_al.SRTN(undone_list)
        ready_queue.queue.clear()
      elif scheduling_method == 'HRRN' :
        scheduling_al.HRRN(undone_list)
        ready_queue.clear()
      else :
        scheduling_al.new(undone_list)
      #큐에 현재 온 프로세스들 넣기
      into_Q(undone_list, ready_queue)
      #큐에서 프로세서로 할당하기
      processor_allocate(que = ready_queue, lst = processor_list)
      print('hi')
      #프로세서 돌리기
      for i in range(4) : 
        if processor_list[i].in_proc.proc_name != 'none' :
          processor_list[i].running()
          processor_list[i].in_proc.work_while[1] = current_time + 1
          if processor_list[i].in_proc.work_state == 0 :
            processor_list[i].in_proc.work_state = 1
          elif processor_list[i].in_proc.work_state == 1 :
            processor_list[i].in_proc.work_state = 2
          else :
            pass
          if processor_list[i].in_proc.lb_time == 0 :
            processor_list[i].in_proc.work_state = 0
            processor_list[i].put_out(un_done = ready_queue, lst = undone_list, lst2 = done_list)
          else :
            if scheduling_method == 'RR' :
              scheduling_al.RR(undone_list)
            elif scheduling_method == 'new' : 
              scheduling_al.new(undone_list)
            processor_list[i].in_proc.work_state = 0
            processor_list[i].put_out(un_done = ready_queue, lst = undone_list, lst2 = done_list)
 
    current_time += 1
    if test == True : 
        print('=============================================')
        for i in range(len(process_list)) :
          process_list[i].see_in_val()
        print('=============================================')
        for i in range(len(undone_list)) :
          undone_list[i].see_in_val()
        print('=============================================')
        for i in range(len(done_list)) :
          done_list[i].see_in_val()
        print('=============================================')
        for i in range(4) :
            processor_list[i].in_proc.see_in_val()
        print('=============================================')
    time.sleep(1.0)

test = True
if test == True :
  processor_1.on_off()
  processor_2.on_off()
  input_list = [['t1', 0, 7], ['t2', 0, 4], ['t3', 1, 2], ['t4', 5, 4], ['t5', 20, 7]]
  start_sequence(1)
