from pathlib import Path

from PIL import Image

from src.model.fractal_image import FractalImage
from src.saver.image_saver import ImageSaver


class FormatImageSaver(ImageSaver):
    def __init__(self, image_format: str) -> None:
        """
        Класс для сохранения фрактального изображения в файл в указанном формате.

        :param image_format: Формат изображения (например, 'png', 'bmp', 'jpeg').
        """
        self.format = image_format

    def save(self, image: FractalImage, path: Path) -> None:
        """
        Сохраняет фрактальное изображение в файл в указанном формате.

        :param image: Фрактальное изображение, которое нужно сохранить.
        :param path: Путь, по которому нужно сохранить изображение.
        """
        rendered_image = self._convert_fractal_image_to_pil_image(image)
        rendered_image.save(path, format=self.format)

    @staticmethod
    def _convert_fractal_image_to_pil_image(image: FractalImage) -> Image:
        """
        Преобразует фрактальное изображение в объект PIL Image.

        :param image: Фрактальное изображение, которое нужно преобразовать.
        :return: Объект PIL Image.
        """
        pil_image = Image.new("RGB", (image.width, image.height))
        for y in range(image.height):
            for x in range(image.width):
                pixel = image.pixel(x, y)
                if pixel is not None:
                    color = (pixel.red, pixel.green, pixel.blue)
                    pil_image.putpixel((x, y), color)
        return pil_image
