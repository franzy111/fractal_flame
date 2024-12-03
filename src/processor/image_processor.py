from abc import ABC, abstractmethod

from src.model.fractal_image import FractalImage


class ImageProcessor(ABC):
    @abstractmethod
    def processor(self, image: FractalImage) -> None:
        pass
