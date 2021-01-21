import numpy as np
import pytest
from pathlib import Path
from problem3.solutions import task1, task2, task3


basedir = Path(__file__).parent.parent/'tests'/'arrays'


@pytest.mark.parametrize('array, func', [
    (np.load(basedir / 'p3t1.npy'), task1),
    (np.load(basedir / 'p3t2.npy'), task2),
    (np.load(basedir / 'p3t3.npy'), task3),
], ids=['task1', 'task2', 'task3'])
def test_problem_3(array, func):
    np.testing.assert_allclose(func(), array)
