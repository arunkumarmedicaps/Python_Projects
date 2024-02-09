import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
    }

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    if response.status_code == 200:
        temperature = weather_data['main']['temp'] -273 #to convert KELVIN to deg c
        description = weather_data['weather'][0]['description']
        print(f"Current temperature in {city}: {temperature}°C, {description}")
    else:
        print(f"Failed to get weather data. Error: {weather_data['message']}")

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = 'b783e1c647eb08286d126b2eaa700439'
    city = input("Enter the city name: ")
    
    get_weather(api_key, city)
