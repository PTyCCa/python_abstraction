"""Реализуйте абстракцию для работы с рациональными числами включающую в себя следующие функции:

Конструктор make — принимает на вход числитель и знаменатель, возвращает дробь.
Селектор get_numer — возвращает числитель
Селектор get_denom — возвращает знаменатель
Сложение add — складывает переданные дроби
Вычитание sub — находит разность между двумя дробями
Не забудьте реализовать нормализацию дробей удобным для вас способом.

Примеры работы:

>>> import rational

>>> rat1 = rational.make(3, 9)
>>> rational.get_numer(rat1)
1
>>> rational.get_denom(rat1)
3
>>> rat2 = rational.make(10, 3)
>>> rat3 = rational.add(rat1, rat2)
>>> rational.to_str(rat3)
11/3
>>> rat4 = rational.sub(rat1, rat2)
>>> rational.to_str(rat4)
-3/1
Подсказки
Функция gcd из модуля math находит наибольший общий делитель двух чисел
Функция to_str возвращает строковое представление числа (используется для отладки)
Функция int преобразует значение к целому числу"""

import math


# BEGIN
def make(numer, denom):
    gcd = math.gcd(numer, denom)
    return {
        "numer": int(numer / gcd),
        "denom": int(denom / gcd),
    }


def get_numer(rat):
    return rat["numer"]


def get_denom(rat):
    return rat["denom"]


def add(rat1, rat2):
    numer1 = get_numer(rat1)
    denom1 = get_denom(rat1)
    numer2 = get_numer(rat2)
    denom2 = get_denom(rat2)

    return make(
        numer1 * denom2 + numer2 * denom1,
        denom1 * denom2,
    )


def sub(rat1, rat2):
    numer1 = get_numer(rat1)
    denom1 = get_denom(rat1)
    numer2 = get_numer(rat2)
    denom2 = get_denom(rat2)

    return make(
        numer1 * denom2 - numer2 * denom1,
        denom1 * denom2,
    )
# END


def to_str(rat):
    return "{}/{}".format(get_numer(rat), get_denom(rat))


_______________________

from fractions import Fraction


# BEGIN (write your solution here)
def make(numer, denom):
    return Fraction(numer, denom)


def get_numer(rational):
    return rational.numerator


def get_denom(rational):
    return rational.denominator


def add(rat1, rat2):
    return rat1 + rat2


def sub(rat1, rat2):
    return rat1 - rat2


# END


def to_str(rat):
    return "{}/{}".format(get_numer(rat), get_denom(rat))
