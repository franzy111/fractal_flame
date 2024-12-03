import math
from decimal import Decimal

from src.model.point import Point
from src.transforms.transformation import Transformation


class ExpTransformation(Transformation):
    def apply(self, point: Point) -> Point:
        dx = math.exp(point.x - 1) * math.cos(Decimal(math.pi) * point.y)
        dy = math.exp(point.x - 1) * math.sin(Decimal(math.pi) * point.y)
        return Point(dx, dy)
