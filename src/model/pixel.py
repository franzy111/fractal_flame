import threading
from decimal import Decimal

from src.model.color import Color


class Pixel:
    """
    Класс Pixel представляет собой модель пикселя изображения.

    Хранит информацию о цвете (красный, зеленый, синий), количестве попаданий
    и нормализованном значении. Реализует потокобезопасное обновление цвета пикселя.
    """

    red: int
    green: int
    blue: int
    hit_count: int
    normal: Decimal
    lock_for_color: threading.RLock

    def __init__(self, red: int, green: int, blue: int, hit_count: int, normal: float | Decimal) -> None:
        """
        Конструктор для инициализации пикселя с указанными параметрами.

        :param red: Красная составляющая цвета.
        :param green: Зеленая составляющая цвета.
        :param blue: Синяя составляющая цвета.
        :param hit_count: Количество попаданий в пиксель.
        :param normal: Нормализованное значение.
        """
        self.red = red
        self.green = green
        self.blue = blue
        self.hit_count = hit_count
        self.normal = normal
        self.lock_for_color = threading.RLock()

    def saturate_hit_count(self, color: Color) -> None:
        """
        Обновляет цвет пикселя на основе заданного цвета с учетом количества попаданий.

        Если пиксель еще не был обновлен, он принимает заданный цвет.
        В противном случае средний цвет вычисляется как среднее между текущим и новым цветом.

        Метод потокобезопасен благодаря использованию "замка".

        :param color: Новый цвет для обновления, представленный как кортеж (r, g, b).
        """
        with self.lock_for_color:
            if self.hit_count == 0:
                self.red, self.green, self.blue = color.r, color.g, color.b
            else:
                self.red = (self.red + color.r) // 2
                self.green = (self.green + color.g) // 2
                self.blue = (self.blue + color.b) // 2
            self.hit_count += 1
