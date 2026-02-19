from weather_app.formatters import format_weather_data


def test_format_weather_data_happy_path():
    fake_data = {
        "name": "Warsaw",
        "sys": {"country": "PL"},
        "main": {"temp": 20, "feels_like": 18, "humidity": 60},
        "weather": [{"description": "clear sky"}],
        "wind": {"speed": 5, "deg": 180},
    }

    result = format_weather_data(fake_data)

    assert "Warsaw" in result
    assert "PL" in result
    assert "20" in result
    assert "clear sky" in result


def test_format_weather_data_missing_wind_deg():
    fake_data = {
        "name": "Warsaw",
        "sys": {"country": "PL"},
        "main": {"temp": 20, "feels_like": 18, "humidity": 60},
        "weather": [{"description": "clear sky"}],
        "wind": {"speed": 5},
    }

    result = format_weather_data(fake_data)

    assert "Wind: " in result
    assert "Wind: 5 m/s" in result
    assert "direction" not in result
    assert "Weather in Warsaw, PL:" in result


def test_format_weather_data_missing_wind():
    fake_data = {
        "name": "Warsaw",
        "sys": {"country": "PL"},
        "main": {"temp": 20, "feels_like": 18, "humidity": 60},
        "weather": [{"description": "clear sky"}],
    }

    result = format_weather_data(fake_data)

    assert "Wind:" in result
    assert "N/A" in result
    assert "Weather in Warsaw, PL:" in result
