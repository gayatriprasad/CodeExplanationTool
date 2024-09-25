from .code_parser import parse_code
from .ast_analyzer import analyze_ast
from .explanation_generator import generate_explanation
from .nlp_processor import process_text
from .feedback_handler import FeedbackHandler
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize the feedback handler
feedback_handler = FeedbackHandler('../data/feedback.json')

def explain_code(code: str) -> str:
    """
    Generate an explanation for the given Python code.
    """
    try:
        logger.debug("Parsing code")
        ast_tree = parse_code(code)
        
        logger.debug("Analyzing AST")
        analysis = analyze_ast(ast_tree)
        if analysis is None:
            logger.error("AST analysis failed to produce a result")
            return "Error: AST analysis failed to produce a result."
        
        logger.debug("Generating explanation")
        raw_explanation = generate_explanation(analysis)
        
        logger.debug("Processing explanation")
        processed_explanation = process_text(raw_explanation)
        
        return processed_explanation
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return f"Error: {str(e)}"

def save_feedback(code: str, explanation: str, rating: int, comment: str) -> None:
    """
    Save user feedback for a given code explanation.
    """
    try:
        feedback_handler.save_feedback(code, explanation, rating, comment)
        logger.debug("Feedback saved successfully")
    except Exception as e:
        logger.error(f"An error occurred while saving feedback: {str(e)}", exc_info=True)
        raise