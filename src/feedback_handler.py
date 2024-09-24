import json
from datetime import datetime
from typing import List, Dict, Any


class FeedbackHandler:
    """
    A class to handle saving and retrieving user feedback for code explanations.

    This class provides methods to save feedback to a file and retrieve all
    feedback entries from the file.
    """

    def __init__(self, feedback_file: str):
        """
        Initialize the FeedbackHandler with a specified feedback file.

        Args:
            feedback_file (str): The path to the file where feedback will be stored.
        """
        self.feedback_file = feedback_file

    def save_feedback(self, code: str, explanation: str, rating: int, comment: str) -> None:
        """
        Save a feedback entry to the feedback file.

        Args:
            code (str): The original code snippet.
            explanation (str): The generated explanation for the code.
            rating (int): User rating for the explanation (expected to be an integer).
            comment (str): Additional user comment.

        Raises:
            ValueError: If the rating is not an integer.
            IOError: If there's an issue writing to the feedback file.
        """
        if not isinstance(rating, int):
            raise ValueError("Rating must be an integer.")

        feedback = {
            'timestamp': datetime.now().isoformat(),
            'code': code,
            'explanation': explanation,
            'rating': rating,
            'comment': comment
        }

        try:
            with open(self.feedback_file, 'a') as f:
                json.dump(feedback, f)
                f.write('\n')
        except IOError as e:
            raise IOError(f"Error writing to feedback file: {e}")

    def get_all_feedback(self) -> List[Dict[str, Any]]:
        """
        Retrieve all feedback entries from the feedback file.

        Returns:
            list: A list of dictionaries, each containing a feedback entry.

        Raises:
            IOError: If there's an issue reading from the feedback file.
            json.JSONDecodeError: If there's an issue parsing the JSON data.
        """
        feedback_list = []
        try:
            with open(self.feedback_file, 'r') as f:
                for line in f:
                    feedback_list.append(json.loads(line.strip()))
        except IOError as e:
            raise IOError(f"Error reading from feedback file: {e}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Error parsing feedback data: {e}")
        return feedback_list
