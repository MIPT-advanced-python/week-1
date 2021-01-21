"""
Рассмотрим сложную математическую функцию на отрезке [1, 15]:

f(x) = sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)

Она может описывать, например, зависимость оценок, которые выставляют определенному сорту вина эксперты,
в зависимости от возраста этого вина.
Мы хотим приблизить сложную зависимость с помощью функции из определенного семейства.
В этом задании мы будем приближать указанную функцию с помощью многочленов.

Как известно, многочлен степени n
w_0 + w_1 x + w_2 x^2 + ... + w_n x^n
однозначно определяется любыми n + 1 различными точками, через которые он проходит.
Это значит, что его коэффициенты w_0, ..., w_n можно определить через систему:

w_0 + w_1 x_0 + w_2 (x_0)^2 + ... + w_n (x_0)^n = y_0
w_0 + w_1 x_1 + w_2 (x_1)^2 + ... + w_n (x_1)^n = y_1
.............
w_0 + w_1 x_n + w_2 (x_n)^2 + ... + w_n (x_2)^n = y_n

Задание состоит из нескольких частей:

0. Сформулируйте систему на языке A*x = b, т.е. поймите, как сделать матрицу A, вектор b.
"""


def task1():
    """
    Возьмите f в точках 1 и 15, затем решите систему с помощью scipy.linalg.solve
    Нарисуйте функцию f и полученный многочлен.
    Хорошо ли он аппруксимирует?
    Почему это прямая?

    :return: верните вектор решения системы
    """
    pass


def task2():
    """
    Сделайте то же самое, но для многочлена второй степени, взяв f в точках 1, 8 и 15.
    Улучшилось ли качество?

    :return: верните вектор решения системы
    """
    pass


def task3():
    """
    Сделайте то же самое, но для многочлена третей степени, взяв f в точках 1, 4, 10, 15.

    :return: верните вектор решения системы
    """
    pass