# Code Explanation Tool - Simplified Developer Guide

## Project Overview
This tool takes Python code as input and generates natural language explanations of the code's functionality.

## Project Structure
```
CodeExplanationTool/
├── src/
│   ├── __init__.py
│   ├── code_parser.py
│   ├── explanation_generator.py
│   └── main.py
├── tests/
│   ├── test_code_parser.py
│   └── test_explanation_generator.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Setting Up the Development Environment
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## Core Components
1. `code_parser.py`: Handles input code and generates an Abstract Syntax Tree (AST)
2. `explanation_generator.py`: Processes the AST and generates natural language explanations
3. `main.py`: Orchestrates the overall process and handles user interaction

## Running the Tool
Execute `python src/main.py` and follow the prompts to input code and receive explanations.

## Running Tests
Use pytest to run the test suite: `pytest tests/`

## Contributing
Please follow PEP 8 style guidelines for Python code. Submit pull requests for any new features or bug fixes.

## Next Steps
- Implement basic code parsing using Python's `ast` module
- Develop simple explanation templates for common code structures
- Create a basic command-line interface for user interaction
