from abc import ABC, abstractmethod
from pathlib import Path

from src.model.fractal_image import FractalImage


class ImageSaver(ABC):
    @abstractmethod
    def save(self, image: FractalImage, path: Path) -> None:
        pass
