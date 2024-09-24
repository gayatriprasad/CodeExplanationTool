"""
Main script for the Code Explanation Tool.

This script integrates various components of the tool to provide code explanations.
"""

from src.input_handler import parse_code
from src.ast_analyzer import analyze_ast
from src.explanation_generator import generate_explanation
from src.nlp_processor import process_text
from src.feedback_handler import FeedbackHandler

# Initialize the feedback handler
feedback_handler = FeedbackHandler('data/feedback.json')

def explain_code(code: str) -> str:
    """
    Generate an explanation for the given Python code.

    Args:
        code (str): The Python code to explain.

    Returns:
        str: A detailed explanation of the code.

    Raises:
        ValueError: If there's an error in parsing or analyzing the code.
    """
    try:
        # Parse the code into an Abstract Syntax Tree (AST)
        ast_tree = parse_code(code)
        
        # Analyze the AST to extract relevant information
        analysis = analyze_ast(ast_tree)
        
        # Generate a raw explanation based on the analysis
        raw_explanation = generate_explanation(analysis)
        
        # Process the raw explanation to improve readability
        processed_explanation = process_text(raw_explanation)
        
        return processed_explanation
    except ValueError as e:
        return f"Error: {str(e)}"

def save_feedback(code: str, explanation: str, rating: int, comment: str) -> None:
    """
    Save user feedback for a given code explanation.

    Args:
        code (str): The original code that was explained.
        explanation (str): The generated explanation.
        rating (int): User rating for the explanation.
        comment (str): User's comment on the explanation.
    """
    feedback_handler.save_feedback(code, explanation, rating, comment)

if __name__ == "__main__":
    # Example usage with nested structures
    sample_code = """
def outer_function(x):
    if x > 0:
        def inner_function(y):
            if y % 2 == 0:
                return y * 2
            else:
                return y + 1
        return inner_function(x)
    else:
        return 0

result = outer_function(5)
print(result)
    """
    
    # Generate and print the explanation for the sample code
    explanation = explain_code(sample_code)
    print(explanation)
    
    # Simulate user feedback
    save_feedback(sample_code, explanation, 5, "Great explanation!")
