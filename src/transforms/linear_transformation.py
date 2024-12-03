
from src.model.point import Point
from src.transforms.transformation import Transformation


class LinearTransformation(Transformation):
    def apply(self, point: Point) -> Point:
        return point
