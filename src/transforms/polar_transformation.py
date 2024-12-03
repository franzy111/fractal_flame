import math

from src.model.point import Point
from src.transforms.transformation import Transformation


class PolarTransformation(Transformation):
    def apply(self, point: Point) -> Point:
        dx = math.atan2(point.x, point.y) / math.pi
        dy = math.sqrt(point.x ** 2 + point.y ** 2) - 1
        return Point(dx, dy)
