import requests

def fetch():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        joke_data = response.json()
        print(joke_data['value'])
    else:
        print("Failed to fetch joke.")

fetch()

def fetch_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        print(f"Weather in {city_name}: {description}")
        print(f"Temperature: {temperature} °C")
    else:
        print("Failed to fetch weather data. Please check the city name or API key.")

city = input("Enter the name of a municipality: ")
api_key = "7164e17f06a896b7fcf81403f69be9d7"
fetch_weather(city, api_key)