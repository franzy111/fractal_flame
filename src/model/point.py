from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Point:
    """
    Представление точки.
    """

    x: Decimal
    y: Decimal

    def __init__(self, x: float | Decimal, y: float | Decimal) -> None:
        self.x = Decimal(x)
        self.y = Decimal(y)
