import sqlite3
from numpy import random

def generate_data(numer: int):
    conn = sqlite3.connect("DaneStartowe.db")
    cursor = conn.cursor()
    for _ in range(50):
        arrival_time = random.randint(0, 50)
        executing_time = random.randint(10, 60)
        cursor.execute("INSERT INTO dane (numer, arrival_time, executing_time) VALUES (?, ?, ?)",
                       (numer, arrival_time, executing_time))
    conn.commit()
    conn.close()
