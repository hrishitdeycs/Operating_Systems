processes = [
    {"pid": 1, "arrival": 0, "burst": 6, "remaining": 6},
    {"pid": 2, "arrival": 1, "burst": 8, "remaining": 8},
    {"pid": 3, "arrival": 2, "burst": 7, "remaining": 7},
    {"pid": 4, "arrival": 3, "burst": 3, "remaining": 3},
]
current_time = 0
completed = []
turnaround_times = []
waiting_times = []
print("{:<5} {:<7} {:<5} {:<7} {:<11} {:<10} {:<7}".format(
    "PID", "Arrival", "Burst", "Start", "Completion", "Turnaround", "Waiting"
))
start_times = {}  # Track first start times
while len(completed) < len(processes):
    # Select processes that have arrived and are not completed
    available = [p for p in processes if p["arrival"] <= current_time and p["pid"] not in completed]
    if not available:
        current_time += 1
        continue
    # Choose process with shortest remaining time
    next_proc = min(available, key=lambda x: x["remaining"])
    # Record start time if first time execution
    if next_proc["pid"] not in start_times:
        start_times[next_proc["pid"]] = current_time
    # Execute for 1 time unit
    next_proc["remaining"] -= 1
    current_time += 1
    # If process finished
    if next_proc["remaining"] == 0:
        completion = current_time
        turnaround = completion - next_proc["arrival"]
        waiting = turnaround - next_proc["burst"]
        turnaround_times.append(turnaround)
        waiting_times.append(waiting)
        completed.append(next_proc["pid"])
        print("{:<5} {:<7} {:<5} {:<7} {:<11} {:<10} {:<7}".format(
            next_proc["pid"], next_proc["arrival"], next_proc["burst"],
            start_times[next_proc["pid"]], completion, turnaround, waiting
        ))
avg_tat = sum(turnaround_times) / len(processes)
avg_wt = sum(waiting_times) / len(processes)
print("\nAverage Turnaround Time:", avg_tat)
print("Average Waiting Time   :", avg_wt)
