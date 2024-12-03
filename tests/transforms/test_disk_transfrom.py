from decimal import Decimal

from src.model.point import Point
from src.transforms.disk_transformation import DiskTransformation


def test_disk_transform() -> None:
    act_point: Point = Point(1, 1)
    exp_point: Point = Point(-0.2409756332, -0.0665638355)
    assert abs(DiskTransformation().apply(act_point).x - exp_point.x) < Decimal("0.00000001")
    assert abs(DiskTransformation().apply(act_point).y - exp_point.y) < Decimal("0.00000001")
