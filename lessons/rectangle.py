"""Реализуйте абстракцию (набор функций) для работы с прямоугольниками, стороны которого всегда параллельны осям. Прямоугольник может располагаться в любом месте координатной плоскости.

При такой постановке, достаточно знать только три параметра для однозначного задания прямоугольника на плоскости: координаты левой-верхней точки, ширину и высоту. Зная их, мы всегда можем построить прямоугольник одним единственным способом.

      |
    4 |    точка   ширина
      |       *-------------
    3 |       |            |
      |       |            | высота
    2 |       |            |
      |       --------------
    1 |
      |
------|---------------------------
    0 |  1   2   3   4   5   6   7
      |
      |
      |
Основной интерфейс:

make_rectangle (конструктор) – создает прямоугольник. Принимает параметры: левую-верхнюю точку, ширину и высоту. Ширина и высота – положительные числа.
Селекторы get_start_point, get_width и get_height
contains_origin – проверяет, принадлежит ли центр координат прямоугольнику (не лежит на границе прямоугольника, а находится внутри). Чтобы в этом убедиться, достаточно проверить, что все вершины прямоугольника лежат в разных квадрантах (их можно высчитать в момент проверки).
# Создание прямоугольника:
# p - левая верхняя точка
# 4 - ширина
# 5 - высота
#
# p    4
# -----------
# |         |
# |         | 5
# |         |
# -----------

>>> p = make_decart_point(0, 1)
>>> rectangle = make_rectangle(p, 4, 5)

>>> contains_origin(rectangle)
False

>>> rectangle2 = make_rectangle(make_decart_point(-4, 3), 5, 4)
>>> contains_origin(rectangle2)
True
Подсказки
Квадрант плоскости — любая из 4 областей (углов), на которые плоскость делится двумя взаимно перпендикулярными прямыми, принятыми в качестве осей координат.
Для определения квадранта, в которой лежит точка, используйте функцию get_quadrant."""

from points import get_quadrant, get_x, get_y, make_decart_point


# BEGIN
def make_rectangle(point, width, height):
    return {
        "point": point,
        "width": width,
        "height": height,
    }


def get_start_point(rectangle):
    return rectangle['point']


def get_width(rectangle):
    return rectangle['width']


def get_height(rectangle):
    return rectangle['height']


def contains_origin(rectangle):
    point1 = get_start_point(rectangle)
    point2 = make_decart_point(
        get_x(point1) + get_width(rectangle),
        get_y(point1) - get_height(rectangle),
    )

    return get_quadrant(point1) == 2 and get_quadrant(point2) == 4
# END