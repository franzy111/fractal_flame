from decimal import Decimal

from src.model.point import Point
from src.transforms.linear_transformation import LinearTransformation


def test_lin_transform() -> None:
    act_point: Point = Point(1, 1)
    exp_point: Point = Point(1, 1)
    assert abs(LinearTransformation().apply(act_point).x - exp_point.x) < Decimal("0.00000001")
    assert abs(LinearTransformation().apply(act_point).y - exp_point.y) < Decimal("0.00000001")
