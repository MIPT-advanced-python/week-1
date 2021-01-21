import numpy as np
import pytest
from sklearn.preprocessing import normalize
import problem1.solutions as solutions

np.random.seed(0)


def matmult(a,b):
    zip_b = list(zip(*b))
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in a]


def get_answers():
    return [
        ([i for i in range(12, 512)], solutions.task1),
        ([0 for _ in range(54)] + [1] + [0 for _ in range(1000 - 55)], solutions.task2),
        ([[20*j + i for i in range(20)] for j in range(20)], solutions.task3),
    ]


@pytest.mark.parametrize('expected, actual_fn', get_answers(),
                         ids=[f'task{i}' for i in range(1, 4)])
def test_task_1_2_3(uses_loop, expected, actual_fn):
    assert not uses_loop(actual_fn)
    assert (np.array(expected) == actual_fn()).all()


@pytest.mark.parametrize('size', [5, 10, 100, 200, 500])
def test_task_4(uses_loop, size):
    assert not uses_loop(solutions.task4)
    data = np.random.randint(-10, 100, size)
    expected = []
    for item in data:
        if item > 0:
            expected.append(item)
    assert (np.array(expected) == solutions.task4(data)).all()


def test_task_5(uses_loop):
    assert not uses_loop(solutions.task5)
    np.random.seed(0)
    m1, m2, actual = solutions.task5()
    expected = matmult(m1, m2)
    np.testing.assert_allclose(expected, actual)


def test_task_6(uses_loop):
    assert not uses_loop(solutions.task6)
    data = solutions.task6()
    for i in range(len(data)):
        for j in range(len(data[0])):
            if i == 0 or i == len(data) - 1 or j == 0 or j == len(data[0]) - 1:
                assert data[i][j] == 0
            else:
                assert data[i][j] == 1


def test_task_7(uses_loop):
    assert not uses_loop(solutions.task7)
    np.random.seed(0)
    data = solutions.task7()
    assert isinstance(data, np.ndarray)
    assert (sorted(data) == data).all()


def test_task_9(uses_loop):
    assert not uses_loop(solutions.task8)
    np.random.seed(0)
    expected, actual = solutions.task9()
    assert isinstance(expected, np.ndarray)
    assert isinstance(actual, np.ndarray)
    expected = normalize((expected - expected.mean()).reshape(1, -1)).reshape(-1)
    np.testing.assert_allclose(expected, actual)


@pytest.mark.parametrize('number, vector, expected', [
    (3, [1, 2, 3, 4, 5], 3),
    (2, [1, 4, 5, 0, -2], 1),
    (3, [-100, -200, 123, 49, 85], 49)
])
def test_task_10(uses_loop, number, vector, expected):
    assert not uses_loop(solutions.task10)
    actual = solutions.task10(number, np.array(vector))
    assert expected == actual


@pytest.mark.parametrize('n, vector, expected', [
    (3, [1, 2, 3, 4, 9], [3, 4, 9]),
    (1, [1, 10, 4, -2, 5], [10]),
    (5, [-100, 23, 75, 612, 74, -20], [-20, 23, 74, 75, 612])
])
def test_task_11(uses_loop, n, vector, expected):
    assert not uses_loop(solutions.task10)
    expected, vector = map(np.array, (expected, vector))
    actual = solutions.task11(n, np.array(vector))
    assert (expected == actual).all()
