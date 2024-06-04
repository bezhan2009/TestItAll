from typing import Any
from src.errors.add_function_errors import FuncName, FuncArgs
from src.vars.functions.func_vars import func_vars


def add_function(function_name: str, function_args: list[Any]) -> bool:
    """
    Adds a new function to the `func_vars` dictionary.

    Args:
        function_name (str): The name of the function to be added.
        function_args (list[Any]): A list of arguments for the function.

    Returns:
        bool: True if the function was successfully added, False otherwise.

    Raises:
        FuncNameError: If the `function_name` is an empty string or contains invalid characters.
        FuncArgsError: If the `function_args` is not a list or contains invalid values.
    """
    if not function_name or not isinstance(function_name, str) or not function_name.isidentifier():
        raise FuncName.Error("Function name must be a non-empty string with valid identifier characters")

    if not isinstance(function_args, list):
        raise FuncArgs.Error("Function arguments must be a list")

    for arg in function_args:
        if not isinstance(arg, (str, int, float, bool, None.__class__)):
            raise FuncArgs.Error(f"Function argument '{arg}' is of an invalid type")

    func_vars[function_name] = function_args
    return True
