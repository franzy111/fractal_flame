import random
from abc import ABC, abstractmethod

from src.model.affine_coef import AffineCoefficient
from src.model.fractal_image import FractalImage
from src.model.point import Point
from src.model.rect import Rect
from src.transforms.affine_transformation import AffineTransformation
from src.transforms.transformation import Transformation
from src.utils import random_utils


class AbstractRenderer(ABC):
    """
    Абстрактный класс AbstractRenderer предоставляет базовую реализацию рендеринга фракталов.

    Использует аффинные преобразования, вариации и симметрию для генерации изображения фрактала.
    """

    steps_for_normalization: int
    affine_count: int
    iter_per_sample: int
    symmetry: int
    variations: list[Transformation]

    def __init__(self, steps_for_normalization: int, affine_count: int,
                 iter_per_sample: int, symmetry: int, variations: list[Transformation]) -> None:
        """
        Конструктор для создания рендерера.

        :param steps_for_normalization: Количество шагов для нормализации перед началом записи в изображение.
        :param affine_count: Количество аффинных преобразований.
        :param iter_per_sample: Количество итераций на каждый сэмпл.
        :param symmetry: Количество симметрий для генерации точек.
        :param variations: Список вариаций (трансформаций), применяемых к точкам.
        """
        self.steps_for_normalization = steps_for_normalization
        self.affine_count = affine_count
        self.iter_per_sample = iter_per_sample
        self.symmetry = symmetry
        self.variations = variations

    def render(self, width: int, height: int, world: Rect) -> FractalImage:
        """
        Рендерит фрактальное изображение заданного размера в пределах указанного мирового пространства.

        :param width: Ширина изображения.
        :param height: Высота изображения.
        :param world: Прямоугольник мирового пространства, задающий область рендеринга.
        :return: Объект FractalImage, представляющий отрендеренное изображение.
        """
        image = FractalImage.create(width, height)
        affine_transformations = self.generate_affine_transformations()
        self.render_image(image, world, affine_transformations)
        return image

    @abstractmethod
    def render_image(self, image: FractalImage, world: Rect,
                     affine_transformations: list[AffineTransformation]) -> None:
        """
        Метод, который должен быть реализован в подклассах для управления процессом рендеринга.

        :param image: Изображение, в которое записывается результат.
        :param world: Прямоугольник мирового пространства.
        :param affine_transformations: Список аффинных преобразований.
        """

    def render_one_sample(self, image: "FractalImage", world: "Rect", affine_transformations: list) -> None:
        """
        Обрабатывает один сэмпл для генерации изображения.

        Применяет аффинные преобразования, вариации и симметрию для создания точек.

        :param image: Изображение, в которое записывается результат.
        :param world: Прямоугольник мирового пространства.
        :param affine_transformations: Список аффинных преобразований.
        """
        current_point = random_utils.get_random_point(world)
        for step in range(-self.steps_for_normalization, self.iter_per_sample):
            affine = random_utils.get_random_elem_from_list(affine_transformations)
            variation = random_utils.get_random_elem_from_list(self.variations)
            current_point = affine.apply(current_point)
            current_point = variation.apply(current_point)
            if step > 0:
                theta = 0.0
                for _ in range(self.symmetry):
                    theta += 2 * 3.141592653589793 / self.symmetry
                    point = world.rotate_point(current_point, theta)
                    self.process_point(world, image, point, affine)
    @staticmethod
    def process_point(world: Rect, image: FractalImage, point: Point, affine: AffineTransformation) -> None:
        """
        Обрабатывает точку, преобразуя её в пиксель изображения.

        :param world: Прямоугольник мирового пространства.
        :param image: Изображение, в которое записывается пиксель.
        :param point: Точка, которую нужно преобразовать.
        :param affine: Аффинное преобразование, связанное с точкой.
        """
        pixel = image.resolve_pixel(world, point)
        if pixel:
            pixel.saturate_hit_count(affine.affine_coef.color)

    def generate_affine_transformations(self) -> list:
        """
        Генерирует список случайных аффинных преобразований.

        :return: Список объектов AffineTransformation.
        """
        random_instance = random.Random()
        affine_transformations = []
        for _ in range(self.affine_count):
            transformation = AffineTransformation(AffineCoefficient.generate_random(random_instance))
            affine_transformations.append(transformation)
        return affine_transformations
