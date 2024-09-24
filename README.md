# Code Explanation Tool

The Code Explanation Tool is a Python-based application that analyzes Python code and generates human-readable explanations of its structure and functionality.

## Features

- Parse Python code into an Abstract Syntax Tree (AST)
- Analyze the AST to extract relevant code structures
- Generate explanations for functions, classes, loops, and other Python constructs
- Process explanations using basic NLP techniques for improved readability
- Collect and store user feedback on explanations

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/code-explanation-tool.git
   cd code-explanation-tool
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To use the Code Explanation Tool without the web interface:

1. Open a Python interactive shell or create a new Python file.
2. Import the `explain_code` function:
   ```python
   from code_explanation import explain_code
   ```
3. Use the function to explain Python code:
   ```python
   code = """
   def greet(name):
       return f"Hello, {name}!"
   
   result = greet("World")
   print(result)
   """
   explanation = explain_code(code)
   print(explanation)
   ```

To run the web interface:

1. Run the Flask application:
   ```
   python run.py
   ```
2. Open a web browser and navigate to `http://localhost:5000`

## Testing

To run the test script:

```
python test_script.py
```

This will run a series of test cases and display the results in the console.

## Contributing

Please read the [Developer Guide](developer_guide.md) for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.