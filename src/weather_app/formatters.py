def format_weather_data(data) -> str:
    wind = data.get("wind", {})
    speed = wind.get("speed", "N/A")
    deg = wind.get("deg")

    if deg is None:
        wind_line = f"Wind: {speed} m/s"
    else:
        wind_line = f"Wind: {speed} m/s at {deg}°"

    lines = [
        f"Weather in {data['name']}, {data['sys']['country']}:",
        f"Temperature: {round(data['main']['temp'])}°C (feels like {round(data['main']['feels_like'])}°C)",
        f"Humidity: {data['main']['humidity']}%",
        f"Description: {data['weather'][0]['description']}",
        wind_line,
    ]
    return "\n".join(lines)


def daily_summary_from_forecast(forecast_json) -> list[dict]:
    items = forecast_json["list"]
    by_date = {}

    for item in items:
        date = item["dt_txt"].split(" ")[0]
        tmin = item["main"]["temp_min"]
        tmax = item["main"]["temp_max"]
        feels_like = item["main"]["feels_like"]
        desc = item["weather"][0]["description"]

        if date not in by_date:
            by_date[date] = {"tmin": tmin, "tmax": tmax, "feels_like": feels_like, "desc": {desc: 1}}
        else:
            by_date[date]["tmin"] = min(by_date[date]["tmin"], tmin)
            by_date[date]["tmax"] = max(by_date[date]["tmax"], tmax)
            by_date[date]["feels_like"] = round((by_date[date]["feels_like"] + feels_like) / 2)
            counts = by_date[date]["desc"]
            counts[desc] = counts.get(desc, 0) + 1

    result = [
        {
            "date": date,
            "tmin": round(info["tmin"]),
            "tmax": round(info["tmax"]),
            "feels_like": info["feels_like"],
            "desc": max(info["desc"], key=info["desc"].get),
        }
        for date, info in by_date.items()
    ]
    result.sort(key=lambda x: x["date"])
    return result

def format_forecast_data(forecast_json, days = 4) -> str:
    city = forecast_json.get("city", {}).get("name", "N/A")
    country = forecast_json.get("city", {}).get("country", "N/A")
    daily = daily_summary_from_forecast(forecast_json)[:days]

    lines = [f"Forecast for {city}, {country} (next {len(daily)} days):"]
    for day in daily:
        lines.append(f"{day['date']}: {day['tmin']}°C - {day['tmax']}°C, feels like {day['feels_like']}°C, {day['desc']}")
    return "\n".join(lines)
