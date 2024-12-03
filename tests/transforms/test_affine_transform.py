from decimal import Decimal

import pytest

from src.model.point import Point
from src.transforms.affine_transformation import AffineTransformation


@pytest.mark.parametrize(
    ("x", "y", "res_x", "res_y"),
    [
        (0, 0, 0.3, 0.6),
        (1, 1, 0.6, 1.5)
    ]
)
def test_affine_transform(affine_transformation: AffineTransformation, x: float, y: float,
                          res_x: float, res_y: float)-> None:
    act_point: Point = Point(x, y)
    exp_point: Point = Point(res_x, res_y)
    assert (abs(affine_transformation.apply(act_point).x - exp_point.x) < Decimal("0.000000001"))
    assert (abs(affine_transformation.apply(act_point).y - exp_point.y) < Decimal("0.000000001"))
