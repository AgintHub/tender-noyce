from pydantic import BaseModel, Field


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


class TrainWeatherModelOutput(BaseModel):
    """Pydantic model for train_weather_model node outputs."""
    model_identifier: str = (
        Field(..., description="Unique identifier or filename for the trained weather prediction model")
    )
    training_success: bool = (
        Field(..., description="Indicates whether the model training completed successfully")
    )
    validation_accuracy: float = (
        Field(..., description="Validation accuracy (between 0 and 1) of the trained model on the validation set")
    )


def train_weather_model(prepare_forecast_features_input: PrepareForecastFeaturesOutput, **kwargs) -> TrainWeatherModelOutput:
    """
    Trains a machine‑learning model for next‑week weather prediction.

    Parameters
    ----------
    historical_avg_temperature : float
        Average temperature over the historical period (°C).
    historical_std_temperature : float
        Standard deviation of temperature over the historical period (°C).
    historical_total_precipitation : float
        Total precipitation over the historical period (mm).
    historical_avg_humidity : float
        Average humidity over the historical period (%).
    historical_avg_wind_speed : float
        Average wind speed over the historical period (km/h).
    current_temperature : float
        Current temperature reading (°C).
    current_humidity : float
        Current humidity reading (%).
    current_precipitation : float
        Current precipitation reading (mm).
    current_wind_speed : float
        Current wind speed reading (km/h).

    Returns
    -------
    dict[str, Any]
        A dictionary containing the trained model identifier, a boolean flag
        indicating training success, and a float validation accuracy.

    Raises
    ------
    ValueError
        Raised if any input feature is missing or out of expected bounds.
    RuntimeError
        Raised if the training algorithm fails to converge.
    IOError
        Raised if the model cannot be serialized to disk.

    Examples
    --------
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
    {'model_identifier': 'weather_model_v1.pkl', 'training_success': True,
    'validation_accuracy': 0.87}

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

    """
    return TrainWeatherModelOutput(
        model_identifier="",
        training_success=False,
        validation_accuracy=0.0,
    )