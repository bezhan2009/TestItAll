import unittest
from typing import Any
from src.errors.add_function_errors.FuncName import Error as FuncNameError
from src.errors.add_function_errors.FuncArgs import Error as FuncArgsError
from src.vars.functions.func_vars import func_vars
from src.utils.add_function import add_function


class TestAddFunction(unittest.TestCase):
    def setUp(self):
        self.addCleanup(self.cleanup_func_vars)

    def cleanup_func_vars(self):
        func_vars.clear()

    def test_add_valid_function(self):
        result = add_function("my_function", [1, 2.0, "three", True, None])
        self.assertTrue(result)
        self.assertEqual(func_vars["my_function"], [1, 2.0, "three", True, None])

    def test_add_function_with_empty_name(self):
        with self.assertRaises(FuncNameError):
            add_function("", [1, 2])

    def test_add_function_with_invalid_name(self):
        with self.assertRaises(FuncNameError):
            add_function("my function", [1, 2])

    def test_add_function_with_non_string_name(self):
        with self.assertRaises(FuncNameError):
            add_function(123, [1, 2])

    def test_add_function_with_non_list_args(self):
        with self.assertRaises(FuncArgsError):
            add_function("my_function", 123)

    def test_add_function_with_invalid_arg_type(self):
        with self.assertRaises(FuncArgsError):
            add_function("my_function", [1, 2, {}])


if __name__ == '__main__':
    unittest.main()
