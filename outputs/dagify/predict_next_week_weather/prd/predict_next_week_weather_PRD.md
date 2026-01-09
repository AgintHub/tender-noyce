# predict_next_week_weather PRD

## Description
Use the trained machine learning model to forecast weather conditions for the upcoming week for a specific ZIP code.


## Conceptual Info

This node loads the previously trained weather prediction model and applies it to the cleaned historical and current weather data, producing a week‑ahead forecast for a user‑specified ZIP code.

## Docstring

### Summary
Predict the next week’s weather using a trained machine learning model.

### Parameters

- **zip_code** (str): The 5‑digit ZIP code for which the forecast should be generated.
- **model_identifier** (str): Filename or unique ID of the trained weather prediction model returned by `train_weather_model`.

### Returns

dict: Dictionary containing the week start date, daily temperatures, daily precipitation probabilities, and daily weather descriptions.

### Raises

- FileNotFoundError: If the model file identified by `model_identifier` cannot be located.
- ValueError: If the provided `zip_code` is not a 5‑digit string or the model fails to produce predictions.
- RuntimeError: If the prediction process encounters unexpected data issues.

### Examples

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
