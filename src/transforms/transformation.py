from abc import ABC, abstractmethod

from src.model.point import Point


class Transformation(ABC):
    @abstractmethod
    def apply(self, point: Point) -> Point:
        """
        Нелинейное преобразование, которое принимает точку в качестве входных данных

        и возвращает новую точку в качестве результата.

        :param point: Точка.
        :return: Точка, полученная путём преобразований.
        """
