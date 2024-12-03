from src.model.affine_coef import AffineCoefficient
from src.model.point import Point
from src.transforms.transformation import Transformation


class AffineTransformation(Transformation):
    affine_coef: AffineCoefficient

    def __init__(self, affine_coef: AffineCoefficient) -> None:
        self.affine_coef = affine_coef

    def apply(self, point: Point) -> Point:
        x = (self.affine_coef.a * point.x +
             self.affine_coef.b * point.y + self.affine_coef.c)
        y = (self.affine_coef.d * point.x +
             self.affine_coef.e * point.y + self.affine_coef.f)
        return Point(x, y)
