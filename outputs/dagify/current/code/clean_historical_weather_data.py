from pydantic import BaseModel, Field
from typing import List


class GetHistoricalWeatherDataOutput(BaseModel):
    """Pydantic model for get_historical_weather_data node outputs."""
    historical_dates: List[str] = (
        Field(..., description="List of dates (YYYY-MM-DD) for which historical weather data is retrieved")
    )
    historical_temperatures: List[float] = (
        Field(..., description="List of daily average temperatures (in degrees Celsius) corresponding to the dates")
    )
    historical_precipitation: List[float] = (
        Field(..., description="List of daily precipitation amounts (in millimeters) corresponding to the dates")
    )
    is_valid: bool = (
        Field(..., description="Whether the retrieved historical data set passed basic integrity checks")
    )


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


def clean_historical_weather_data(get_historical_weather_data_input: GetHistoricalWeatherDataOutput, **kwargs) -> CleanHistoricalWeatherDataOutput:
    """
    Clean and preprocess historical weather data by removing missing values,
    normalizing numeric fields, and calculating derived metrics.

    Parameters
    ----------
    historical_dates : List[str]
        List of dates (YYYY-MM-DD) for which historical weather data is
        retrieved.
    historical_temperatures : List[float]
        List of daily average temperatures (in degrees Celsius)
        corresponding to the dates.
    historical_precipitation : List[float]
        List of daily precipitation amounts (in millimeters) corresponding
        to the dates.
    historical_humidity : List[float]
        List of daily average relative humidity percentages (0–100)
        corresponding to the dates.
    historical_wind_speed : List[float]
        List of daily average wind speeds (in km/h) corresponding to the
        dates.
    is_valid : bool
        Flag indicating whether the retrieved data set passed basic
        integrity checks.

    Returns
    -------
    Dict[str, Union[int, bool, List[float]]]
        Dictionary containing cleaned record counts, number of missing
        values removed, normalized temperature, humidity, precipitation, and
        wind speed arrays, and a success flag.

    Raises
    ------
    ValueError
        Raised if `is_valid` is False or if any input lists have mismatched
        lengths.

    Examples
    --------
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

    >>> clean_historical_weather_data(

    ...     historical_dates=['2025-12-01'],

    ...     historical_temperatures=[None],

    ...     historical_precipitation=[None],

    ...     historical_humidity=[None],

    ...     historical_wind_speed=[None],

    ...     is_valid=False

    >>> )
    ValueError: Retrieved historical data failed basic integrity checks.

    """
    return CleanHistoricalWeatherDataOutput(
        cleaned_record_count=0,
        missing_value_removed=0,
        temperature_values=[],
        humidity_values=[],
        precipitation_values=[],
        wind_speed_values=[],
        is_cleaned=False,
    )