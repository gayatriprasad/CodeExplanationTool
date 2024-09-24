"""
Main script for the Code Explanation Tool.
This script integrates various components of the tool to provide code explanations.
"""
from code_explanation.code_parser import parse_code
from code_explanation.ast_analyzer import analyze_ast
from code_explanation.explanation_generator import generate_explanation
from code_explanation.nlp_processor import process_text
from code_explanation.feedback_handler import FeedbackHandler

# Initialize the feedback handler
feedback_handler = FeedbackHandler('../data/feedback.json')

def explain_code(code: str) -> str:
    """
    Generate an explanation for the given Python code.
    
    Args:
        code (str): The Python code to explain.
    
    Returns:
        str: The generated explanation or an error message.
    """
    try:
        # Parse the code into an Abstract Syntax Tree (AST)
        ast_tree = parse_code(code)
        
        # Analyze the AST to extract relevant information
        analysis = analyze_ast(ast_tree)
        if analysis is None:
            return "Error: AST analysis failed to produce a result."
        
        # Generate a raw explanation based on the analysis
        raw_explanation = generate_explanation(analysis)
        
        # Process the raw explanation to improve readability
        processed_explanation = process_text(raw_explanation)
        
        return processed_explanation
    except ValueError as e:
        return f"Error: {str(e)}"
    except TypeError as e:
        return f"Error: Unexpected data type in analysis. Details: {str(e)}"

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
    # Example usage
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
    # save_feedback(sample_code, explanation, 5, "Great explanation!")