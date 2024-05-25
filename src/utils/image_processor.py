import cv2
import numpy as np


class ImageProcessor:
    def __init__(self, image_path: str):
        self.image_path = image_path

    def load_image(self) -> np.ndarray:
        return cv2.imread(self.image_path)

    def resize_image(self, width: int, height: int) -> np.ndarray:
        image = self.load_image()
        return cv2.resize(image, (width, height))

    def apply_grayscale(self) -> np.ndarray:
        image = self.load_image()
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def apply_blur(self) -> np.ndarray:
        image = self.load_image()
        return cv2.blur(image, (5, 5))


def process_image(image_path: str, processing_type: str) -> np.ndarray:
    processor = ImageProcessor(image_path)
    if processing_type == "resize":
        return processor.resize_image(640, 480)
    elif processing_type == "grayscale":
        return processor.apply_grayscale()
    elif processing_type == "blur":
        return processor.apply_blur()
    else:
        raise ValueError("Invalid processing type")
