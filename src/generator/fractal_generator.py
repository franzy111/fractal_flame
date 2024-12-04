import logging
import time
from pathlib import Path

from src.model.fractal_image import FractalImage
from src.model.rect import Rect
from src.processor.image_processor import ImageProcessor
from src.processor.log_gamma_correction_image_processor import LogGammaCorrectionImageProcessor
from src.renderer.abstract_renderer import AbstractRenderer
from src.saver.fornat_image_saver import FormatImageSaver
from src.ui.command_line_args import CommandLineArgs

logger = logging.getLogger(__name__)

class FractalGenerator:
    """
    Класс FractalGenerator отвечает за генерацию и сохранение фрактального изображения.
    """

    MILLI_TO_SEC = 1000

    def run(self, config: CommandLineArgs) -> None:
        """
        Запускает процесс генерации и сохранения фрактального изображения.

        :param config: Объект Config для получения параметров конфигурации.
        """
        try:
            logger.info("Fractal image generating...")

            start_time = time.time()

            image = self.generate(
                config.get_int("image.height"),
                config.get_int("image.width"),
                config.get_rect(),
                config.get_renderer(),
                LogGammaCorrectionImageProcessor(config.get_float("processor.gamma"))
            )

            end_time = time.time()

            logger.info("Fractal image generated successfully.")
            logger.info("Time: %.2f sec", (end_time - start_time))


            saver = FormatImageSaver(config.get("saver.format"))
            saver.save(
                image,
                Path(f"{config.get('saver.path')}.{config.get('saver.format')}")
            )

            logger.info("Fractal image saved successfully.")
        except Exception:
            logger.exception("Error during fractal generation")
    @staticmethod
    def generate(width: int, height: int, area: Rect, renderer: AbstractRenderer,
                 processor: ImageProcessor) -> FractalImage:
        """
        Генерирует фрактальное изображение.

        :param width: Ширина изображения.
        :param height: Высота изображения.
        :param area: Область для рендеринга.
        :param renderer: Объект Renderer для рендеринга изображения.
        :param processor: Объект ImageProcessor для обработки изображения.
        :return: Объект FractalImage.
        """
        image = renderer.render(width, height, area)
        processor.processor(image)
        return image
