from src.model.fractal_image import FractalImage
from src.model.rect import Rect
from src.transforms.affine_transformation import AffineTransformation
from src.transforms.transformation import Transformation

from .abstract_renderer import AbstractRenderer


class SingleThreadRenderer(AbstractRenderer):
    """
    Класс для рендеринга фрактала с использованием простого однофазного рендеринга.

    Каждый сэмпл фрактала обрабатывается последовательно, без использования многозадачности.
    """

    def __init__(self, steps_for_normalization: int, affine_count: int, samples: int,
                 iter_per_sample: int, symmetry: int, variations: list[Transformation]) -> None:
        """
        Инициализирует параметры рендеринга.

        :param steps_for_normalization: Количество шагов для нормализации.
        :param affine_count: Количество аффинных преобразований.
        :param samples: Количество сэмплов для рендеринга.
        :param iter_per_sample: Количество итераций на каждый сэмпл.
        :param symmetry: Симметрия фрактала (например, количество повторений).
        :param variations: Список вариаций преобразований.
        """
        super().__init__(steps_for_normalization, affine_count, iter_per_sample, symmetry, variations)
        self.samples = samples

    def render_image(self, image: FractalImage, world: Rect,
                     affine_transformations: list[AffineTransformation]) -> None:
        """
        Рендерит фрактал, выполняя заданное количество сэмплов последовательно.

        Каждый сэмпл генерируется на основе аффинных преобразований и вариаций, без использования многозадачности.

        :param image: Фрактальное изображение, которое будет рендериться.
        :param world: Прямоугольник, определяющий область видимости фрактала.
        :param affine_transformations: Список аффинных преобразований, которые будут применяться к фракталу.
        """
        for _ in range(self.samples):
            self.render_one_sample(image, world, affine_transformations)
