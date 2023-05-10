class process() :
  proc_name = 'p1'
  a_time = 0 #arrive time
  b_time = 0 #brust time
  lb_time = 0 #left brust time
  w_time = 0 #wait time
  ta_time = 0 #turnaround_time
  nt_time = 0 #normalized turnaround time
  res_ratio = 0 #Response ratio
  work_val = 0 #얼마나 일했는지.

  #프로세스에 기본 값 넣기.
  def value_input(self, name = 'p1' , arr_time = 0, bst_time = 0) :
    self.a_time = arr_time
    self.b_time = bst_time
    self.lb_time = self.b_time
    self.proc_name = name

  #프로세스를 진행시킬 때 사용.
  def advence_progress(self, processor_work_val) : 
    if (self.work_val + processor_work_val) > self.b_time :
      self.work_val = self.b_time
    else : 
      self.work_val += processor_work_val

    self.lb_time = self.b_time - self.work_val
      
  #프로세스 대기중.
  def waiting_turn(self) :
    self.w_time += 1 

  #진행도 계산.
  def progress_val(self) :
    progress = 0.0
    progress = (self.b_time - self.lb_time) / self.b_time * 100
    return progress

  #프로세스 종료시 사용.
  def job_done(self, undone_list, done_list) : 
    undone_list.remove(self)
    done_list.append(self)
    self.ta_time = self.b_time + self.w_time
    self.nt_time = self.ta_time / self.b_time

  #응답률 계산.
  def res_check(self) :
    if self.lb_time != 0 :
      self.res_ratio = (self.lb_time + self.w_time) / self.lb_time
    else :
      pass

  #테스트용 함수, 안에 든 요소값들을 전부 반환.
  def see_in_val(self) :
    print(f'이름 : {self.proc_name}, AT : {self.a_time}, BT : {self.b_time}, LBT : {self.lb_time}')
    print(f'WT : {self.w_time}, TT : {self.ta_time}, NTT : {self.nt_time}, Res_ratio : {self.res_ratio}')
    print(f'{self.work_val}')

#프로세스를 추가하는 함수, 가변 변수를 프로그램 동작 중 선언할 수 있는 함수.
def proc_add(*, name = 'p1', arr_time = 0, bst_time = 0) :
  name = f'{name}'
  globals()[name] = process()
  globals()[name].value_input(name, arr_time, bst_time)


if __name__ == '__main__' :
  process_list = []
  un_done_list = []
  done_list = []
  test = True
  
  input_nam = input('프로세스 이름을 입력하시오 : ')
  input_arr = int(input('프로세스 도착시간을 입력하시오 : '))
  input_bst = int(input('프로세스 실행시간을 입력하시오 : '))
  proc_add(name = input_nam, arr_time = input_arr, bst_time = input_bst)
  process_list.append(globals()[f'{input_nam}'])
  process_list[0].see_in_val()
  un_done_list.append(process_list[0])

  while process_list[0].lb_time != 0 : 
    if test == True :
      process_list[0].advence_progress(1)
      test = False
    else :
      process_list[0].waiting_turn()
      test = True

    process_list[0].res_check()
    process_list[0].see_in_val()
    print(f'진행도 : {process_list[0].progress_val()}')

    if process_list[0].lb_time == 0 :
      process_list[0].job_done(un_done_list, done_list)
      
  process_list[0].see_in_val()
