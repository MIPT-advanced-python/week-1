"""
Напишите полностью векторизованный вариант
Дан трёхмерный массив, содержащий изображение размера (height, width, numChannels),
а также вектор длины numChannels.
Сложить каналы изображения с указанными весами и вернуть результат в виде
матрицы размера (height, width).

Преобразуйте цветное изображение в оттенки серого, использовав коэффициенты np.array([0.299, 0.587, 0.114]).
"""

import numpy as np


COEFFICIENTS = np.array([0.299, 0.587, 0.114])


def sum_image_channels(image_path: str) -> np.ndarray:
    # return resulting matrix
    pass
