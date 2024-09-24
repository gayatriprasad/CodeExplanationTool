"""
This module analyzes the Abstract Syntax Tree (AST) of Python code.
"""
import ast
from typing import List, Dict, Any

def analyze_ast(tree: ast.AST) -> List[Dict[str, Any]]:
    """
    Analyze the given AST and extract relevant information.
    
    Args:
        tree (ast.AST): The AST to analyze.
    
    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing analyzed code structures.
    """
    analyzer = ASTAnalyzer()
    return analyzer.visit(tree)

class ASTAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.structures = []

    def visit_FunctionDef(self, node):
        self.structures.append({
            'type': 'function',
            'name': node.name,
            'args': [arg.arg for arg in node.args.args],
            'body': self.visit_body(node.body)
        })

    def visit_ClassDef(self, node):
        self.structures.append({
            'type': 'class',
            'name': node.name,
            'body': self.visit_body(node.body)
        })

    def visit_Import(self, node):
        for alias in node.names:
            self.structures.append({
                'type': 'import',
                'name': alias.name
            })

    def visit_ImportFrom(self, node):
        for alias in node.names:
            self.structures.append({
                'type': 'import',
                'name': f"{node.module}.{alias.name}"
            })

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.structures.append({
                    'type': 'variable',
                    'name': target.id
                })

    def visit_For(self, node):
        self.structures.append({
            'type': 'for_loop',
            'body': self.visit_body(node.body)
        })

    def visit_While(self, node):
        self.structures.append({
            'type': 'while_loop',
            'body': self.visit_body(node.body)
        })

    def visit_If(self, node):
        self.structures.append({
            'type': 'if_statement',
            'body': self.visit_body(node.body)
        })

    def visit_body(self, body):
        original_structures = self.structures
        self.structures = []
        for item in body:
            self.visit(item)
        body_structures = self.structures
        self.structures = original_structures
        return body_structures

    def generic_visit(self, node):
        super().generic_visit(node)

    def visit(self, node):
        super().visit(node)
        return self.structures