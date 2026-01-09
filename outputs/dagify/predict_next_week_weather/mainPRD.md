# predict_next_week_weather - Complete PRD Documentation

## Overview
PRDs for nodes in the 'predict_next_week_weather' module.

## Table of Contents

- [clean_historical_weather_data](#clean_historical_weather_data)

- [format_weather_prediction](#format_weather_prediction)

- [get_current_weather_data](#get_current_weather_data)

- [get_historical_weather_data](#get_historical_weather_data)

- [get_zip_code](#get_zip_code)

- [predict_next_week_weather](#predict_next_week_weather)

- [prepare_forecast_features](#prepare_forecast_features)

- [train_weather_model](#train_weather_model)



---

## clean_historical_weather_data

### Description
Retrieve historical weather data from a reliable source and transform it into a consistent, missing‑value‑free, and normalized dataset suitable for downstream machine learning training and forecasting.

### Conceptual Info

This node takes raw historical weather data and returns a cleaned, normalized, and statistically ready dataset that can be consumed by the forecasting pipeline.

### Docstring

**Summary:** Clean and preprocess historical weather data by removing missing values, normalizing numeric fields, and calculating derived metrics.

**Parameters:**

- historical_dates (List[str]): List of dates (YYYY-MM-DD) for which historical weather data is retrieved.
- historical_temperatures (List[float]): List of daily average temperatures (in degrees Celsius) corresponding to the dates.
- historical_precipitation (List[float]): List of daily precipitation amounts (in millimeters) corresponding to the dates.
- historical_humidity (List[float]): List of daily average relative humidity percentages (0–100) corresponding to the dates.
- historical_wind_speed (List[float]): List of daily average wind speeds (in km/h) corresponding to the dates.
- is_valid (bool): Flag indicating whether the retrieved data set passed basic integrity checks.
**Returns:** Dict[str, Union[int, bool, List[float]]] - Dictionary containing cleaned record counts, number of missing values removed, normalized temperature, humidity, precipitation, and wind speed arrays, and a success flag.

**Raises:**

- ValueError: Raised if `is_valid` is False or if any input lists have mismatched lengths.
**Examples:**

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



---

## format_weather_prediction

### Description
Takes the raw forecast from the weather model and transforms it into a structured, presentation‑ready format, adding derived high/low temperatures, estimated precipitation amounts, and concise summary sentences for each day.

### Conceptual Info

Transforms a machine‑learning forecast into a user‑friendly report.

### Docstring

**Summary:** Format raw weather predictions into a structured report with derived metrics and summaries.

**Parameters:**

- week_start_date (str): ISO date string of the first day of the forecast week.
- daily_temperatures (List[float]): Predicted average temperature (°C) for each day of the week.
- daily_precipitation (List[float]): Predicted precipitation probability (0–100%) for each day.
- daily_weather_descriptions (List[str]): Human‑readable weather description for each day (e.g., 'Sunny').
**Returns:** Dict[str, List[Union[str, float]]] - Dictionary containing dates, high/low temps, precipitation chance, estimated amount, and daily summary sentences.

**Raises:**

- ValueError: If the three input lists have different lengths.
- TypeError: If any input is not of the expected type.
**Examples:**

```python
>>> week_start_date = '2026-01-09',
>>> daily_temperatures = [5.0, 6.0, 7.0, 4.5, 8.0, 6.5, 7.5],
>>> daily_precipitation = [10.0, 20.0, 0.0, 50.0, 5.0, 30.0, 15.0],
>>> daily_weather_descriptions = ['Sunny', 'Cloudy', 'Clear', 'Rainy', 'Sunny', 'Rainy', 'Cloudy'],
>>> output = format_weather_prediction(
...     week_start_date,
...     daily_temperatures,
...     daily_precipitation,
...     daily_weather_descriptions
>>> )
{
  'date': ['2026-01-09', '2026-01-10', '2026-01-11', '2026-01-12', '2026-01-13', '2026-01-14', '2026-01-15'],
  'high_temp': [10.0, 11.0, 12.0, 9.5, 13.0, 11.5, 12.5],
  'low_temp': [0.0, 1.0, 2.0, -0.5, 3.0, 1.5, 2.5],
  'precipitation_chance': [10.0, 20.0, 0.0, 50.0, 5.0, 30.0, 15.0],
  'precipitation_amount': [1.0, 2.0, 0.0, 5.0, 0.5, 3.0, 1.5],
  'summary': [
    'Sunny with a high of 10.0°C and a low of 0.0°C. Precipitation chance 10%.',
    'Cloudy with a high of 11.0°C and a low of 1.0°C. Precipitation chance 20%.',
    'Clear day, high 12.0°C, low 2.0°C. No precipitation expected.',
    'Rainy forecast; high 9.5°C, low -0.5°C. 50% chance of rain.',
    'Sunny again, high 13.0°C, low 3.0°C. Light chance of precipitation (5%).',
    'Rainy conditions, high 11.5°C, low 1.5°C. 30% chance of rain.',
    'Cloudy with high 12.5°C, low 2.5°C. 15% chance of precipitation.'
  ]
}
```



---

## get_current_weather_data

### Description
Retrieve current weather data for the given zip code

### Conceptual Info

Collects real‑time weather observations for a user‑specified ZIP code, normalizes the data, and validates the response before passing it to downstream forecasting steps.

### Docstring

**Summary:** Retrieves current weather data for a specified ZIP code from a reliable external weather API.

**Parameters:**

- zip_code (str): A 5‑digit U.S. ZIP code for which to obtain the weather data.
**Returns:** dict - Dictionary containing current temperature, humidity, wind speed, precipitation, condition description, observation timestamp, and a validation flag.

**Raises:**

- ValueError: Raised if the supplied `zip_code` is empty or not a valid 5‑digit string.
- RuntimeError: Raised when the external API request fails or returns invalid data.
**Examples:**

```python
>>> weather = get_current_weather_data('10001')
>>> print(weather['temperature_celsius'])
>>> print(weather['is_valid'])
4.7
True
```

```python
>>> try:
...     get_current_weather_data('ABCDE')
>>> except ValueError as e:
...     print(e)
"zip_code must be a 5‑digit string"
```



---

## get_historical_weather_data

### Description
Retrieve historical weather data for the given zip code

### Conceptual Info

This node acts as the gateway to historical meteorological data for a user‑specified ZIP code. It queries an external weather archive API, performs minimal sanity checks, and returns structured lists that downstream cleaning and feature‑engineering nodes can consume.

### Docstring

**Summary:** Fetches historical weather data for a ZIP code and returns structured lists of dates, temperatures, and precipitation.

**Parameters:**

- zip_code (str): The ZIP code for which historical weather data is to be retrieved. Must be a 5‑digit numeric string.
**Returns:** Dict[str, Any] - A dictionary containing the following keys:
- `historical_dates` (List[str]) – dates in YYYY‑MM‑DD format
- `historical_temperatures` (List[float]) – daily average temperatures in Celsius
- `historical_precipitation` (List[float]) – daily precipitation amounts in millimeters
- `is_valid` (bool) – flag indicating whether the data passed basic validation checks

**Raises:**

- ValueError: Raised if `zip_code` is not a valid 5‑digit string or if the data source reports the ZIP code as unknown.
- ConnectionError: Raised when the external weather API is unreachable or times out.
- RuntimeError: Raised if the retrieved dataset is empty or malformed.
**Examples:**

```python
>>> data = get_historical_weather_data('90210')
'{'historical_dates': ['2026-01-01', '2026-01-02'], 'historical_temperatures': [12.5, 13.0], 'historical_precipitation': [0.0, 5.2], 'is_valid': True}'
```

```python
>>> data = get_historical_weather_data('99999')
ValueError: ZIP code '99999' is invalid or not found in the data source.
```



---

## get_zip_code

### Description
Get the zip code for which the weather needs to be predicted

### Conceptual Info

Collects a valid US ZIP code from the user to be used in subsequent weather data retrieval and prediction steps.

### Docstring

**Summary:** Prompt the user for a ZIP code and validate the input.

**Returns:** str - A 5‑digit US ZIP code string that will be passed to downstream weather data nodes.

**Raises:**

- ValueError: If the user input is not a 5‑digit numeric string or is otherwise invalid.
**Examples:**

```python
>>> def mock_input(prompt: str) -> str:
...     return '90210'
>>> zip_code = get_zip_code()
'90210'
```

```python
>>> def mock_input(prompt: str) -> str:
...     return 'ABC12'
>>> try:
...     zip_code = get_zip_code()
>>> except ValueError as e:
...     print(e)
"Invalid ZIP code: must be a 5-digit numeric string"
```



---

## predict_next_week_weather

### Description
Use the trained machine learning model to forecast weather conditions for the upcoming week for a specific ZIP code.

### Conceptual Info

This node loads the previously trained weather prediction model and applies it to the cleaned historical and current weather data, producing a week‑ahead forecast for a user‑specified ZIP code.

### Docstring

**Summary:** Predict the next week’s weather using a trained machine learning model.

**Parameters:**

- zip_code (str): The 5‑digit ZIP code for which the forecast should be generated.
- model_identifier (str): Filename or unique ID of the trained weather prediction model returned by `train_weather_model`.
**Returns:** dict - Dictionary containing the week start date, daily temperatures, daily precipitation probabilities, and daily weather descriptions.

**Raises:**

- FileNotFoundError: If the model file identified by `model_identifier` cannot be located.
- ValueError: If the provided `zip_code` is not a 5‑digit string or the model fails to produce predictions.
- RuntimeError: If the prediction process encounters unexpected data issues.
**Examples:**

```python
>>> forecast = predict_next_week_weather(zip_code='02115', model_identifier='model_2026_01.pickle')
>>> print(forecast['week_start_date'])
"2026-01-16"
```

```python
>>> forecast = predict_next_week_weather(zip_code='02115', model_identifier='model_2026_01.pickle')
>>> print(forecast['daily_temperatures'])
>>> print(forecast['daily_precipitation'])
>>> print(forecast['daily_weather_descriptions'])
[12.5, 13.0, 11.8, 10.2, 14.1, 13.9, 12.0]
[15.0, 20.5, 5.0, 0.0, 30.0, 25.0, 10.0]
['Sunny', 'Partly Cloudy', 'Rain', 'Clear', 'Rainy', 'Cloudy', 'Sunny']
```



---

## prepare_forecast_features

### Description
Collect and compute summary statistics from cleaned historical weather data and current weather observations to create a feature set for the forecasting model.

### Conceptual Info

Prepares a concise, machine‑ready feature vector from both historical and real‑time weather data, suitable for model training or inference.

### Docstring

**Summary:** Generate summary statistics from cleaned historical weather data and current observations to produce a feature dictionary for forecasting.

**Parameters:**

- cleaned_data (dict): Dictionary returned by `clean_historical_weather_data`. Must contain the keys `temperature_values`, `humidity_values`, `precipitation_values`, `wind_speed_values`, and `is_cleaned`.
- current_data (dict): Dictionary returned by `get_current_weather_data`. Must contain the keys `temperature_celsius`, `humidity_percent`, `wind_speed_kmh`, `precipitation_mm`, and `is_valid`.
**Returns:** dict - A dictionary with keys:
- `historical_avg_temperature`, `historical_std_temperature`, `historical_total_precipitation`,
- `historical_avg_humidity`, `historical_avg_wind_speed`,
- `current_temperature`, `current_humidity`, `current_precipitation`, `current_wind_speed`.

**Raises:**

- ValueError: If any required field is missing or if `cleaned_data['is_cleaned']` or `current_data['is_valid']` is False.
**Examples:**

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



---

## train_weather_model

### Description
Train a machine learning model to predict the weather

### Conceptual Info

This node ingests statistical summaries of historical and current weather data, trains a predictive machine‑learning model, and returns a reference to the persisted model along with training status and validation performance.

### Docstring

**Summary:** Trains a machine‑learning model for next‑week weather prediction.

**Parameters:**

- historical_avg_temperature (float): Average temperature over the historical period (°C).
- historical_std_temperature (float): Standard deviation of temperature over the historical period (°C).
- historical_total_precipitation (float): Total precipitation over the historical period (mm).
- historical_avg_humidity (float): Average humidity over the historical period (%).
- historical_avg_wind_speed (float): Average wind speed over the historical period (km/h).
- current_temperature (float): Current temperature reading (°C).
- current_humidity (float): Current humidity reading (%).
- current_precipitation (float): Current precipitation reading (mm).
- current_wind_speed (float): Current wind speed reading (km/h).
**Returns:** dict[str, Any] - A dictionary containing the trained model identifier, a boolean flag indicating training success, and a float validation accuracy.

**Raises:**

- ValueError: Raised if any input feature is missing or out of expected bounds.
- RuntimeError: Raised if the training algorithm fails to converge.
- IOError: Raised if the model cannot be serialized to disk.
**Examples:**

```python
>>> model_info = train_weather_model(
...     historical_avg_temperature=20.5,
...     historical_std_temperature=5.2,
...     historical_total_precipitation=120.0,
...     historical_avg_humidity=60.0,
...     historical_avg_wind_speed=15.0,
...     current_temperature=22.0,
...     current_humidity=55.0,
...     current_precipitation=0.0,
...     current_wind_speed=10.0
>>> )
{'model_identifier': 'weather_model_v1.pkl', 'training_success': True, 'validation_accuracy': 0.87}
```

```python
>>> # Using an intentionally bad input to trigger an error
>>> train_weather_model(
...     historical_avg_temperature=None,
...     historical_std_temperature=5.2,
...     historical_total_precipitation=120.0,
...     historical_avg_humidity=60.0,
...     historical_avg_wind_speed=15.0,
...     current_temperature=22.0,
...     current_humidity=55.0,
...     current_precipitation=0.0,
...     current_wind_speed=10.0
>>> )
ValueError: historical_avg_temperature must be a float and cannot be None
```

