# modules/weather.py
import requests

def get_weather(city):
    api_key = "your_openweathermap_api_key"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url).json()
    weather = response['weather'][0]['description']
    temperature = response['main']['temp'] - 273.15  # Convert Kelvin to Celsius
    return f"The weather in {city} is {weather} with a temperature of {temperature:.1f} degrees Celsius."