import queue
import scheduling 
import process as Pro
import processor as Prosor

#0번 부터 순차적으로 켜져있고 비어있는 프로세서를 찾아 넣는다.
def processor_allocate(ready_Q = queue.Queue()) :
  for i in range(4) :
    if processor_list[i].Prosor.on_check() and not processor_list[i].Prosor.in_check() :
      processor_list[i].Proser.put_in(ready_Q)
    else : 
      pass

#입력에서 데이터를 받아 프로세스를 선언한다.
def definition(list_proc = []) :
  for i in range(len(list)) :
    Pro.proc_add(name = list[i][0], arr_time = list[i][1], bst_time = list[i][2])
    global process_list.append(Pro.globals()[list[i][0]])

#요소들을 리셋한다.
def reset_all() :
  global current_time = 0
  del global process_list[0:len(process_list)]
  del global done_list[0:len(done_list)]
  global full_power_cosume = 0
  global ready_queue.clear()

#AT와 수행시간을 비교해서 AT가 된 프로세스를 아직 안 끝난 프로세스 리스트에 가져온다.
def come_in(time = 0, proc_list = [], un_done = []):
  for i, v in enumerate(proc_list) :
    if v.process.a_time == time :
      un_done.append(v)
    else : 
      pass

def 

#본 프로그램 함수
def start_sequence(signal = 0) :
  reset_all()
  definition(global input_list)
  global

  while signal == 1 :
    #프로세스 리스트와 다 끝난 리스트의 길이가 같으면 반복을 종료.
    if len(global done_list) == len(global process_list) :
      break

    #들어올 프로세스가 있는 지 확인.
    come_in(time = global current_time, proc_list = global process_list, global undone_list)
    #프로세스가 들어오면 스케쥴링 기법을 시행.
    if flag_2 == 1 :
      flag_2 = 0
      if scheduling_method == 'FCFS' :
        scheduling.FCFS(global undone_list)
      elif scheduling_method == 'RR' :
        scheduling.RR(global undone_list)
      elif scheduling_method == 'SRN' :
        scheduling.SRN(global undone_list)
        global ready_queue.clear()
      elif scheduling_method == 'SRTN' :
        scheduling.SRTN(global undone_list)
        global ready_queue.clear()
      elif scheduling_method == 'HRRN' :
        scheduling.HRRN(global undone_list)
        global ready_queue.clear()
      else :





    global current_time += 1 

input_list = []
process_list = []
undone_list = []
done_list = []
processor_1 = Pro.prosessor()
processor_2 = Pro.prosessor()
processor_3 = Pro.prosessor()
processor_4 = Pro.prosessor()
processor_list = [processor_1, processor_2, processor_3, processor_4]
full_power_cosume = 0
current_time = 0
ready_queue = queue.Queue()
scheduling_method = 'FCFS'
start_flag = 0
flag_2 = 0
