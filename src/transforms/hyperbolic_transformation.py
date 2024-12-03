import math

from src.model.point import Point
from src.transforms.transformation import Transformation


class HyperbolicTransformation(Transformation):
    def apply(self, point: Point) -> Point:
        o = math.atan(point.x / point.y)
        r = math.sqrt(point.x ** 2 + point.y ** 2)
        dx = math.sin(o) / r
        dy = r * math.cos(o)
        return Point(dx, dy)
