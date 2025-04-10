import csv
from datetime import datetime

FILE_NAME = "archive.csv"


def save_request(city, date, result):
    with open(FILE_NAME, mode="a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().isoformat(), city, date or "текущая погода", result])


def read_history():
    try:
        with open(FILE_NAME, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                print(f"[{row[0]}] {row[1]} — {row[2]}: {row[3]}")
    except FileNotFoundError:
        print("История пуста.")