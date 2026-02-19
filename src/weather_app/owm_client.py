import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
BASE_FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


def get_weather_data(city, api_key):
    response = requests.get(
        BASE_URL, 
        params={"q": city, "appid": api_key, "units": "metric"}, 
        timeout=10
    )
    if response.status_code == 401:
        raise RuntimeError("Invalid API key!")
    elif response.status_code == 404:
        raise ValueError("City not found!")
    elif response.status_code != 200:
        raise RuntimeError(f"Error: {response.status_code}")
    return response.json()


def get_forecast_data(city, api_key):
    response = requests.get(
        BASE_FORECAST_URL,
        params={"q": city, "appid": api_key, "units": "metric"},
        timeout=10,
    )
    if response.status_code == 401:
        raise RuntimeError("Invalid API key!")
    elif response.status_code == 404:
        raise ValueError("City not found!")
    elif response.status_code != 200:
        raise RuntimeError(f"Error: {response.status_code}")
    return response.json()
