import random
from typing import Final

from src.model.color import Color


class AffineCoefficient:
    """
    Класс, представляющий коэффициенты для аффинного преобразования.

    Каждый объект содержит шесть коэффициентов (a, b, c, d, e, f) и цвет, связанный с преобразованием.
    """

    MAX_COLOR_RANGE: Final[int] = 255

    a: float
    b: float
    c: float
    d: float
    e: float
    f: float
    color: Color

    def __init__(self, coefficients: dict[str, float], color: Color) -> None:
        """
        Инициализирует объект с коэффициентами и цветом.

        :param coefficients: Словарь с коэффициентами a, b, c, d, e, f.
        :param color: Цвет, представленный как кортеж (r, g, b).
        """
        self.a = coefficients["a"]
        self.b = coefficients["b"]
        self.c = coefficients["c"]
        self.d = coefficients["d"]
        self.e = coefficients["e"]
        self.f = coefficients["f"]
        self.color = color

    @staticmethod
    def generate_random(random_instance: random.Random) -> "AffineCoefficient":
        """
        Генерирует случайный объект AffineCoefficient.

        Коэффициенты a, b, c, d, e, f генерируются случайным образом, при этом a, b, d, e
        удовлетворяют условиям аффинного преобразования.

        :param random_instance: Экземпляр random, используемый для генерации случайных значений.
        :return: Новый объект AffineCoefficient с случайными коэффициентами и цветом.
        """
        c = random_instance.uniform(-1, 1)
        f = random_instance.uniform(-1, 1)

        while True:
            a = random_instance.uniform(-1, 1)
            b = random_instance.uniform(-1, 1)
            d = random_instance.uniform(-1, 1)
            e = random_instance.uniform(-1, 1)
            if AffineCoefficient.is_affine(a, b, d, e):
                break

        color = Color(random_instance.randint(0, AffineCoefficient.MAX_COLOR_RANGE),
                 random_instance.randint(0, AffineCoefficient.MAX_COLOR_RANGE),
                 random_instance.randint(0, AffineCoefficient.MAX_COLOR_RANGE))
        coefficients: dict[str, float] = {
            "a": a,
            "b": b,
            "c": c,
            "d": d,
            "e": e,
            "f": f
        }
        return AffineCoefficient(coefficients, color)

    @staticmethod
    def is_affine(a: float, b: float, d: float, e: float) -> bool:
        """
        Проверяет, соответствуют ли заданные коэффициенты условиям аффинного преобразования.

        :param a: Коэффициент a.
        :param b: Коэффициент b.
        :param d: Коэффициент d.
        :param e: Коэффициент e.
        :return: True, если коэффициенты соответствуют условиям, иначе False.
        """
        return (a ** 2 + d ** 2) < 1 and (b ** 2 + e ** 2) < 1 and \
            (a ** 2 + b ** 2 + d ** 2 + e ** 2) < (1 + (a * e - b * d) ** 2)
