from pydantic import BaseModel, Field
from typing import List


class CleanHistoricalWeatherDataOutput(BaseModel):
    """Pydantic model for clean_historical_weather_data node outputs."""
    cleaned_record_count: int = (
        Field(..., description="Number of records after cleaning")
    )
    missing_value_removed: int = (
        Field(..., description="Number of missing values removed")
    )
    temperature_values: List[float] = (
        Field(..., description="List of temperature values after cleaning")
    )
    humidity_values: List[float] = (
        Field(..., description="List of humidity values after cleaning")
    )
    precipitation_values: List[float] = (
        Field(..., description="List of precipitation values after cleaning")
    )
    wind_speed_values: List[float] = (
        Field(..., description="List of wind speed values after cleaning")
    )
    is_cleaned: bool = (
        Field(..., description="Indicates whether the cleaning process succeeded")
    )


class GetCurrentWeatherDataOutput(BaseModel):
    """Pydantic model for get_current_weather_data node outputs."""
    temperature_celsius: float = (
        Field(..., description="Current air temperature in degrees Celsius")
    )
    humidity_percent: float = (
        Field(..., description="Current relative humidity as a percentage (0\u2013100)")
    )
    wind_speed_kmh: float = (
        Field(..., description="Current wind speed in kilometers per hour")
    )
    precipitation_mm: float = (
        Field(..., description="Current precipitation amount in millimeters")
    )
    condition_description: str = (
        Field(..., description="Human\u2011readable weather condition (e.g., \"Clear\", \"Rain\", \"Snow\")")
    )
    observation_time: str = (
        Field(..., description="Timestamp of the observation in ISO 8601 format (e.g., \"2026-01-09T14:00:00Z\")")
    )
    is_valid: bool = (
        Field(..., description="Flag indicating whether the retrieved data passed validation checks")
    )


class PrepareForecastFeaturesOutput(BaseModel):
    """Pydantic model for prepare_forecast_features node outputs."""
    historical_avg_temperature: float = (
        Field(..., description="Average temperature over the historical period")
    )
    historical_std_temperature: float = (
        Field(..., description="Standard deviation of temperature over the historical period")
    )
    historical_total_precipitation: float = (
        Field(..., description="Total precipitation over the historical period")
    )
    historical_avg_humidity: float = (
        Field(..., description="Average humidity over the historical period")
    )
    historical_avg_wind_speed: float = (
        Field(..., description="Average wind speed over the historical period")
    )
    current_temperature: float = (
        Field(..., description="Current temperature reading")
    )
    current_humidity: float = Field(..., description="Current humidity reading")
    current_precipitation: float = (
        Field(..., description="Current precipitation reading")
    )
    current_wind_speed: float = (
        Field(..., description="Current wind speed reading")
    )


def prepare_forecast_features(clean_historical_weather_data_input: CleanHistoricalWeatherDataOutput, get_current_weather_data_input: GetCurrentWeatherDataOutput, **kwargs) -> PrepareForecastFeaturesOutput:
    """
    Generate summary statistics from cleaned historical weather data and current
    observations to produce a feature dictionary for forecasting.

    Parameters
    ----------
    cleaned_data : dict
        Dictionary returned by `clean_historical_weather_data`. Must contain
        the keys `temperature_values`, `humidity_values`,
        `precipitation_values`, `wind_speed_values`, and `is_cleaned`.
    current_data : dict
        Dictionary returned by `get_current_weather_data`. Must contain the
        keys `temperature_celsius`, `humidity_percent`, `wind_speed_kmh`,
        `precipitation_mm`, and `is_valid`.

    Returns
    -------
    dict
        A dictionary with keys: - `historical_avg_temperature`,
        `historical_std_temperature`, `historical_total_precipitation`, -
        `historical_avg_humidity`, `historical_avg_wind_speed`, -
        `current_temperature`, `current_humidity`, `current_precipitation`,
        `current_wind_speed`.

    Raises
    ------
    ValueError
        If any required field is missing or if `cleaned_data['is_cleaned']`
        or `current_data['is_valid']` is False.

    Examples
    --------
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

    >>> cleaned_data = {'is_cleaned': False}
    >>> current_data = {'is_valid': True}
    >>> prepare_forecast_features(cleaned_data, current_data)
    ValueError: cleaned_data is not cleaned or missing required fields.

    """
    return PrepareForecastFeaturesOutput(
        historical_avg_temperature=0.0,
        historical_std_temperature=0.0,
        historical_total_precipitation=0.0,
        historical_avg_humidity=0.0,
        historical_avg_wind_speed=0.0,
        current_temperature=0.0,
        current_humidity=0.0,
        current_precipitation=0.0,
        current_wind_speed=0.0,
    )