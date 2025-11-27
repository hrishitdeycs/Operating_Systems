processes = [
    {"pid": 1, "arrival": 0, "burst": 10, "priority": 3},
    {"pid": 2, "arrival": 1, "burst": 1, "priority": 1},
    {"pid": 3, "arrival": 2, "burst": 2, "priority": 4},
    {"pid": 4, "arrival": 3, "burst": 1, "priority": 2},
]

current_time = 0
completed = []
turnaround_times = []
waiting_times = []

print("{:<5} {:<7} {:<5} {:<8} {:<6} {:<11} {:<10} {:<7}".format(
    "PID", "Arrival", "Burst", "Priority", "Start", "Completion", "Turnaround", "Waiting"))

while len(completed) < len(processes):

    # Select processes that have arrived but are not completed
    available = [p for p in processes if p["arrival"] <= current_time and p["pid"] not in completed]

    # If no process has arrived yet, increase time
    if not available:
        current_time += 1
        continue

    # Pick highest priority (lower number)
    next_proc = min(available, key=lambda x: x["priority"])

    # Start time for this process
    start_time = current_time

    # CPU executes process fully (non-preemptive)
    current_time += next_proc["burst"]

    # Completion, TAT, WT calculations
    completion_time = current_time
    turnaround = completion_time - next_proc["arrival"]
    waiting = turnaround - next_proc["burst"]

    turnaround_times.append(turnaround)
    waiting_times.append(waiting)
    completed.append(next_proc["pid"])

    print("{:<5} {:<7} {:<5} {:<8} {:<6} {:<11} {:<10} {:<7}".format(
        next_proc["pid"], next_proc["arrival"], next_proc["burst"],
        next_proc["priority"], start_time, completion_time, turnaround, waiting
    ))

# Averages
avg_tat = sum(turnaround_times) / len(processes)
avg_wt = sum(waiting_times) / len(processes)

print("\nAverage Turnaround Time:", avg_tat)
print("Average Waiting Time   :", avg_wt)
