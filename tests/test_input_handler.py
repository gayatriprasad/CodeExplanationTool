import pytest
from code_explanation.input_handler import validate_python_code, preprocess_code, parse_code

def test_validate_python_code():
    assert validate_python_code("print('Hello, World!')") == True
    assert validate_python_code("print('Hello, World!'") == False
    assert validate_python_code("for i in range(10):") == False

def test_preprocess_code():
    assert preprocess_code("  print('Hello')  \n") == "print('Hello')"
    assert preprocess_code("print('Hello')\r\nprint('World')") == "print('Hello')\nprint('World')"

def test_parse_code():
    valid_code = "x = 5\nprint(x)"
    assert parse_code(valid_code) is not None

    with pytest.raises(ValueError):
        parse_code("print('Hello'")