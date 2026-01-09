# prepare_forecast_features PRD

## Description
Collect and compute summary statistics from cleaned historical weather data and current weather observations to create a feature set for the forecasting model.


## Conceptual Info

Prepares a concise, machine‑ready feature vector from both historical and real‑time weather data, suitable for model training or inference.

## Docstring

### Summary
Generate summary statistics from cleaned historical weather data and current observations to produce a feature dictionary for forecasting.

### Parameters

- **cleaned_data** (dict): Dictionary returned by `clean_historical_weather_data`. Must contain the keys `temperature_values`, `humidity_values`, `precipitation_values`, `wind_speed_values`, and `is_cleaned`.
- **current_data** (dict): Dictionary returned by `get_current_weather_data`. Must contain the keys `temperature_celsius`, `humidity_percent`, `wind_speed_kmh`, `precipitation_mm`, and `is_valid`.

### Returns

dict: A dictionary with keys:
- `historical_avg_temperature`, `historical_std_temperature`, `historical_total_precipitation`,
- `historical_avg_humidity`, `historical_avg_wind_speed`,
- `current_temperature`, `current_humidity`, `current_precipitation`, `current_wind_speed`.

### Raises

- ValueError: If any required field is missing or if `cleaned_data['is_cleaned']` or `current_data['is_valid']` is False.

### Examples

```python
>>> cleaned_data = {
...     'cleaned_record_count': 3,
...     'missing_value_removed': 0,
...     'temperature_values': [20.0, 21.5, 19.0],
...     'humidity_values': [60.0, 55.0, 65.0],
...     'precipitation_values': [5.0, 0.0, 2.0],
...     'wind_speed_values': [15.0, 12.0, 18.0],
...     'is_cleaned': True
>>> } 
>>> current_data = {
...     'temperature_celsius': 22.3,
...     'humidity_percent': 58.0,
...     'wind_speed_kmh': 12.0,
...     'precipitation_mm': 0.0,
...     'condition_description': 'Clear',
...     'observation_time': '2026-01-09T14:00:00Z',
...     'is_valid': True
>>> } 
>>> features = prepare_forecast_features(cleaned_data, current_data)
{
  'historical_avg_temperature': 20.166666666666668,
  'historical_std_temperature': 1.540309513061559,
  'historical_total_precipitation': 7.0,
  'historical_avg_humidity': 60.0,
  'historical_avg_wind_speed': 15.0,
  'current_temperature': 22.3,
  'current_humidity': 58.0,
  'current_precipitation': 0.0,
  'current_wind_speed': 12.0
}
```

```python
>>> cleaned_data = {'is_cleaned': False}
>>> current_data = {'is_valid': True}
>>> prepare_forecast_features(cleaned_data, current_data)
ValueError: cleaned_data is not cleaned or missing required fields.
```
