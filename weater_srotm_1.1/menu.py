from weather_api import get_coordinates, get_weather
from data_manager import save_request, read_history
from archive import get_weather_by_date

def show_main_menu():
    while True:
        print("===== МЕНЮ =====")
        print("1. Узнать погоду")
        print("2. Архив по дате")
        print("3. История запросов")
        print("0. Выход")
        choice = input("\nВыберите пункт меню: ")

        if choice == "1":
            city = input("Введите город: ")
            lat, lon = get_coordinates(city)
            if lat is not None and lon is not None:
                temperature, code = get_weather(lat, lon)
                if temperature is not None:
                    print(f"Сейчас в городе {city} {temperature}°C, код погоды: {code}")
                    save_request(city, "now", temperature)
            else:
                print("Не удалось получить координаты города.")

        elif choice == "2":
            # ... остальной код ...
            pass

        elif choice == "3":
            # ... остальной код ...
            pass

        elif choice == "0":
            break

        else:
            print("Неверный ввод. Попробуйте снова.")
