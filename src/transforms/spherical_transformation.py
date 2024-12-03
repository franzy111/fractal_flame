
from src.model.point import Point
from src.transforms.transformation import Transformation


class SphericalTransformation(Transformation):
    def apply(self, point: Point) -> Point:
        r = point.x ** 2 + point.y ** 2
        dx = (1 / r) * point.x
        dy = (1 / r) * point.y
        return Point(dx, dy)
