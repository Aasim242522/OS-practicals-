def sjf_non_preemptive(processes):
    n = len(processes)
    completed = [False] * n
    current_time = 0
    completed_count = 0
    
    wt = [0] * n
    tat = [0] * n
    ct = [0] * n
    gantt_chart = []
    
    while completed_count < n:
        # Find all processes that have arrived and are not completed
        available = []
        for i in range(n):
            pid, at, bt = processes[i]
            if at <= current_time and not completed[i]:
                available.append((bt, at, pid, i))
                
        if available:
            # Sort by Burst Time (primary), then Arrival Time (secondary)
            available.sort(key=lambda x: (x[0], x[1]))
            bt, at, pid, idx = available[0]
            
            start_time = current_time
            current_time += bt
            completion_time = current_time
            
            ct[idx] = completion_time
            tat[idx] = ct[idx] - processes[idx][1]
            wt[idx] = tat[idx] - processes[idx][2]
            
            completed[idx] = True
            completed_count += 1
            gantt_chart.append((pid, start_time, completion_time))
        else:
            # If no process has arrived, CPU remains idle
            current_time += 1

    # Calculate averages
    avg_wt = sum(wt) / n
    avg_tat = sum(tat) / n
    
    # Print results
    print("\n--- Non-Preemptive SJF Scheduling Results ---")
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

# Dataset for Question 5
# Format: (Process_ID, Arrival_Time, Burst_Time)
processes_q5 = [
    ("P1", 0, 7),
    ("P2", 2, 4),
    ("P3", 4, 1),
    ("P4", 5, 4)
]

sjf_non_preemptive(processes_q5)
