# clean_historical_weather_data PRD

## Description
Retrieve historical weather data from a reliable source and transform it into a consistent, missing‑value‑free, and normalized dataset suitable for downstream machine learning training and forecasting.


## Conceptual Info

This node takes raw historical weather data and returns a cleaned, normalized, and statistically ready dataset that can be consumed by the forecasting pipeline.

## Docstring

### Summary
Clean and preprocess historical weather data by removing missing values, normalizing numeric fields, and calculating derived metrics.

### Parameters

- **historical_dates** (List[str]): List of dates (YYYY-MM-DD) for which historical weather data is retrieved.
- **historical_temperatures** (List[float]): List of daily average temperatures (in degrees Celsius) corresponding to the dates.
- **historical_precipitation** (List[float]): List of daily precipitation amounts (in millimeters) corresponding to the dates.
- **historical_humidity** (List[float]): List of daily average relative humidity percentages (0–100) corresponding to the dates.
- **historical_wind_speed** (List[float]): List of daily average wind speeds (in km/h) corresponding to the dates.
- **is_valid** (bool): Flag indicating whether the retrieved data set passed basic integrity checks.

### Returns

Dict[str, Union[int, bool, List[float]]]: Dictionary containing cleaned record counts, number of missing values removed, normalized temperature, humidity, precipitation, and wind speed arrays, and a success flag.

### Raises

- ValueError: Raised if `is_valid` is False or if any input lists have mismatched lengths.

### Examples

```python
>>> clean_historical_weather_data(

...     historical_dates=['2025-12-01', '2025-12-02', '2025-12-03'],

...     historical_temperatures=[-2.5, None, 0.0],

...     historical_precipitation=[5.0, 0.0, None],

...     historical_humidity=[80.0, 75.0, 78.0],

...     historical_wind_speed=[15.0, 10.0, 12.0],

...     is_valid=True

>>> )
{
  'cleaned_record_count': 2,
  'missing_value_removed': 2,
  'temperature_values': [-2.5, 0.0],
  'humidity_values': [80.0, 75.0, 78.0],
  'precipitation_values': [5.0, 0.0],
  'wind_speed_values': [15.0, 10.0, 12.0],
  'is_cleaned': True
}
```

```python
>>> clean_historical_weather_data(

...     historical_dates=['2025-12-01'],

...     historical_temperatures=[None],

...     historical_precipitation=[None],

...     historical_humidity=[None],

...     historical_wind_speed=[None],

...     is_valid=False

>>> )
ValueError: Retrieved historical data failed basic integrity checks.
```
