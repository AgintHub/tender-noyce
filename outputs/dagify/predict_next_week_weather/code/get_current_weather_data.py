from pydantic import BaseModel, Field


class GetZipCodeOutput(BaseModel):
    """Pydantic model for get_zip_code node outputs."""
    zip_code: str = (
        Field(..., description="The ZIP code entered by the user for which the weather forecast will be predicted")
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


def get_current_weather_data(get_zip_code_input: GetZipCodeOutput, **kwargs) -> GetCurrentWeatherDataOutput:
    """
    Retrieves current weather data for a specified ZIP code from a reliable
    external weather API.

    Parameters
    ----------
    zip_code : str
        A 5‑digit U.S. ZIP code for which to obtain the weather data.

    Returns
    -------
    dict
        Dictionary containing current temperature, humidity, wind speed,
        precipitation, condition description, observation timestamp, and a
        validation flag.

    Raises
    ------
    ValueError
        Raised if the supplied `zip_code` is empty or not a valid 5‑digit
        string.
    RuntimeError
        Raised when the external API request fails or returns invalid data.

    Examples
    --------
    >>> weather = get_current_weather_data('10001')
    >>> print(weather['temperature_celsius'])
    >>> print(weather['is_valid'])
    4.7
    True

    >>> try:
    ...     get_current_weather_data('ABCDE')
    >>> except ValueError as e:
    ...     print(e)
    "zip_code must be a 5‑digit string"

    """
    return GetCurrentWeatherDataOutput(
        temperature_celsius=0.0,
        humidity_percent=0.0,
        wind_speed_kmh=0.0,
        precipitation_mm=0.0,
        condition_description="",
        observation_time="",
        is_valid=False,
    )