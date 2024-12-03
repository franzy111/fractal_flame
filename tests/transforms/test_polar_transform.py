from decimal import Decimal

from src.model.point import Point
from src.transforms.polar_transformation import PolarTransformation


def test_polar_transform() -> None:
    act_point: Point = Point(1, 1)
    exp_point: Point = Point(0.25, 0.4142135623)
    assert abs(PolarTransformation().apply(act_point).x - exp_point.x) < Decimal("0.00000001")
    assert abs(PolarTransformation().apply(act_point).y - exp_point.y) < Decimal("0.00000001")
