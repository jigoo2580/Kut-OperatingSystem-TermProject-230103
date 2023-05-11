#process_list.sort(key = lambda process: process.b_time, reverse = True)
#return process_list

class process:

    def __init__(self, name, a_time, b_time, w_time):
        self.name = name
        self.a_time = a_time
        self.b_time = b_time
        self.w_time = w_time
        self.res_ratio = (self.w_time + self.b_time) / self.b_time

    def __repr__(self):
        return '{' + self.name + ', ' + str(self.a_time) + ', ' + str(self.b_time) + ', ' + str(self.w_time) + ', ' +str(self.res_ratio) +'}'
#        res_ratio = (process.w_time + process.b_time) / process.w_time

def SPN(process_list):
#    sorted(process_list, key= lambda x: x.b_time)
    return process_list.sort(key = lambda x: x.b_time)
    
def SRTN(process_list):
    return process_list.sort(key = lambda process: process.b_time)

def HRRN(process_list):
    return process_list.sort(key = lambda process: process.res_ratio, reverse = True)

def new_rr(process_list, time_quatum):
    process_list1 = []
    process_list2 = []

    process_list.sort(key = lambda process: process.b_time)

    length = len(process_list)
    
    for i in range(length):
        if process_list[i].b_time < time_quatum:
            process_list1.append(process_list[i])
        else:
            process_list2.append(process_list[i])

    process_list2.sort(key = lambda process: process.b_time, reverse = True)

    process_list = process_list1 + process_list2

    return process_list




if __name__ == '__main__' :

    processes = [
        process('P1', 0, 1, 20),
        process('P2', 1, 5, 1),
        process('P3', 2, 2, 5),
        process('P4', 3, 3, 5),  
    ]
    print(processes)

#    processes.sort(key = lambda x: x.b_time)
#    SPN(processes)
    # HRRN(processes)
    new_rr(processes, 2)
    print(processes)
    print("\n\n")
