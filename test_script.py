from code_explanation.main import explain_code
from code_explanation.feedback_handler import FeedbackHandler

def test_code_explanation():
    # Test case 1: Simple function
    code1 = """
def greet(name):
    return f"Hello, {name}!"

result = greet("World")
print(result)
"""
    print("Test Case 1:")
    print(code1)
    print("\nExplanation:")
    print(explain_code(code1))
    print("\n" + "-"*50 + "\n")

    # Test case 2: Class with method
    code2 = """
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
result = calc.add(5, 3)
print(result)
"""
    print("Test Case 2:")
    print(code2)
    print("\nExplanation:")
    print(explain_code(code2))
    print("\n" + "-"*50 + "\n")

    # Test case 3: Loop and conditional
    code3 = """
for i in range(5):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
"""
    print("Test Case 3:")
    print(code3)
    print("\nExplanation:")
    print(explain_code(code3))

def test_feedback_handler():
    feedback_handler = FeedbackHandler('test_feedback.json')
    feedback_handler.save_feedback(
        code="def greet(): print('Hello')",
        explanation="This code defines a function that prints 'Hello'",
        rating=5,
        comment="Clear explanation"
    )
    print("Feedback saved successfully. Check test_feedback.json")

if __name__ == "__main__":
    print("Testing Code Explanation:")
    test_code_explanation()
    print("\nTesting Feedback Handler:")
    test_feedback_handler()