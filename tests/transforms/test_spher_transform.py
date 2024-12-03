from decimal import Decimal

from src.model.point import Point
from src.transforms.spherical_transformation import SphericalTransformation


def test_spher_transform() -> None:
    act_point: Point = Point(1, 1)
    exp_point: Point = Point(0.5, 0.5)
    assert abs(SphericalTransformation().apply(act_point).x - exp_point.x) < Decimal("0.00000001")
    assert abs(SphericalTransformation().apply(act_point).y - exp_point.y) < Decimal("0.00000001")
