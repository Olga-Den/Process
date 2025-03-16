class Process:
    def __init__(self, pid: int, arrival_time: int, executing_time: int):
        self.pid = pid
        self.arrival_time = arrival_time
        self.executing_time = executing_time
        self.waiting_time = 0
        self.turnaround_time = 0
