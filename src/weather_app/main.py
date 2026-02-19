from dotenv import load_dotenv
import os
import argparse

from .owm_client import get_weather_data, get_forecast_data
from .formatters import format_weather_data, format_forecast_data

def parse_args():
    parser = argparse.ArgumentParser(description="Get weather data for a city.")
    parser.add_argument("-c", type=str, help="Name of the city")
    parser.add_argument("--forecast", action="store_true", help="Show forecast for next days")
    parser.add_argument("--days", type=int, default=4, help="Number of days to show in forecast (default: 4)")
    return parser.parse_args()


def main():
    load_dotenv()
    api_key = os.getenv("OWM_API_KEY")
    if not api_key:
        print("API key not found!")
        raise SystemExit(1)

    args = parse_args()
    
    city = (args.c or "").strip()
    if not city:
        city = input("Enter city name: ").strip()
    if not city:
        print("City name cannot be empty!")
        raise SystemExit(1)

    try:
        if args.forecast:
            forecast_json = get_forecast_data(city, api_key)
            print(format_forecast_data(forecast_json, days=args.days))
        else:
            weather_data = get_weather_data(city, api_key)
            print(format_weather_data(weather_data))
    except Exception as e:
        print(f"Error: {e}")
        raise SystemExit(1)
    
if __name__ == "__main__":
    main()
