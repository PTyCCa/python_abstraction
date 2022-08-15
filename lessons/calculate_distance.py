"""Реализуйте функцию calculate_distance(), которая находит расстояние между двумя точками на плоскости:

>>> point1 = [0, 0]
>>> point2 = [3, 4]
>>> calculate_distance(point1, point2)
5.0"""

# BEGIN
import math


def calculate_distance(point1, point2):
    delta_x = point2[0] - point1[0]
    delta_y = point2[1] - point1[1]

    return math.sqrt((delta_x ** 2) + (delta_y ** 2))
# END