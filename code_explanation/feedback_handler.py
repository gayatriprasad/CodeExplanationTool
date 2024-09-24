"""
This module handles user feedback for the Code Explanation Tool.
"""
import json
from typing import Dict, Any

class FeedbackHandler:
    def __init__(self, feedback_file: str):
        """
        Initialize the FeedbackHandler.
        
        Args:
            feedback_file (str): Path to the JSON file where feedback will be stored.
        """
        self.feedback_file = feedback_file

    def save_feedback(self, code: str, explanation: str, rating: int, comment: str) -> None:
        """
        Save user feedback for a given code explanation.
        
        Args:
            code (str): The original code that was explained.
            explanation (str): The generated explanation.
            rating (int): User rating for the explanation.
            comment (str): User's comment on the explanation.
        """
        feedback = {
            'code': code,
            'explanation': explanation,
            'rating': rating,
            'comment': comment
        }
        self._append_feedback(feedback)

    def _append_feedback(self, feedback: Dict[str, Any]) -> None:
        """
        Append the feedback to the JSON file.
        
        Args:
            feedback (Dict[str, Any]): The feedback data to append.
        """
        try:
            with open(self.feedback_file, 'r+') as f:
                data = json.load(f)
                data.append(feedback)
                f.seek(0)
                json.dump(data, f, indent=2)
        except FileNotFoundError:
            with open(self.feedback_file, 'w') as f:
                json.dump([feedback], f, indent=2)