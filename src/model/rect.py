import math

from src.model.point import Point


class Rect:
    x: float
    y: float
    width: float
    height: float

    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        """
        Класс Rect представляет прямоугольник в двумерной системе координат.

        Хранит координаты верхнего левого угла, ширину и высоту прямоугольника.

        :param x: Координата X верхнего левого угла прямоугольника.
        :param y: Координата Y верхнего левого угла прямоугольника.
        :param width: Ширина прямоугольника.
        :param height: Высота прямоугольника.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def contains(self, p: Point) -> bool:
        """
        Проверяет, содержится ли заданная точка внутри прямоугольника.

        :param p: Точка для проверки (объект класса Point).
        :return: True, если точка находится внутри прямоугольника, иначе False.
        """
        return self.x <= p.x < self.x + self.width and self.y <= p.y < self.y + self.height

    def rotate_point(self, point: Point, angle: float) -> Point:
        """
        Выполняет поворот точки относительно центра прямоугольника на заданный угол.

        :param point: Точка, которую нужно повернуть (объект класса Point).
        :param angle: Угол поворота в радианах (положительное значение — по часовой стрелке).
        :return: Новая точка, являющаяся результатом поворота (объект класса Point).
        """
        center_x = self.x + self.width / 2
        center_y = self.y + self.height / 2

        rotate_x = (point.x - center_x) * math.cos(angle) - (point.y - center_y) * math.sin(angle) + center_x
        rotate_y = (point.x - center_x) * math.sin(angle) + (point.y - center_y) * math.cos(angle) + center_y

        return Point(rotate_x, rotate_y)


