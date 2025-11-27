class Process :
    def __init__(self,process_id,arrival_time,burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.start_time = 0
        self.completion_time =0
        self.waiting_time = 0
        self.turn_around_time = 0 
        

def fcfs(processes):
        processes.sort(key=lambda x:(x.arrival_time))
        current_time = 0
        total_turn_around_time = 0 
        total_waiting_time = 0 
        for process in processes:
            if(process.arrival_time > current_time):
                current_time = process.arrival_time
            process.start_time = current_time
            process.completion_time = process.start_time + process.burst_time
            process.turn_around_time  = process.completion_time - process.arrival_time
            process.waiting_time  = process.turn_around_time - process.burst_time
            total_turn_around_time += process.turn_around_time
            current_time = process.completion_time
               
            total_waiting_time += process.waiting_time
     
        print("Process_Id \t Arrival_time \t Burst_Time \t Start_time \t Completion_time \t Waiting time \t  Turn around time" )


        for process in processes:
            print(f"{process.process_id} \t {process.arrival_time} \t {process.burst_time} \t {process.start_time} \t {process.completion_time} \t{process.waiting_time} \t {process.turn_around_time}")

        print("average waiting time ",total_waiting_time/len(processes))
        print("average turn around time ",total_turn_around_time/len(processes))

    

def main():
    processes = [Process("P1",0,9),
                Process("P2",1,8),
                Process("P3",1,5),
                Process("P4",3,6),
                Process("P5",4,2)
        ]
        
    fcfs(processes)
    


if __name__ == "__main__":
    main()
    
