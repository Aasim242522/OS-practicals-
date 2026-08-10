def fcfs(processes, arrival_time, burst_time):
    n = len(processes)
    # Sort processes by arrival time
    data = sorted(zip(processes, arrival_time, burst_time), key=lambda x: x[1])
    
    t = 0
    wt = [0] * n
    tat = [0] * n
    
    for i in range(n):
        p, at, bt = data[i]
        if t < at:
            t = at
        t += bt
        tat_val = t - at
        wt_val = tat_val - bt
        
        wt[i] = wt_val
        tat[i] = tat_val

    print("--- FCFS Scheduling ---")
    for i in range(n):
        print(f"Process {data[i][0]} -> TAT: {tat[i]}, WT: {wt[i]}")
    print(f"Average Turnaround Time: {sum(tat) / n:.2f}")
    print(f"Average Waiting Time: {sum(wt) / n:.2f}")

# Data from document: P1(AT=0, BT=5), P2(AT=4, BT=2), P3(AT=5, BT=4)
fcfs(["P1", "P2", "P3"], [0, 4, 5], [5, 2, 4])
