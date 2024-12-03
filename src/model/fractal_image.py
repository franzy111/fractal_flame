from typing import Optional

from src.model.pixel import Pixel
from src.model.point import Point
from src.model.rect import Rect


class FractalImage:
    """
    Класс FractalImage представляет изображение фрактала.

    Содержит массив пикселей, ширину и высоту изображения.
    Является неизменяемым (immutable).
    """

    data: list[Pixel]
    width: int
    height: int

    def __init__(self, data: list[Pixel], width: int, height: int) -> None:
        """
        Инициализирует объект FractalImage с данными пикселей, шириной и высотой изображения.

        :param data: Массив пикселей изображения.
        :param width: Ширина изображения.
        :param height: Высота изображения.
        """
        self.data = data
        self.width = width
        self.height = height

    @classmethod
    def create(cls, width: int, height: int) -> "FractalImage":
        """
        Создает новое изображение фрактала заданной ширины и высоты.

        Все пиксели инициализируются значениями по умолчанию: (0, 0, 0, 0, 0).

        :param width: Ширина изображения.
        :param height: Высота изображения.
        :return: Новый экземпляр FractalImage.
        """
        data = [Pixel(0, 0, 0, 0, 0) for _ in range(width * height)]
        return cls(data, width, height)

    def resolve_pixel(self, rect: Rect, point: Point) -> Optional[Pixel]:
        """
        Находит пиксель, соответствующий точке в заданном прямоугольнике.

        Выполняет преобразование координат точки из системы координат
        прямоугольника в систему координат изображения.

        :param rect: Прямоугольная область, определяющая границы поиска.
        :param point: Точка, для которой требуется найти соответствующий пиксель.
        :return: Пиксель, соответствующий точке, или None, если точка вне области rect.
        """
        if not rect.contains(point):
            return None
        x = int(((point.x - rect.x) / rect.width) * self.width)
        y = int(((point.y - rect.y) / rect.height) * self.height)
        return self.pixel(x, y)

    def contains(self, x: int, y: int) -> bool:
        """
        Проверяет, находятся ли координаты в пределах изображения.

        :param x: Координата по оси X.
        :param y: Координата по оси Y.
        :return: True, если координаты находятся в пределах изображения, иначе False.
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def pixel(self, x: int, y: int) -> Optional[Pixel]:
        """
        Возвращает пиксель по заданным координатам.

        :param x: Координата по оси X.
        :param y: Координата по оси Y.
        :return: Пиксель, расположенный по указанным координатам, или None, если координаты вне границ.
        """
        if not self.contains(x, y):
            return None
        return self.data[y * self.width + x]
