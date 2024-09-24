import ast
from typing import Dict, Any, List

class ASTAnalyzer(ast.NodeVisitor):
    """
    A class for analyzing Python Abstract Syntax Trees (AST).

    This class visits different nodes in the AST and extracts relevant information
    about functions, classes, imports, variables, loops, and conditional statements.
    """

    def __init__(self):
        self.analysis = []
        self.current_scope = self.analysis

    def visit_FunctionDef(self, node):
        """Visit a function definition node."""
        func_info = {
            'type': 'function',
            'name': node.name,
            'args': [arg.arg for arg in node.args.args],
            'body': [],
            'lineno': node.lineno
        }
        self._process_scope(func_info)

    def visit_ClassDef(self, node):
        """Visit a class definition node."""
        class_info = {
            'type': 'class',
            'name': node.name,
            'body': [],
            'lineno': node.lineno
        }
        self._process_scope(class_info)

    def visit_Import(self, node):
        """Visit an import node."""
        for alias in node.names:
            self.current_scope.append({
                'type': 'import',
                'name': alias.name,
                'lineno': node.lineno
            })

    def visit_ImportFrom(self, node):
        """Visit an import from node."""
        for alias in node.names:
            self.current_scope.append({
                'type': 'import',
                'name': f"{node.module}.{alias.name}",
                'lineno': node.lineno
            })

    def visit_Assign(self, node):
        """Visit an assignment node."""
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.current_scope.append({
                    'type': 'variable',
                    'name': target.id,
                    'lineno': target.lineno
                })
        self.generic_visit(node)

    def visit_For(self, node):
        """Visit a for loop node."""
        self._process_loop('for_loop', node)

    def visit_While(self, node):
        """Visit a while loop node."""
        self._process_loop('while_loop', node)

    def visit_If(self, node):
        """Visit an if statement node."""
        if_info = {
            'type': 'if_statement',
            'body': [],
            'lineno': node.lineno
        }
        self._process_scope(if_info)

    def _process_scope(self, info):
        """
        Process a new scope (function, class, loop, or conditional).

        Args:
            info (dict): Information about the new scope.
        """
        self.current_scope.append(info)
        previous_scope = self.current_scope
        self.current_scope = info['body']
        self.generic_visit(info)
        self.current_scope = previous_scope

    def _process_loop(self, loop_type, node):
        """
        Process a loop node (for or while).

        Args:
            loop_type (str): Type of the loop ('for_loop' or 'while_loop').
            node (ast.AST): The loop node to process.
        """
        loop_info = {
            'type': loop_type,
            'body': [],
            'lineno': node.lineno
        }
        self._process_scope(loop_info)


def analyze_ast(tree: ast.AST) -> List[Dict[str, Any]]:
    """
    Analyze the given Abstract Syntax Tree.

    Args:
        tree (ast.AST): The AST to analyze.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing information about
        the elements in the analyzed code.
    """
    analyzer = ASTAnalyzer()
    analyzer.visit(tree)
    return analyzer.analysis
