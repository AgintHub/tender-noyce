from pydantic import BaseModel, Field
from typing import List


class PredictNextWeekWeatherOutput(BaseModel):
    """Pydantic model for predict_next_week_weather node outputs."""
    week_start_date: str = (
        Field(..., description="ISO date string representing the first day of the forecast week.")
    )
    daily_temperatures: float = (
        Field(..., description="Predicted average temperature for each day of the week.")
    )
    daily_precipitation: float = (
        Field(..., description="Predicted precipitation probability (0\u2011100%) for each day of the week.")
    )
    daily_weather_descriptions: str = (
        Field(..., description="Human\u2011readable weather description for each day (e.g., 'Sunny', 'Rainy').")
    )


class FormatWeatherPredictionOutput(BaseModel):
    """Pydantic model for format_weather_prediction node outputs."""
    date: List[str] = (
        Field(..., description="ISO date string (YYYY-MM-DD) for each forecast day.")
    )
    high_temp: List[float] = (
        Field(..., description="Predicted high temperature for each day (\u00b0C).")
    )
    low_temp: List[float] = (
        Field(..., description="Predicted low temperature for each day (\u00b0C).")
    )
    precipitation_chance: List[float] = (
        Field(..., description="Probability of precipitation (0\u2013100%).")
    )
    precipitation_amount: List[float] = (
        Field(..., description="Estimated precipitation volume in millimeters.")
    )
    summary: List[str] = (
        Field(..., description="Human\u2011readable summary sentence for each day.")
    )


def format_weather_prediction(predict_next_week_weather_input: PredictNextWeekWeatherOutput, **kwargs) -> FormatWeatherPredictionOutput:
    """
    Format raw weather predictions into a structured report with derived metrics
    and summaries.

    Parameters
    ----------
    week_start_date : str
        ISO date string of the first day of the forecast week.
    daily_temperatures : List[float]
        Predicted average temperature (°C) for each day of the week.
    daily_precipitation : List[float]
        Predicted precipitation probability (0–100%) for each day.
    daily_weather_descriptions : List[str]
        Human‑readable weather description for each day (e.g., 'Sunny').

    Returns
    -------
    Dict[str, List[Union[str, float]]]
        Dictionary containing dates, high/low temps, precipitation chance,
        estimated amount, and daily summary sentences.

    Raises
    ------
    ValueError
        If the three input lists have different lengths.
    TypeError
        If any input is not of the expected type.

    Examples
    --------
    >>> week_start_date = '2026-01-09',
    >>> daily_temperatures = [5.0, 6.0, 7.0, 4.5, 8.0, 6.5, 7.5],
    >>> daily_precipitation = [10.0, 20.0, 0.0, 50.0, 5.0, 30.0, 15.0],
    >>> daily_weather_descriptions = ['Sunny', 'Cloudy', 'Clear', 'Rainy',
    'Sunny', 'Rainy', 'Cloudy'],
    >>> output = format_weather_prediction(
    ...     week_start_date,
    ...     daily_temperatures,
    ...     daily_precipitation,
    ...     daily_weather_descriptions
    >>> )
    {
      'date': ['2026-01-09', '2026-01-10', '2026-01-11', '2026-01-12',
    '2026-01-13', '2026-01-14', '2026-01-15'],
      'high_temp': [10.0, 11.0, 12.0, 9.5, 13.0, 11.5, 12.5],
      'low_temp': [0.0, 1.0, 2.0, -0.5, 3.0, 1.5, 2.5],
      'precipitation_chance': [10.0, 20.0, 0.0, 50.0, 5.0, 30.0, 15.0],
      'precipitation_amount': [1.0, 2.0, 0.0, 5.0, 0.5, 3.0, 1.5],
      'summary': [
        'Sunny with a high of 10.0°C and a low of 0.0°C. Precipitation chance
    10%.',
        'Cloudy with a high of 11.0°C and a low of 1.0°C. Precipitation chance
    20%.',
        'Clear day, high 12.0°C, low 2.0°C. No precipitation expected.',
        'Rainy forecast; high 9.5°C, low -0.5°C. 50% chance of rain.',
        'Sunny again, high 13.0°C, low 3.0°C. Light chance of precipitation
    (5%).',
        'Rainy conditions, high 11.5°C, low 1.5°C. 30% chance of rain.',
        'Cloudy with high 12.5°C, low 2.5°C. 15% chance of precipitation.'
      ]
    }

    """
    return FormatWeatherPredictionOutput(
        date=[],
        high_temp=[],
        low_temp=[],
        precipitation_chance=[],
        precipitation_amount=[],
        summary=[],
    )