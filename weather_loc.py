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


#def get_lat_long(city_name, state_code, country_code, limit, api_key):
def get_lat_long(api_key, city):
    base_url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        'q': f'{city}',
        #'limit': limit,
        'appid': api_key
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        
        if data:
            # Assuming the first result is the desired one
            lat = data[0]['lat']
            long = data[0]['lon']
            print(lat)
            print(long)
            
        else:
            print("No data found for the provided location.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error making the request: {e}")
        return None



if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = 'b783e1c647eb08286d126b2eaa700439'
    city = input("Enter the city name: ")
    
    get_weather(api_key, city)
    print("\n\n")
    get_lat_long(api_key, city)
