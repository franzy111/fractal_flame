from dataclasses import dataclass


@dataclass
class Color:
    """
    Представление цвета.
    """

    r: int
    g: int
    b: int
    a: int = 255  # Значение прозрачности по умолчанию

    def to_tuple(self) -> tuple[int, int, int, int]:
        """
        Возвращает цвет в виде кортежа (R, G, B, A).
        """
        return self.r, self.g, self.b, self.a
