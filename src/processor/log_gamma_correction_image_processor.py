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

        :param gamma: параметр гамма-коррекции (должен быть больше 0).
        """
        self.gamma = gamma

    def processor(self, image: FractalImage) -> None:
        """
        Обрабатывает изображение, применяя логарифмическую нормализацию и гамма-коррекцию

        к каждому пикселю изображения.

        :param image: Объект FractalImage, представляющий изображение фрактала.
        """
        max_value = 0.0
        for y in range(image.height):
            for x in range(image.width):
                pixel = image.pixel(x, y)
                if pixel is not None and pixel.hit_count != 0:
                    pixel.normal = math.log10(pixel.hit_count)
                    max_value = max(pixel.normal, max_value)

        for y in range(image.height):
            for x in range(image.width):
                pixel = image.pixel(x, y)
                if pixel is not None:
                    pixel.normal = pixel.normal / max_value
                    pixel.red = int(pixel.red * math.pow(pixel.normal, (1.0 / self.gamma)))
                    pixel.green = int(pixel.green * math.pow(pixel.normal, (1.0 / self.gamma)))
                    pixel.blue = int(pixel.blue * math.pow(pixel.normal, (1.0 / self.gamma)))
