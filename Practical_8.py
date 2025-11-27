processes = [
    {"pid": 1, "arrival": 0, "burst": 6},
    {"pid": 2, "arrival": 1, "burst": 8},
    {"pid": 3, "arrival": 2, "burst": 7},
    {"pid": 4, "arrival": 3, "burst": 3},
]

current_time = 0
completed = []
turnaround_times = []
waiting_times = []

print("{:<5} {:<7} {:<5} {:<7} {:<11} {:<10} {:<7}".format(
    "PID", "Arrival", "Burst", "Start", "Completion", "Turnaround", "Waiting"
))

while len(completed) < len(processes):

    # Select processes that have arrived so far
    available = [p for p in processes if p["arrival"] <= current_time and p["pid"] not in completed]

    # CPU idle → move time forward
    if not available:
        current_time += 1
        continue

    # Choose shortest burst process
    next_proc = min(available, key=lambda x: x["burst"])

    # Start executing
    start_time = current_time
    current_time += next_proc["burst"]
    completion = current_time

    # Time calculations
    turnaround = completion - next_proc["arrival"]
    waiting = turnaround - next_proc["burst"]

    turnaround_times.append(turnaround)
    waiting_times.append(waiting)
    completed.append(next_proc["pid"])

    print("{:<5} {:<7} {:<5} {:<7} {:<11} {:<10} {:<7}".format(
        next_proc["pid"], next_proc["arrival"], next_proc["burst"],
        start_time, completion, turnaround, waiting
    ))

# Averages
avg_tat = sum(turnaround_times) / len(processes)
avg_wt = sum(waiting_times) / len(processes)

print("\nAverage Turnaround Time:", avg_tat)
print("Average Waiting Time   :", avg_wt)
