import math

from src.model.point import Point
from src.transforms.transformation import Transformation


class HeartTransformation(Transformation):
    def apply(self, point: Point) -> Point:
        o = math.atan(point.x / point.y)
        r = math.sqrt(point.x ** 2 + point.y ** 2)
        dx = r * math.sin(o * r)
        dy = -r * math.cos(o * r)
        return Point(dx, dy)
