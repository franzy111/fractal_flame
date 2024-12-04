import math

from src.model.fractal_image import FractalImage
from src.processor.image_processor import ImageProcessor


class LogGammaCorrectionImageProcessor(ImageProcessor):
    """
    Класс LogGammaCorrectionImageProcessor реализует коррекцию изображения

    с использованием логарифмической функции и гамма-коррекции.
    Обрабатывает изображение FractalImage, нормализует значения интенсивности
    пикселей и выполняет гамма-коррекцию для каждого пикселя.
    """

    def __init__(self, gamma: float) -> None:
        """
        Создает экземпляр процессора изображения с заданным значением гаммы.

        :param gamma: Параметр гамма-коррекции (должен быть больше 0).
        """
        if gamma <= 0:
            raise ValueError("Gamma must be greater than 0.")
        self.gamma = gamma

    def processor(self, image: FractalImage) -> None:
        """
        Обрабатывает изображение, применяя логарифмическую нормализацию

        и гамма-коррекцию к каждому пикселю изображения.

        :param image: Объект FractalImage, представляющий изображение фрактала.
        """
        max_value = self._get_max_normal(image)
        self._normalize_and_apply_gamma_correction(image, max_value)
    @staticmethod
    def _get_max_normal(image: FractalImage) -> float:
        """
        Находит максимальное значение нормализации для пикселей изображения.

        Значение нормализации рассчитывается с использованием логарифмической функции.

        :param image: Объект FractalImage, представляющий изображение фрактала.
        :return: Максимальное значение нормализации.
        """
        max_value = 0.00000001
        for y in range(image.height):
            for x in range(image.width):
                pixel = image.pixel(x, y)
                if pixel is not None and pixel.hit_count > 0:
                    pixel.normal = math.log10(pixel.hit_count)
                    max_value = max(max_value, pixel.normal)
        return max_value

    def _normalize_and_apply_gamma_correction(self, image: FractalImage, max_value: float) -> None:
        """
        Выполняет нормализацию значений пикселей изображения и применяет гамма-коррекцию.

        :param image: Объект FractalImage, представляющий изображение фрактала.
        :param max_value: Максимальное значение нормализации.
        """
        for y in range(image.height):
            for x in range(image.width):
                pixel = image.pixel(x, y)
                if pixel is not None:
                    pixel.normal /= max_value
                    correction_factor = math.pow(pixel.normal, 1.0 / self.gamma)
                    pixel.red = int(pixel.red * correction_factor)
                    pixel.green = int(pixel.green * correction_factor)
                    pixel.blue = int(pixel.blue * correction_factor)
