from decimal import Decimal

from src.model.point import Point
from src.transforms.heart_transformation import HeartTransformation


def test_heart_transform() -> None:
    act_point: Point = Point(1, 1)
    exp_point: Point = Point(1.2671621313, -0.6279332232)
    assert abs(HeartTransformation().apply(act_point).x - exp_point.x) < Decimal("0.00000001")
    assert abs(HeartTransformation().apply(act_point).y - exp_point.y) < Decimal("0.00000001")
