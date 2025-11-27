# First Come First Serve (FCFS) Scheduling

# Process data
processes = [
    {"pid": 1, "arrival": 0, "burst": 5},
    {"pid": 2, "arrival": 1, "burst": 3},
    {"pid": 3, "arrival": 2, "burst": 8},
    {"pid": 4, "arrival": 3, "burst": 6},
]

# Sort processes by arrival time
processes.sort(key=lambda x: x["arrival"])

current_time = 0
turnaround_times = []
waiting_times = []

# Print table header
print("{:<5} {:<7} {:<5} {:<7} {:<11} {:<10} {:<7}".format(
    "PID", "Arrival", "Burst", "Start", "Completion", "Turnaround", "Waiting"
))

# Calculate CT, TAT, WT
for p in processes:

    # CPU idle → move time to arrival time
    if current_time < p["arrival"]:
        current_time = p["arrival"]

    start_time = current_time
    current_time += p["burst"]   # Completion time
    completion = current_time

    turnaround = completion - p["arrival"]
    waiting = turnaround - p["burst"]

    turnaround_times.append(turnaround)
    waiting_times.append(waiting)

    print("{:<5} {:<7} {:<5} {:<7} {:<11} {:<10} {:<7}".format(
        p["pid"], p["arrival"], p["burst"], start_time,
        completion, turnaround, waiting
    ))

# Averages
avg_tat = sum(turnaround_times) / len(processes)
avg_wt = sum(waiting_times) / len(processes)

print("\nAverage Turnaround Time:", avg_tat)
print("Average Waiting Time   :", avg_wt)
