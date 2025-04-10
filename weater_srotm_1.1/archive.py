import csv

def get_weather_by_date(city, date):
    try:
        with open('archive.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == city and row[1] == date:
                    return row[2]  # Погода по дате
    except FileNotFoundError:
        print("Файл с архивом не найден.")
    return None
