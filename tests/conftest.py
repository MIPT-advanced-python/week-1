import ast
import inspect
import pytest


@pytest.fixture()
def uses_loop():
    def _uses_loop(function):
        loop_statements = ast.For, ast.While, ast.AsyncFor, ast.ListComp

        nodes = ast.walk(ast.parse(inspect.getsource(function)))
        return any(isinstance(node, loop_statements) for node in nodes)
    return _uses_loop
