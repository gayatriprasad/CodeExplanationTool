"""
Code Explanation Tool
---------------------

This package provides tools for explaining Python code structures.
"""

from .main import explain_code, save_feedback
from .code_parser import parse_code
from .ast_analyzer import analyze_ast
from .explanation_generator import generate_explanation
from .nlp_processor import process_text
from .feedback_handler import FeedbackHandler

__all__ = [
    'explain_code',
    'save_feedback',
    'parse_code',
    'analyze_ast',
    'generate_explanation',
    'process_text',
    'FeedbackHandler'
]

__version__ = '0.1.0'