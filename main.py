import sqlite3
from Functions import *
from Algorithms import *
from Generator import generate_data

def initialize_database():
    conn = sqlite3.connect("DaneStartowe.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dane (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numer INTEGER,
            arrival_time INTEGER,
            executing_time INTEGER
        )
    """)
    conn.commit()
    conn.close()

def initialize_results_database():
    conn = sqlite3.connect("DaneFinish.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS wyniki (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numer INTEGER,
            algorytm TEXT,
            waiting_time INTEGER,
            turnaround_time INTEGER
        )
    """)
    conn.commit()
    conn.close()

def initialize_process_details_database():
    conn = sqlite3.connect("Dane.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS procesy (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numer INTEGER,
            pid INTEGER,
            arrival_time INTEGER,
            start_time INTEGER,
            end_time INTEGER,
            waiting_time INTEGER
        )
    """)
    conn.commit()
    conn.close()

def main():
    initialize_database()
    initialize_results_database()
    initialize_process_details_database()

    numer = int(input("Podaj numer danych: "))
    generate_data(numer)

    algorithm = input("Wybierz algorytm (fcfs, sjf, rr): ")
    time_quantum = int(input("Podaj kwantum czasu: ")) if algorithm == "rr" else None

    processes = load_data(numer)
    results = fcfs(processes) if algorithm == "fcfs" else sjf(processes) if algorithm == "sjf" else round_robin(processes, time_quantum)

    save_results(numer, algorithm, results)
    print("Dane zapisane!")

if __name__ == "__main__":
    main()
