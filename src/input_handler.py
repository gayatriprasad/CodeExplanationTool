import ast
from typing import Optional

def validate_python_code(code: str) -> bool:
    """
    Validate if the given string is syntactically correct Python code.

    Args:
        code (str): The Python code to validate.

    Returns:
        bool: True if the code is valid, False otherwise.
    """
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False

def preprocess_code(code: str) -> str:
    """
    Preprocess the input code by removing leading/trailing whitespace
    and normalizing line endings.

    Args:
        code (str): The input Python code.

    Returns:
        str: The preprocessed code.
    """
    return code.strip().replace('\r\n', '\n')

def parse_code(code: str) -> Optional[ast.AST]:
    """
    Parse the given Python code into an Abstract Syntax Tree (AST).

    Args:
        code (str): The Python code to parse.

    Returns:
        Optional[ast.AST]: The AST of the parsed code, or None if parsing fails.

    Raises:
        ValueError: If the input code is not valid Python.
    """
    preprocessed_code = preprocess_code(code)
    if not validate_python_code(preprocessed_code):
        raise ValueError("Invalid Python code")
    return ast.parse(preprocessed_code)
