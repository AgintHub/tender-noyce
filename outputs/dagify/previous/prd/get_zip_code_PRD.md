# get_zip_code PRD

## Description
Get the zip code for which the weather needs to be predicted


## Conceptual Info

Collects a valid US ZIP code from the user to be used in subsequent weather data retrieval and prediction steps.

## Docstring

### Summary
Prompt the user for a ZIP code and validate the input.

### Returns

str: A 5‑digit US ZIP code string that will be passed to downstream weather data nodes.

### Raises

- ValueError: If the user input is not a 5‑digit numeric string or is otherwise invalid.

### Examples

```python
>>> def mock_input(prompt: str) -> str:
...     return '90210'
>>> zip_code = get_zip_code()
'90210'
```

```python
>>> def mock_input(prompt: str) -> str:
...     return 'ABC12'
>>> try:
...     zip_code = get_zip_code()
>>> except ValueError as e:
...     print(e)
"Invalid ZIP code: must be a 5-digit numeric string"
```
