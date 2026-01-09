# format_weather_prediction PRD

## Description
Takes the raw forecast from the weather model and transforms it into a structured, presentation‑ready format, adding derived high/low temperatures, estimated precipitation amounts, and concise summary sentences for each day.


## Conceptual Info

Transforms a machine‑learning forecast into a user‑friendly report.

## Docstring

### Summary
Format raw weather predictions into a structured report with derived metrics and summaries.

### Parameters

- **week_start_date** (str): ISO date string of the first day of the forecast week.
- **daily_temperatures** (List[float]): Predicted average temperature (°C) for each day of the week.
- **daily_precipitation** (List[float]): Predicted precipitation probability (0–100%) for each day.
- **daily_weather_descriptions** (List[str]): Human‑readable weather description for each day (e.g., 'Sunny').

### Returns

Dict[str, List[Union[str, float]]]: Dictionary containing dates, high/low temps, precipitation chance, estimated amount, and daily summary sentences.

### Raises

- ValueError: If the three input lists have different lengths.
- TypeError: If any input is not of the expected type.

### Examples

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
