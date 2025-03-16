import sqlite3
import csv


def export_to_csv(filename="dane_startowe.csv"):
    conn = sqlite3.connect("DaneStartowe.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dane")

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([desc[0] for desc in cursor.description])
        writer.writerows(cursor.fetchall())

    conn.close()
    print(f"Dane zapisano w pliku {filename}")


export_to_csv()
