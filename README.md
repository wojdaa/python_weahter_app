# python_weather_app

A Python weather application that fetches weather data from OpenWeatherMap API.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - Linux/Mac: `source .venv/bin/activate`

3. Install dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

4. Create a `.env` file with your OpenWeatherMap API key:
   ```
   OWM_API_KEY=your_api_key_here
   ```

## Usage

Run the weather app:
```bash
python -m weather_app.main -c "City Name"
```

## Development

### Code Formatting with Black

Format all code:
```bash
black src/ tests/
```

Check formatting without making changes:
```bash
black --check src/ tests/
```

### Running Tests

```bash
pytest
```
