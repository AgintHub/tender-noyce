from pydantic import BaseModel, Field
from typing import List


class GetZipCodeOutput(BaseModel):
    """Pydantic model for get_zip_code node outputs."""
    zip_code: str = (
        Field(..., description="The ZIP code entered by the user for which the weather forecast will be predicted")
    )


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


def get_historical_weather_data(get_zip_code_input: GetZipCodeOutput, **kwargs) -> GetHistoricalWeatherDataOutput:
    """
    Fetches historical weather data for a ZIP code and returns structured lists
    of dates, temperatures, and precipitation.

    Parameters
    ----------
    zip_code : str
        The ZIP code for which historical weather data is to be retrieved.
        Must be a 5‑digit numeric string.

    Returns
    -------
    Dict[str, Any]
        A dictionary containing the following keys: - `historical_dates`
        (List[str]) – dates in YYYY‑MM‑DD format - `historical_temperatures`
        (List[float]) – daily average temperatures in Celsius -
        `historical_precipitation` (List[float]) – daily precipitation
        amounts in millimeters - `is_valid` (bool) – flag indicating whether
        the data passed basic validation checks

    Raises
    ------
    ValueError
        Raised if `zip_code` is not a valid 5‑digit string or if the data
        source reports the ZIP code as unknown.
    ConnectionError
        Raised when the external weather API is unreachable or times out.
    RuntimeError
        Raised if the retrieved dataset is empty or malformed.

    Examples
    --------
    >>> data = get_historical_weather_data('90210')
    '{'historical_dates': ['2026-01-01', '2026-01-02'],
    'historical_temperatures': [12.5, 13.0], 'historical_precipitation': [0.0,
    5.2], 'is_valid': True}'

    >>> data = get_historical_weather_data('99999')
    ValueError: ZIP code '99999' is invalid or not found in the data source.

    """
    return GetHistoricalWeatherDataOutput(
        historical_dates=[],
        historical_temperatures=[],
        historical_precipitation=[],
        is_valid=False,
    )