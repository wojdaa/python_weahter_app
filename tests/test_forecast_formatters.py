from weather_app.formatters import format_forecast_data

def test_format_forecast_data_happy_path():
    fake_forecast_json = {
        "city": {"name": "Warsaw", "country": "PL"},
        "list": [
            {"dt_txt": "2024-06-01 12:00:00", "main": {"temp_min": 15, "temp_max": 25, "feels_like": 20}, "weather": [{"description": "clear sky"}]},
            {"dt_txt": "2024-06-01 15:00:00", "main": {"temp_min": 14, "temp_max": 24, "feels_like": 19}, "weather": [{"description": "clear sky"}]},
            {"dt_txt": "2024-06-02 12:00:00", "main": {"temp_min": 16, "temp_max": 26, "feels_like": 21}, "weather": [{"description": "light rain"}]},
            {"dt_txt": "2024-06-02 15:00:00", "main": {"temp_min": 15, "temp_max": 25, "feels_like": 20}, "weather": [{"description": "light rain"}]},
        ]
    }

    result = format_forecast_data(fake_forecast_json, days=2)

    assert "Forecast for Warsaw, PL" in result
    assert "2024-06-01" in result
    assert "2024-06-02" in result
    assert "feels like 20°C" in result
    assert "clear sky" in result