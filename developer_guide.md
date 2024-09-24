# Developer Guide for Code Explanation Tool

This guide provides information for developers who want to contribute to or extend the Code Explanation Tool.

## Project Structure

```
code_explanation_tool/
│
├── code_explanation/
│   ├── __init__.py
│   ├── main.py
│   ├── code_parser.py
│   ├── ast_analyzer.py
│   ├── explanation_generator.py
│   ├── nlp_processor.py
│   └── feedback_handler.py
│
├── run.py
├── test_script.py
├── requirements.txt
├── README.md
└── developer_guide.md
```

## Module Descriptions

- `main.py`: Integrates all components and provides the main `explain_code` function.
- `code_parser.py`: Handles parsing of Python code into an Abstract Syntax Tree (AST).
- `ast_analyzer.py`: Analyzes the AST to extract relevant code structures.
- `explanation_generator.py`: Generates human-readable explanations from the analyzed structures.
- `nlp_processor.py`: Applies basic NLP techniques to improve the readability of explanations.
- `feedback_handler.py`: Manages the collection and storage of user feedback.

## Development Workflow

1. Fork the repository and clone your fork.
2. Create a new branch for your feature or bug fix.
3. Make your changes, following the coding standards outlined below.
4. Write or update tests as necessary.
5. Run the test script to ensure all tests pass.
6. Commit your changes and push to your fork.
7. Submit a pull request with a clear description of your changes.

## Coding Standards

- Follow PEP 8 style guide for Python code.
- Use type hints for function arguments and return values.
- Write docstrings for all functions, classes, and modules.
- Keep functions small and focused on a single task.
- Use meaningful variable and function names.

## Testing

- Write unit tests for new functions and classes.
- Update existing tests when modifying functionality.
- Ensure all tests pass before submitting a pull request.
- Use the `test_script.py` file to add new test cases for the main functionality.

## Extending the Tool

To add support for new Python constructs:

1. Update the `ASTAnalyzer` class in `ast_analyzer.py` to recognize the new construct.
2. Add a new template for the construct in `explanation_generator.py`.
3. Update the `generate_explanation` function to handle the new construct type.
4. Add test cases to verify the new functionality.

## Web Interface

The web interface is built using Flask. To modify the interface:

1. Update the routes in `run.py` as needed.
2. Create or modify HTML templates in the `templates` directory.
3. Add any necessary static files (CSS, JavaScript) to the `static` directory.

## Feedback and Issues

- Use the GitHub issue tracker to report bugs or suggest enhancements.
- Provide as much detail as possible when reporting issues, including steps to reproduce.

## Code Review Process

- All pull requests will be reviewed by project maintainers.
- Address any comments or requested changes promptly.
- Once approved, your changes will be merged into the main branch.

Thank you for contributing to the Code Explanation Tool!s