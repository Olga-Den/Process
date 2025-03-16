import time
import threading

def fcfs(pool: list) -> list:
    time_elapsed = 0
    result = []
    for process in sorted(pool, key=lambda p: p[1]):
        waiting_time = max(0, time_elapsed - process[1])
        turnaround_time = waiting_time + process[2]
        result.append((process[0], waiting_time, turnaround_time))
        time_elapsed += process[2]
    return result

def sjf(pool: list) -> list:
    time_elapsed = 0
    result = []
    ready_queue = []
    pool = sorted(pool, key=lambda p: p[1])
    while pool or ready_queue:
        while pool and pool[0][1] <= time_elapsed:
            ready_queue.append(pool.pop(0))
        if ready_queue:
            ready_queue.sort(key=lambda p: p[2])
            process = ready_queue.pop(0)
            waiting_time = max(0, time_elapsed - process[1])
            turnaround_time = waiting_time + process[2]
            result.append((process[0], waiting_time, turnaround_time))
            time_elapsed += process[2]
        else:
            time_elapsed += 1
    return result

def round_robin(pool: list, time_quantum: int) -> list:
    queue = pool.copy()
    time_elapsed = 0
    result = []
    while queue:
        process = queue.pop(0)
        if process[2] > time_quantum:
            queue.append((process[0], process[1], process[2] - time_quantum))
            time_elapsed += time_quantum
        else:
            waiting_time = max(0, time_elapsed - process[1])
            turnaround_time = waiting_time + process[2]
            result.append((process[0], waiting_time, turnaround_time))
            time_elapsed += process[2]
    return result

