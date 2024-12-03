from enum import Enum


class ImageFormat(Enum):
    png = "png"
    bmp = "bmp"
    jpeg = "jpg"

    def __init__(self, format_name: str) -> None:
        self.format_name = format_name
