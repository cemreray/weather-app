import requests

def get_coordinates(city_name):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name" : city_name,
        "count" : 1,
        "language" : "tr",
        "format" : "json"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    if "results" not in data:
        return None
    
    city = data["results"][0]

    return {
        "name" : city["name"],
        "country" : city.get("country", ""),
        "latitude" : city["latitude"],
        "longitude" : city["longitude"]
    }

def get_weather (latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude" : latitude,
        "longitude" : longitude,
        "current_weather" : True
    }

    response = requests.get(url , params=params)
    response.raise_for_status()

    data = response.json()

    return data["current_weather"]

def get_forecast(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_max,temperature_2m_min,weather_code",
        "forecast_days": 5,
        "timezone": "auto"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    return data["daily"]