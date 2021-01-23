import ast
import inspect
import numpy as np
import pytest
from pathlib import Path


@pytest.fixture()
def uses_loop():
    def _uses_loop(function):
        loop_statements = ast.For, ast.While, ast.AsyncFor, ast.ListComp

        nodes = ast.walk(ast.parse(inspect.getsource(function)))
        return any(isinstance(node, loop_statements) for node in nodes)
    return _uses_loop


@pytest.fixture(scope='session', params=[1, 2])
def image_fixture(request):
    prefix = Path(__file__).parent.parent/'tests'
    path = prefix/'images'/f'{request.param}.png'
    expected = np.load(prefix/'arrays'/f'{request.param}.npz')['arr_0']
    yield path, expected

