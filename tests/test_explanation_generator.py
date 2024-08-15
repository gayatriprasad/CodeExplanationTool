from src.explanation_generator import generate_explanation

def test_generate_explanation():
    analysis = {
        'functions': [{'name': 'greet', 'args': ['name'], 'lineno': 1}],
        'classes': [{'name': 'Person', 'lineno': 4}],
        'imports': [{'name': 'math', 'lineno': 8}],
        'variables': [{'name': 'x', 'lineno': 10}],
        'loops': [{'type': 'for', 'lineno': 12}],
        'conditionals': [{'type': 'if', 'lineno': 11}]
    }
    
    explanation = generate_explanation(analysis)
    
    assert "function named 'greet'" in explanation
    assert "class named 'Person'" in explanation
    assert "imports the module or object 'math'" in explanation
    assert "variable named 'x'" in explanation
    assert "starts a for loop" in explanation
    assert "starts an if statement" in explanation