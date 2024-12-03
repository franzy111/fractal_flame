import math

from src.model.point import Point
from src.transforms.transformation import Transformation


class DiskTransformation(Transformation):
    def apply(self, point: Point) -> Point:
        r = math.sqrt(point.x ** 2 + point.y ** 2)
        dx = 1 / math.pi * math.atan(point.y / point.x) * math.sin(math.pi * r)
        dy = 1 / math.pi * math.atan(point.y / point.x) * math.cos(math.pi * r)
        return Point(dx, dy)
