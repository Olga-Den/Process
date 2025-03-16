import sqlite3
import csv

def export_danefinish_to_csv(filename="wyniki.csv"):
    conn = sqlite3.connect("DaneFinish.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM wyniki")

    with open(filename, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow([desc[0] for desc in cursor.description])
        writer.writerows(cursor.fetchall())

    conn.close()
    print(f"Dane zapisano w pliku {filename} (z bazy 'DaneFinish.db')")

export_danefinish_to_csv()

