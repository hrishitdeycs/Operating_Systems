class Process :
    def __init__(self,process_id,burst_time):
        self.process_id = process_id
        self.burst_time = burst_time
        self.waiting_time = 0 
        self.turn_around_time = 0 

def shortest_job_first(processes):
    sorted_process = sorted(processes,key=lambda x : x.burst_time)
    total_turn_around_time = 0 
    total_waiting_time = 0 


    for i in range(len(sorted_process)):
        if(i == 0):
            sorted_process[i].waiting_time = 0
        else:
            sorted_process[i].waiting_time = sorted_process[i-1].waiting_time + sorted_process[i-1].burst_time
        sorted_process[i].turn_around_time = sorted_process[i].waiting_time + sorted_process[i].burst_time
        total_turn_around_time += sorted_process[i].turn_around_time
        total_waiting_time += sorted_process[i].waiting_time


    for process in sorted_process:
        print(f"Process_id : {process.process_id} , Burst_time : {process.burst_time}, Waiting_time {process.waiting_time}, Turn_around_time : {process.turn_around_time} ")

        
    print("average waiting time ",total_waiting_time/len(sorted_process))
    print("average turn_around_time ",total_turn_around_time/len(sorted_process))

def main():
        processes = [Process("P1",9),
                Process("P2",4),
                Process("P3",5),
                Process("P4",6),
                Process("P5",2)
        ]

        shortest_job_first(processes)
    
if __name__ == "__main__":
    main()
