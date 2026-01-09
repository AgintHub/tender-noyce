# get_historical_weather_data PRD

## Description
Retrieve historical weather data for the given zip code


## Conceptual Info

This node acts as the gateway to historical meteorological data for a user‑specified ZIP code. It queries an external weather archive API, performs minimal sanity checks, and returns structured lists that downstream cleaning and feature‑engineering nodes can consume.

## Docstring

### Summary
Fetches historical weather data for a ZIP code and returns structured lists of dates, temperatures, and precipitation.

### Parameters

- **zip_code** (str): The ZIP code for which historical weather data is to be retrieved. Must be a 5‑digit numeric string.

### Returns

Dict[str, Any]: A dictionary containing the following keys:
- `historical_dates` (List[str]) – dates in YYYY‑MM‑DD format
- `historical_temperatures` (List[float]) – daily average temperatures in Celsius
- `historical_precipitation` (List[float]) – daily precipitation amounts in millimeters
- `is_valid` (bool) – flag indicating whether the data passed basic validation checks

### Raises

- ValueError: Raised if `zip_code` is not a valid 5‑digit string or if the data source reports the ZIP code as unknown.
- ConnectionError: Raised when the external weather API is unreachable or times out.
- RuntimeError: Raised if the retrieved dataset is empty or malformed.

### Examples

```python
>>> data = get_historical_weather_data('90210')
'{'historical_dates': ['2026-01-01', '2026-01-02'], 'historical_temperatures': [12.5, 13.0], 'historical_precipitation': [0.0, 5.2], 'is_valid': True}'
```

```python
>>> data = get_historical_weather_data('99999')
ValueError: ZIP code '99999' is invalid or not found in the data source.
```
