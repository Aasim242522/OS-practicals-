def fcfs_scheduling(processes):
    # Sort processes based on Arrival Time
    processes.sort(key=lambda x: x[1])
    
    n = len(processes)
    wt = [0] * n
    tat = [0] * n
    ct = [0] * n
    
    current_time = 0
    gantt_chart = []
    
    for i in range(n):
        pid, at, bt = processes[i]
        
        # If CPU is idle till process arrives
        if current_time < at:
            current_time = at
            
        start_time = current_time
        current_time += bt
        completion_time = current_time
        
        ct[i] = completion_time
        tat[i] = ct[i] - at
        wt[i] = tat[i] - bt
        
        gantt_chart.append((pid, start_time, completion_time))
        
    # Calculate averages
    avg_wt = sum(wt) / n
    avg_tat = sum(tat) / n
    
    # Print results
    print("--- FCFS Scheduling Results ---")
    print("Process\tArrival\tBurst\tWaiting\tTurnaround")
    for i in range(n):
        pid, at, bt = processes[i]
        print(f"{pid}\t{at}\t{bt}\t{wt[i]}\t{tat[i]}")
        
    print(f"\nAverage Waiting Time = {avg_wt:.2f} ms")
    print(f"Average Turnaround Time = {avg_tat:.2f} ms")
    
    # Print Gantt Chart
    print("\nGantt Chart:")
    print(" | ".join([f"{p[0]}" for p in gantt_chart]))
    timeline = [gantt_chart[0][1]] + [p[2] for p in gantt_chart]
    print(" ".join([f"{t:<6}" for t in timeline]))

# Dataset for Question 4
# Format: (Process_ID, Arrival_Time, Burst_Time)
processes_q4 = [
    ("P1", 0, 5),
    ("P2", 1, 3),
    ("P3", 2, 8),
    ("P4", 3, 6)
]

fcfs_scheduling(processes_q4)

