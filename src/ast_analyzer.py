"""
This module generates explanations for Python code structures.

It provides templates for common code constructs and a function to generate
explanations based on an analysis of the code structure.
"""

from typing import List, Dict, Any

# Templates for different code constructs
TEMPLATES = {
    'function': "This code defines a function named '{name}' that takes {arg_count} argument(s): {args}.",
    'class': "This code defines a class named '{name}'.",
    'import': "This code imports the module or object '{name}'.",
    'variable': "This code declares a variable named '{name}'.",
    'for_loop': "This code starts a for loop.",
    'while_loop': "This code starts a while loop.",
    'if_statement': "This code starts an if statement for conditional execution."
}


def generate_explanation(analysis: List[Dict[str, Any]], indent: int = 0) -> str:
    """
    Generate a human-readable explanation of code structure based on analysis.

    This function recursively processes the analyzed code structures and generates
    explanations using predefined templates. It handles nested structures by
    increasing the indentation level for each nested block.

    Args:
        analysis (List[Dict[str, Any]]): A list of dictionaries containing
                                         analyzed code structures.
        indent (int): The current indentation level (default is 0).

    Returns:
        str: A string containing the generated explanation.

    Example:
        analysis = [
            {
                'type': 'function',
                'name': 'example_function',
                'args': ['arg1', 'arg2'],
                'body': [
                    {'type': 'variable', 'name': 'x'},
                    {'type': 'for_loop', 'body': [...]}
                ]
            }
        ]
        explanation = generate_explanation(analysis)
        print(explanation)
    """
    explanations = []
    indent_str = "  " * indent

    for item in analysis:
        explanation = ""
        if item['type'] in TEMPLATES:
            # Generate explanation based on the template
            if item['type'] == 'function':
                explanation = TEMPLATES['function'].format(
                    name=item['name'],
                    arg_count=len(item['args']),
                    args=', '.join(item['args'])
                )
            elif item['type'] in ['class', 'import', 'variable']:
                explanation = TEMPLATES[item['type']].format(name=item['name'])
            else:
                explanation = TEMPLATES[item['type']]

            explanations.append(f"{indent_str}{explanation}")

            # Handle nested structures
            if 'body' in item and item['body']:
                structure_type = 'function' if item['type'] == 'function' else \
                                 'class' if item['type'] == 'class' else \
                                 'loop' if item['type'] in ['for_loop', 'while_loop'] else \
                                 'if statement'
                explanations.append(f"{indent_str}Inside this {structure_type}:")
                explanations.append(generate_explanation(item['body'], indent + 1))

    return '\n'.join(explanations)
