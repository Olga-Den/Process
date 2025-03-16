import sqlite3
from Algorithms import fcfs, sjf, round_robin

def load_data(numer: int):
    conn = sqlite3.connect("DaneStartowe.db")
    cursor = conn.cursor()
    cursor.execute("SELECT arrival_time, executing_time FROM dane WHERE numer = ?", (numer,))
    data = cursor.fetchall()
    conn.close()
    return [(i, at, et) for i, (at, et) in enumerate(data)]

def save_results(numer: int, algorithm: str, results: list):
    conn = sqlite3.connect("DaneFinish.db")
    cursor = conn.cursor()

    total_waiting_time = sum(p[1] for p in results)
    total_turnaround_time = sum(p[2] for p in results)
    avg_waiting_time = total_waiting_time / len(results)
    avg_turnaround_time = total_turnaround_time / len(results)

    cursor.execute("""
        INSERT INTO wyniki (numer, algorytm, waiting_time, turnaround_time)
        VALUES (?, ?, ?, ?)
    """, (numer, algorithm, avg_waiting_time, avg_turnaround_time))

    conn.commit()
    conn.close()

    save_process_details(numer, results)

def save_process_details(numer: int, results: list):
    conn = sqlite3.connect("Dane.db")
    cursor = conn.cursor()

    for process in results:
        pid = process[0]
        arrival_time = process[1]
        start_time = arrival_time + process[1]
        end_time = start_time + process[2]
        waiting_time = process[1]

        cursor.execute("""
            INSERT INTO procesy (numer, pid, arrival_time, start_time, end_time, waiting_time)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (numer, pid, arrival_time, start_time, end_time, waiting_time))

    conn.commit()
    conn.close()

