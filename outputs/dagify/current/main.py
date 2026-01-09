import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.clean_historical_weather_data import clean_historical_weather_data
from code.format_weather_prediction import format_weather_prediction
from code.get_current_weather_data import get_current_weather_data
from code.get_historical_weather_data import get_historical_weather_data
from code.get_zip_code import get_zip_code
from code.predict_next_week_weather import predict_next_week_weather
from code.prepare_forecast_features import prepare_forecast_features
from code.train_weather_model import train_weather_model

# Get async mode from environment variable or default to False
ASYNC_MODE = os.environ.get('ASYNC_MODE', '').lower() in ('true', '1', 'yes', 'y')

def make_async(func):
    """Convert a synchronous function to an asynchronous function.

    If the function is already asynchronous, return it unchanged.
    If the function is synchronous, wrap it in an async function.
    """
    # If it's already a coroutine function, return it as is
    if inspect.iscoroutinefunction(func):
        return func

    # Otherwise, wrap it as an async function
    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return async_wrapper

clean_historical_weather_data_async = make_async(clean_historical_weather_data)
format_weather_prediction_async = make_async(format_weather_prediction)
get_current_weather_data_async = make_async(get_current_weather_data)
get_historical_weather_data_async = make_async(get_historical_weather_data)
get_zip_code_async = make_async(get_zip_code)
predict_next_week_weather_async = make_async(predict_next_week_weather)
prepare_forecast_features_async = make_async(prepare_forecast_features)
train_weather_model_async = make_async(train_weather_model)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: get_zip_code
    async def run_get_zip_code():
        # Call the async version of get_zip_code with results from dependencies
        return await get_zip_code_async(user_input)

    # Run level 0 nodes in parallel
    results['get_zip_code'] = await run_get_zip_code()

    # Level 1: get_historical_weather_data, get_current_weather_data
    async def run_get_historical_weather_data():
        # Call the async version of get_historical_weather_data with results from dependencies
        return await get_historical_weather_data_async(results['get_zip_code'])

    async def run_get_current_weather_data():
        # Call the async version of get_current_weather_data with results from dependencies
        return await get_current_weather_data_async(results['get_zip_code'])

    # Run level 1 nodes in parallel
    level_1_results = await asyncio.gather(run_get_historical_weather_data(), run_get_current_weather_data())
    results['get_historical_weather_data'] = level_1_results[0]
    results['get_current_weather_data'] = level_1_results[1]

    # Level 2: clean_historical_weather_data
    async def run_clean_historical_weather_data():
        # Call the async version of clean_historical_weather_data with results from dependencies
        return await clean_historical_weather_data_async(results['get_historical_weather_data'])

    # Run level 2 nodes in parallel
    results['clean_historical_weather_data'] = await run_clean_historical_weather_data()

    # Level 3: prepare_forecast_features
    async def run_prepare_forecast_features():
        # Call the async version of prepare_forecast_features with results from dependencies
        return await prepare_forecast_features_async(results['clean_historical_weather_data'], results['get_current_weather_data'])

    # Run level 3 nodes in parallel
    results['prepare_forecast_features'] = await run_prepare_forecast_features()

    # Level 4: train_weather_model
    async def run_train_weather_model():
        # Call the async version of train_weather_model with results from dependencies
        return await train_weather_model_async(results['prepare_forecast_features'])

    # Run level 4 nodes in parallel
    results['train_weather_model'] = await run_train_weather_model()

    # Level 5: predict_next_week_weather
    async def run_predict_next_week_weather():
        # Call the async version of predict_next_week_weather with results from dependencies
        return await predict_next_week_weather_async(results['train_weather_model'])

    # Run level 5 nodes in parallel
    results['predict_next_week_weather'] = await run_predict_next_week_weather()

    # Level 6: format_weather_prediction
    async def run_format_weather_prediction():
        # Call the async version of format_weather_prediction with results from dependencies
        return await format_weather_prediction_async(results['predict_next_week_weather'])

    # Run level 6 nodes in parallel
    results['format_weather_prediction'] = await run_format_weather_prediction()

    # Return all results
    return results

def run_workflow_sync(user_input: str) -> Dict[str, Any]:
    """Synchronous wrapper around the async workflow execution."""
    return asyncio.run(run_workflow(user_input))

def main():
    """Main entry point.

    Handles arguments in the following priority:
    1. Command-line argument (sys.argv[1])
    2. If no argument, uses empty string as input but displays a warning.
    """
    # Get user input from command line or use empty string
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        # No input provided - display help message but continue with empty string
        print('Warning: No input provided. Using empty string as input.')
        print('For better results, provide an input argument:')
        print(f'  python {os.path.basename(__file__)} "your input text here"')
        print('Or use a file as input:')
        print(f'  python {os.path.basename(__file__)} "$(cat input.txt)"')
        user_input = ""

    print(f'Running workflow with input: {user_input}')

    # Run the workflow
    results = run_workflow_sync(user_input)

    # Print results
    try:
        # Convert results to JSON
        json_results = json.dumps(results, indent=2, default=str)
        print(json_results)
    except (TypeError, ValueError) as e:
        print(f'Results could not be converted to JSON: {e}')
        print(f'Raw results: {results}')

    return results

if __name__ == '__main__':
    main()
