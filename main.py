from weather import get_coordinates, get_weather, get_forecast


def main():
    city_name = input("Please enter the city whose weather you would like to check: ")

    city = get_coordinates(city_name)

    if city is None:
        print("City not found. Please try again.")
        return

    weather = get_weather(city["latitude"], city["longitude"])
    weather_code = weather["weathercode"]

    if weather_code == 0:
        weather_emoji = "☀️ Clear"
    elif weather_code <= 3:
        weather_emoji = "☁️ Cloudy"
    elif weather_code <= 67:
        weather_emoji = "🌧️ Rainy"
    else:
        weather_emoji = "🌩️ Severe weather"

    forecast = get_forecast(city["latitude"], city["longitude"])

    print()
    print("*" * 45)
    print("           WEATHER APPLICATION")
    print("*" * 45)

    print(f"Location       : {city['name']}, {city['country']}")
    print(f"Condition      : {weather_emoji}")
    print(f"Temperature    : {weather['temperature']}°C")
    print(f"Wind Speed     : {weather['windspeed']} km/h")
    print(f"Wind Direction : {weather['winddirection']}°")
    print(f"Time           : {weather['time']}")

    print("*" * 45)

    print()
    print("5-Day Forecast")
    print("-" * 45)

    for i in range(5):
        date = forecast["time"][i]
        max_temp = forecast["temperature_2m_max"][i]
        min_temp = forecast["temperature_2m_min"][i]

        print(f"{date} | Max: {max_temp}°C | Min: {min_temp}°C")


if __name__ == "__main__":
    main()