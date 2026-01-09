from pydantic import BaseModel, Field


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


def predict_next_week_weather(train_weather_model_input: TrainWeatherModelOutput, **kwargs) -> PredictNextWeekWeatherOutput:
    """
    Predict the next week’s weather using a trained machine learning model.

    Parameters
    ----------
    zip_code : str
        The 5‑digit ZIP code for which the forecast should be generated.
    model_identifier : str
        Filename or unique ID of the trained weather prediction model
        returned by `train_weather_model`.

    Returns
    -------
    dict
        Dictionary containing the week start date, daily temperatures, daily
        precipitation probabilities, and daily weather descriptions.

    Raises
    ------
    FileNotFoundError
        If the model file identified by `model_identifier` cannot be
        located.
    ValueError
        If the provided `zip_code` is not a 5‑digit string or the model
        fails to produce predictions.
    RuntimeError
        If the prediction process encounters unexpected data issues.

    Examples
    --------
    >>> forecast = predict_next_week_weather(zip_code='02115',
    model_identifier='model_2026_01.pickle')
    >>> print(forecast['week_start_date'])
    "2026-01-16"

    >>> forecast = predict_next_week_weather(zip_code='02115',
    model_identifier='model_2026_01.pickle')
    >>> print(forecast['daily_temperatures'])
    >>> print(forecast['daily_precipitation'])
    >>> print(forecast['daily_weather_descriptions'])
    [12.5, 13.0, 11.8, 10.2, 14.1, 13.9, 12.0]
    [15.0, 20.5, 5.0, 0.0, 30.0, 25.0, 10.0]
    ['Sunny', 'Partly Cloudy', 'Rain', 'Clear', 'Rainy', 'Cloudy', 'Sunny']

    """
    return PredictNextWeekWeatherOutput(
        week_start_date="",
        daily_temperatures=0.0,
        daily_precipitation=0.0,
        daily_weather_descriptions="",
    )