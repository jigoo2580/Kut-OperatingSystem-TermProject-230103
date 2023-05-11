import process

#아무것도 아닌 프로세스(프로세스 없음 == 초깃값)
none = process.process()
none.value_input(name = none, arr_time = -1, bst_time = -1)

class processor() : 
  #프로세서 기본 속성
  processor_name = 'P1'
  processor_type = 'E'
  processor_work_val = 1
  power_consumption = 1.0
  starting_power_consumption = 0.1
  
  #프로세서 가변 속성
  on_off_state = 'off'
  sleep_state = 'sleep'
  consumed_power = 0
  in_proc = none

  #프로세스 속성 변경(타입 변경)
  def processor_type_change(self) :
    #E -> P
    if self.processor_type == 'E' :
      self.processor_type = 'P'
      self.processor_work_val = 2
      self.power_consumption = 3.0
      self.starting_power_consumption = 0.5
    #P -> E
    else :
      self.processor_type = 'E'
      self.processor_work_val = 1
      self.power_consumption = 1.0
      self.starting_power_consumption = 0.1

  #프로세서 키고 끄기
  def on_off(self) :
    if self.on_off_state == 'off' :
      self.on_off_state = 'on' 
    else :
      self.on_off_state = 'off' 

  #프로세서가 켜져있는가? - 시작할때 사용한다 설정했느냐.
  def on_check(self) :
    if self.on_off_state == 'off' :
      return False
    else :
      return True

  #프로세스가 프로세서 안에 있는가?
  def in_check(self) : 
    if self.in_proc.proc_name != 'none' :
      return False
    else :
      return True

  #프로세스를 프로세서에 할당
  def put_in(self, ready_Q = queue.Queue()) : 
    in_proc = ready_Q.get()

  #프로세스를 프로세서에서 해제
  def put_out(self, un_done = queue.Queue()) : 
    if un_done.qsize() != 0 :
      self.put_in(un_done)
    else : 
      in_proc = none
      self.sleep_state = 'sleep'

  #프로세서 동작(1초)
  def running(self) :
    if self.sleep_state == 'sleep' :
      self.consumed_power += self.starting_power_consumption
      self.sleep_state = 'awake'
    else :
      pass
    self.in_proc.advence_progress(self.processor_work_val)

  #디바이스 리셋
  def reset_device(self) :
    consumed_power = 0
    in_proc = none


if __name__ == '__main__' :
  processor_1 = processor()
  processor_2 = processor()
  print(processor_1.processor_type)
  print(processor_2.processor_type)

  processor_1.processor_type_change()
  print(processor_1.processor_type)
  print(processor_2.processor_type)

  process.proc_add(name = 'test', arr_time = 0, bst_time = 9)
  process.test.see_in_val()
  process.proc_add(name = 'test2', arr_time = 2, bst_time = 7)
  process.proc_add(name = 'test3', arr_time = 3, bst_time = 9)

  Q = queue.Queue()
  Q.put(process.test)
  Q.put(process.test2)
  Q.put(process.test3)

  proc = test
  proc.see_in_val
  proc = test_2
  proc.see_in_val
