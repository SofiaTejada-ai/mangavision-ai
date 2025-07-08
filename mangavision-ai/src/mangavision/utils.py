import cv2
import numpy as np
from pathlib import Path

def load_page(path: str | Path) -> np.ndarray:

    #Read an image file and return it as an RGB NumPy array.
    #path : str | pathlib.Path is Path to a PNG/JPG page.
    #Returns np.ndarray Array with shape (H, W, 3) in RGB order.

    path = Path(path)

    # cv2.imread reads in BGR by default
    img_bgr = cv2.imread(str(path), cv2.IMREAD_COLOR)
    if img_bgr is None:
        raise FileNotFoundError(path)

    # Convert BGR → RGB so downstream code sees normal colours
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    return img_rgb
