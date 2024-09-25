import ast
from code_explanation.ast_analyzer import analyze_ast

def test_analyze_ast():
    code = """
def greet(name):
    print(f"Hello, {name}!")

class Person:
    def __init__(self, name):
        self.name = name

import math

x = 10
if x > 5:
    for i in range(x):
        print(i)
    """
    
    tree = ast.parse(code)
    analysis = analyze_ast(tree)
    
    assert len(analysis['functions']) == 2  # greet and __init__
    assert len(analysis['classes']) == 1    # Person
    assert len(analysis['imports']) == 1    # math
    assert len(analysis['variables']) == 2  # x and i
    assert len(analysis['loops']) == 1      # for loop
    assert len(analysis['conditionals']) == 1  # if statement

    assert analysis['functions'][0]['name'] == 'greet'
    assert analysis['classes'][0]['name'] == 'Person'
    assert analysis['imports'][0]['name'] == 'math'
    assert analysis['variables'][0]['name'] == 'x'