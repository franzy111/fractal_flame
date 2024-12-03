from decimal import Decimal

from src.model.point import Point
from src.transforms.hyperbolic_transformation import HyperbolicTransformation


def test_hyper_transform() -> None:
    act_point: Point = Point(1, 1)
    exp_point: Point = Point(0.5, 1)
    assert abs(HyperbolicTransformation().apply(act_point).x - exp_point.x) < Decimal("0.00000001")
    assert abs(HyperbolicTransformation().apply(act_point).y - exp_point.y) < Decimal("0.00000001")
