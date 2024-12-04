import random
from decimal import Decimal
from typing import TypeVar

from src.model.point import Point
from src.model.rect import Rect

T = TypeVar("T")

def get_random_point(rect: Rect) -> Point:
    return Point(rect.x + Decimal(random.uniform(0, 1)) * rect.width, rect.y
                 + Decimal(random.uniform(0, 1)) * rect.height)

def get_random_elem_from_list(lst: list[T]) -> T:
    return lst[int(random.uniform(0, len(lst)))]
