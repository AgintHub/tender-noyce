from pydantic import BaseModel, Field


class GetZipCodeOutput(BaseModel):
    """Pydantic model for get_zip_code node outputs."""
    zip_code: str = (
        Field(..., description="The ZIP code entered by the user for which the weather forecast will be predicted")
    )


def get_zip_code(general_input: str, **kwargs) -> GetZipCodeOutput:
    """
    Prompt the user for a ZIP code and validate the input.

    Returns
    -------
    str
        A 5‑digit US ZIP code string that will be passed to downstream
        weather data nodes.

    Raises
    ------
    ValueError
        If the user input is not a 5‑digit numeric string or is otherwise
        invalid.

    Examples
    --------
    >>> def mock_input(prompt: str) -> str:
    ...     return '90210'
    >>> zip_code = get_zip_code()
    '90210'

    >>> def mock_input(prompt: str) -> str:
    ...     return 'ABC12'
    >>> try:
    ...     zip_code = get_zip_code()
    >>> except ValueError as e:
    ...     print(e)
    "Invalid ZIP code: must be a 5-digit numeric string"

    """
    return GetZipCodeOutput(
        zip_code="",
    )