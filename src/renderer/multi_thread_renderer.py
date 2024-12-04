from concurrent.futures import ThreadPoolExecutor

from src.model.fractal_image import FractalImage
from src.model.rect import Rect
from src.renderer.abstract_renderer import AbstractRenderer
from src.transforms.affine_transformation import AffineTransformation
from src.transforms.transformation import Transformation


class MultiThreadRenderer(AbstractRenderer):
    """
    Класс, реализующий рендеринг фрактала с использованием многозадачности.

    Использует пул процессов для параллельного выполнения нескольких выборок фрактала.
    """

    def __init__(self, steps_for_normalization: int, affine_count: int,
                 samples: int, iter_per_sample: int, symmetry: int,
                 variations: list[Transformation]) -> None:
        """
        Конструктор для инициализации параметров рендеринга.

        :param steps_for_normalization: Шаги нормализации.
        :param affine_count: Количество аффинных преобразований.
        :param samples: Количество выборок для рендеринга.
        :param iter_per_sample: Количество итераций для каждой выборки.
        :param symmetry: Симметрия фрактала (например, количество повторений).
        :param variations: Список вариаций преобразований.
        """
        super().__init__(steps_for_normalization, affine_count, iter_per_sample, symmetry, variations)
        self.samples = samples

    def render_image(self, image: FractalImage, world: Rect,
                     affine_transformations: list[AffineTransformation]) -> None:
        """
        Рендерит фрактал в многозадачном режиме, используя пул процессов.

        Для каждой выборки создается отдельный процесс.

        :param image: Фрактальное изображение, которое будет рендериться.
        :param world: Прямоугольник, определяющий область видимости фрактала.
        :param affine_transformations: Список аффинных преобразований.
        """
        with ThreadPoolExecutor() as executor:
            tasks = [executor.submit(self.render_one_sample, image, world, affine_transformations)
                     for _ in range(self.samples)]
            for task in tasks:
                task.result()
