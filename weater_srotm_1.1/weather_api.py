# weather_api.py
import requests

def get_coordinates(city):
    try:
        url = f"https://geocode.maps.co/search?q={city}&countrycodes=ru"
        response = requests.get(url)
        data = response.json()

        if not data:
            print("[ERROR] Город не найден.")
            return None, None

        latitude = float(data[0]["lat"])
        longitude = float(data[0]["lon"])
        print(f"[DEBUG] Coordinates for {city}: {latitude}, {longitude}")
        return latitude, longitude
    except Exception as e:
        print("[ERROR] Не удалось получить координаты:", e)
        return None, None

def get_weather(latitude, longitude):
    try:
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True,
            "timezone": "auto"  # <-- уточняем временную зону
        }
        response = requests.get(url, params=params)
        data = response.json()
        temperature = data["current_weather"]["temperature"]
        weather_code = data["current_weather"]["weathercode"]
        return temperature, weather_code
    except Exception as e:
        print("[ERROR] Не удалось получить погоду:", e)
        return None, None
