# get_current_weather_data PRD

## Description
Retrieve current weather data for the given zip code


## Conceptual Info

Collects real‑time weather observations for a user‑specified ZIP code, normalizes the data, and validates the response before passing it to downstream forecasting steps.

## Docstring

### Summary
Retrieves current weather data for a specified ZIP code from a reliable external weather API.

### Parameters

- **zip_code** (str): A 5‑digit U.S. ZIP code for which to obtain the weather data.

### Returns

dict: Dictionary containing current temperature, humidity, wind speed, precipitation, condition description, observation timestamp, and a validation flag.

### Raises

- ValueError: Raised if the supplied `zip_code` is empty or not a valid 5‑digit string.
- RuntimeError: Raised when the external API request fails or returns invalid data.

### Examples

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
