import argparse
from typing import Optional

from src.model.rect import Rect
from src.renderer.abstract_renderer import AbstractRenderer
from src.renderer.multi_thread_renderer import MultiThreadRenderer
from src.renderer.single_thread_renderer import SingleThreadRenderer
from src.transforms.disk_transformation import DiskTransformation
from src.transforms.exp_transformation import ExpTransformation
from src.transforms.heart_transformation import HeartTransformation
from src.transforms.hyperbolic_transformation import HyperbolicTransformation
from src.transforms.linear_transformation import LinearTransformation
from src.transforms.polar_transformation import PolarTransformation
from src.transforms.spherical_transformation import SphericalTransformation
from src.transforms.transformation import Transformation


class CommandLineArgs:
    """
    Класс для управления конфигурацией приложения.

    Загружает параметры из командной строки и предоставляет методы доступа к этим параметрам.
    """

    def __init__(self) -> None:
        """
        Инициализация и парсинг аргументов командной строки.
        """
        parser = argparse.ArgumentParser(description="Application configuration parser.")

        # Параметры для изображения
        parser.add_argument("--image.width", type=int, required=True, help="Ширина изображения.")
        parser.add_argument("--image.height", type=int, required=True, help="Высота изображения.")

        # Параметры для прямоугольника (Rect)
        parser.add_argument("--rect.cordX", type=float, required=True,
                            help="Координата X прямоугольника.")
        parser.add_argument("--rect.cordY", type=float, required=True,
                            help="Координата Y прямоугольника.")
        parser.add_argument("--rect.width", type=float, required=True, help="Ширина прямоугольника.")
        parser.add_argument("--rect.height", type=float, required=True, help="Высота прямоугольника.")

        # Параметры рендера
        parser.add_argument("--renderer.type", type=str, required=True,
                            help="Тип рендерера (multi/simple).")
        parser.add_argument("--affineCount", type=int, required=True,
                            help="Количество аффинных преобразований.")
        parser.add_argument("--samples", type=int, required=True, help="Количество выборок.")
        parser.add_argument("--iterSamples", type=int, required=True,
                            help="Количество итераций на выборку.")
        parser.add_argument("--symmetry", type=int, required=True, help="Симметрия.")
        parser.add_argument("--steps", type=int, required=True, help="Количество шагов рендера.")

        # Параметр процессора
        parser.add_argument("--processor.gamma", type=float, required=True,
                            help="Значение гамма-коррекции.")

        # Трансформации
        transformations = [
            "DiskTrans", "ExpTrans", "HeartTrans", "HyperTrans",
            "LinearTrans", "PolarTrans", "SphericalTrans"
        ]
        for trans in transformations:
            parser.add_argument(f"--transformations.{trans}", action="store_true",
                                help=f"Включить трансформацию {trans}.")

        # Параметры сохранения
        parser.add_argument("--saver.format", type=str, required=True,
                            help="Формат сохранения изображения (например, png).")
        parser.add_argument("--saver.path", type=str, required=True,
                            help="Путь для сохранения изображения.")

        self.args = parser.parse_args()


    def get(self, key: str) -> Optional[str]:
        """
        Возвращает значение параметра.

        :param key: Ключ параметра.
        :return: Значение параметра или None, если ключ отсутствует.
        """
        args_dict = vars(self.args)
        return args_dict.get(key, None)

    def get_int(self, key: str) -> int:
        """
        Возвращает значение параметра в виде целого числа.

        :param key: Ключ параметра.
        :return: Значение параметра.
        """
        value = self.get(key)
        if value is None:
            raise ValueError("Параметр отсутствует в конфигурации.")
        try:
            return int(value)
        except ValueError as err:
            raise ValueError("Значение параметра не может быть преобразовано в целое число") from err

    def get_float(self, key: str) -> float:
        """
        Возвращает значение параметра в виде числа с плавающей точкой.

        :param key: Ключ параметра.
        :return: Значение параметра.
        """
        return float(self.get(key))


    def get_rect(self) -> Rect:
        """
        Возвращает объект прямоугольника (Rect) с координатами и размерами, полученными из конфигурации.

        :return: Объект прямоугольника.
        """
        x = self.get_float("rect.cordX")
        y = self.get_float("rect.cordY")
        width = self.get_float("rect.width")
        height = self.get_float("rect.height")

        return Rect(x, y, width, height)

    def get_renderer(self) -> AbstractRenderer:
        """
        Создает и возвращает экземпляр рендерера в зависимости от параметров конфигурации.

        :return: Экземпляр рендерера.
        """
        steps = self.get_int("steps")
        affine_count = self.get_int("affineCount")
        samples = self.get_int("samples")
        iter_samples = self.get_int("iterSamples")
        symmetry = self.get_int("symmetry")

        renderer_type = self.get("renderer.type")

        if renderer_type == "multi":
            return MultiThreadRenderer(steps, affine_count, samples, iter_samples, symmetry, self.get_transformations())

        return SingleThreadRenderer(steps, affine_count, samples, iter_samples, symmetry, self.get_transformations())

    def get_transformations(self) -> list[Transformation]:
        """
        Создает и возвращает список трансформаций на основе параметров конфигурации.

        :return: Список трансформаций.
        """
        transformations = []

        if self.get("transformations.DiskTrans"):
            transformations.append(DiskTransformation())
        if self.get("transformations.ExpTrans"):
            transformations.append(ExpTransformation())
        if self.get("transformations.HeartTrans"):
            transformations.append(HeartTransformation())
        if self.get("transformations.HyperTrans"):
            transformations.append(HyperbolicTransformation())
        if self.get("transformations.LinearTrans"):
            transformations.append(LinearTransformation())
        if self.get("transformations.PolarTrans"):
            transformations.append(PolarTransformation())
        if self.get("transformations.SphericalTrans"):
            transformations.append(SphericalTransformation())

        return transformations
