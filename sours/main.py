import csv
import datetime
import requests

def get_weather(city):
    geourl = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=ru&format=json&country=RU"
    geo_response = requests.get(geourl)
    geo_data = geo_response.json()
    if "results" not in geo_data:
        return "Город не найден"
    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()
    w = weather_data["current_weather"]
    return f"{city}: температура {w['temperature']}°C, ветер {w['windspeed']} км/ч"

def main():
    while True:
        print("1. Узнать погоду сейчас")
        print("2. Посмотреть погоду в прошлом")
        print("3. История запросов")
        print("4. Выход")

        a = input("Выберите пункт меню: ")

        if a == "1":
            c = input("Введите город (в России): ")
            w = get_weather(c)
            print("Погода:", w)
            with open("weather.csv", "a", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([datetime.datetime.now(), c, w])
        elif a == "2":
            c = input("Введите город: ")
            d = input("Введите дату в формате ГГГГ-ММ-ДД: ")
            found = False
            with open("weather.csv", "r", encoding="utf-8") as f:
                r = csv.reader(f)
                for row in r:
                    if c in row[1] and d in row[0]:
                        print("Погода в архиве:", row[2])
                        found = True
            if not found:
                print("Нет данных за эту дату.")
        elif a == "3":
            print("Архив запросов:")
            with open("weather.csv", "r", encoding="utf-8") as f:
                r = csv.reader(f)
                for row in r:
                    print("Дата:", row[0], "Город:", row[1], "Погода:", row[2])
        elif a == "4":
            break
        else:
            print("Неверный ввод")

main()
