from decimal import Decimal

import pytest

from src.model.affine_coef import AffineCoefficient
from src.model.color import Color
from src.transforms.affine_transformation import AffineTransformation


@pytest.fixture
def affine_transformation() -> AffineTransformation:
    coef: dict[str, Decimal] = {
        "a": Decimal(0.1),
        "b": Decimal(0.2),
        "c": Decimal(0.3),
        "d": Decimal(0.4),
        "e": Decimal(0.5),
        "f": Decimal(0.6)
    }
    affine_coef: AffineCoefficient = AffineCoefficient(coef, Color(1, 1, 1))
    return AffineTransformation(affine_coef)
