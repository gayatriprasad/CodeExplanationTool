"""
This module handles parsing of Python code into an Abstract Syntax Tree (AST).
"""
import ast
from typing import Optional

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
    # Preprocess the code by removing leading/trailing whitespace and normalizing line endings
    preprocessed_code = code.strip().replace('\r\n', '\n')
    
    try:
        return ast.parse(preprocessed_code)
    except SyntaxError:
        raise ValueError("Invalid Python code")