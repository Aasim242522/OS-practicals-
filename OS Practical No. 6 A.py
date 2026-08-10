def round_robin(processes, arrival_time, burst_time, time_quantum):
    n = len(processes)
    rem_bt = list(burst_time)
    t = 0  # Current time
    wt = [0] * n
    tat = [0] * n
    complete = 0
    
    while complete < n:
        done = True
        for i in range(n):
            if rem_bt[i] > 0:
                done = False
                if rem_bt[i] > time_quantum:
                    t += time_quantum
                    rem_bt[i] -= time_quantum
                else:
                    t += rem_bt[i]
                    wt[i] = t - arrival_time[i] - burst_time[i]
                    rem_bt[i] = 0
                    tat[i] = t - arrival_time[i]
                    complete += 1
        if done:
            break

    print("--- Round Robin Scheduling ---")
    for i in range(n):
        print(f"Process {processes[i]} -> TAT: {tat[i]}, WT: {wt[i]}")
    print(f"Average Turnaround Time: {sum(tat) / n:.2f}")
    print(f"Average Waiting Time: {sum(wt) / n:.2f}\n")

# Data from document: P1(AT=0, BT=5), P2(AT=4, BT=2), P3(AT=5, BT=4) with TQ=2
round_robin(["P1", "P2", "P3"], [0, 4, 5], [5, 2, 4], 2)
