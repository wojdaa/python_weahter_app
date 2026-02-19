from unittest.mock import patch, Mock
import pytest

from weather_app.owm_client import get_weather_data


def make_response(status_code: int, json_data: dict | None = None):
    resp = Mock()
    resp.status_code = status_code
    resp.json.return_value = json_data or {}
    return resp


@patch("weather_app.owm_client.requests.get")
def test_get_weather_data_200(mock_get):
    mock_get.return_value = make_response(
        200, {"main": {"temp": 20}, "weather": [{"description": "clear sky"}]}
    )

    data = get_weather_data("Warsaw", "fake_api_key")
    assert isinstance(data, dict)
    assert data["main"]["temp"] == 20


@patch("weather_app.owm_client.requests.get")
def test_get_weather_data_401(mock_get):
    mock_get.return_value = make_response(401, {"message": "Invalid API key"})

    with pytest.raises(RuntimeError):
        get_weather_data("Warsaw", "invalid_api_key")


@patch("weather_app.owm_client.requests.get")
def test_get_weather_data_404(mock_get):
    mock_get.return_value = make_response(404, {"message": "City not found"})

    with pytest.raises(ValueError):
        get_weather_data("NonExistentCity", "fake_api_key")
