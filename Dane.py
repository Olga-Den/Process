import sqlite3
import csv

def export_dane_to_csv(filename="procesy.csv"):
    conn = sqlite3.connect("Dane.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM procesy")

    with open(filename, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow([desc[0] for desc in cursor.description])
        writer.writerows(cursor.fetchall())

    conn.close()
    print(f"Dane zapisano w pliku {filename} (z bazy 'Dane.db')")

export_dane_to_csv()

