from weather import get_coordinates, get_weather


def main():
    city_name = input("Please enter the city whose weather you would like to check:")

    city = get_coordinates(city_name)

    if city is None:
        print ("City not found. Please try again.")
        return
    
    weather = get_weather(city["latitude"], city["longitude"])

    print()
    print(f"Weather for {city['name']}, {city['country']}")
    print("-" * 40)
    print(f"Temperature:{weather['temperature']}°C")
    print(f"Wind speed: {weather['windspeed']}km/h")
    print(f"Wind direction: {weather['winddirection']}°")
    print(f"Time: {weather['time']}")


if __name__ == "__main__":
    main()