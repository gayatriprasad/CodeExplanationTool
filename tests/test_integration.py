import pytest
from code_explanation.main import explain_code
from code_explanation.ml_model import CodeExplanationModel
from code_explanation.feedback_handler import FeedbackHandler


def test_ml_model_integration():
    model = CodeExplanationModel()
    X = ["def greet():\n    print('Hello')", "x = 5\nprint(x)"]
    y = ["This code defines a function", "This code assigns a value and prints it"]
    model.train(X, y)
    
    prediction = model.predict(["def say_bye():\n    print('Goodbye')"])
    assert "function" in prediction[0]

def test_feedback_handler_integration(tmp_path):
    feedback_file = tmp_path / "feedback.json"
    handler = FeedbackHandler(str(feedback_file))
    
    handler.save_feedback("print('Hello')", "This code prints 'Hello'", 5, "Great explanation!")
    feedback = handler.get_all_feedback()
    
    assert len(feedback) == 1
    assert feedback[0]['code'] == "print('Hello')"
    assert feedback[0]['rating'] == 5