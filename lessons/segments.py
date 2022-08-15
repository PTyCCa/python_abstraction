"""Отрезок — еще один графический примитив. В коде описывается парой точек, одна из которых — начало отрезка, другая — конец. Обычный отрезок не имеет направления, поэтому вы сами вольны выбирать то, какую точку считать началом, а какую концом.

В этом задании подразумевается, что вы уже понимаете принцип построения абстракции и способны самостоятельно принять решение о том, как она будет реализована. Напомню, что сделать это можно разными способами и нет одного правильного.

Реализуйте указанные ниже функции:

make_segment() — принимает на вход две точки и возвращает отрезок.
get_mid_point_of_segment() — принимает на вход отрезок и возвращает точку находящуюся на середине отрезка.
get_begin_point() — принимает на вход отрезок и возвращает точку начала отрезка.
get_end_point() — принимает на вход отрезок и возвращает точку конца отрезка.
Представление отрезка вы должны придумать сами!

Пример работы:

>>> from points import make_decart_point

>>> segment = make_segment(make_decart_point(3, 2), make_decart_point(0, 0))
>>> get_begin_point(segment)  # (3, 2)
>>> get_end_point(segment)  # (0, 0)
>>> get_mid_point_of_segment(segment)  # (1.5, 1)
Подсказки
Для создания точек используйте функцию make_decart_point."""

from points import get_x, get_y, make_decart_point


# BEGIN
def make_segment(point1, point2):
    return {"begin_point": point1, "end_point": point2}


def get_begin_point(segment):
    return segment["begin_point"]


def get_end_point(segment):
    return segment["end_point"]


def get_mid_point_of_segment(segment):
    begin_point = get_begin_point(segment)
    end_point = get_end_point(segment)

    x = (get_x(begin_point) + get_x(end_point)) / 2
    y = (get_y(begin_point) + get_y(end_point)) / 2

    return make_decart_point(x, y)
# END