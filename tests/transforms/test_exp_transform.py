from decimal import Decimal

from src.model.point import Point
from src.transforms.exp_transformation import ExpTransformation


def test_exp_transform() -> None:
    act_point: Point = Point(1, 1)
    exp_point: Point = Point(-1, 0)
    assert abs(ExpTransformation().apply(act_point).x - exp_point.x) < Decimal("0.00000001")
    assert abs(ExpTransformation().apply(act_point).y - exp_point.y) < Decimal("0.00000001")
