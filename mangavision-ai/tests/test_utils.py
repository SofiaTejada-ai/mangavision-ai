import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
from pathlib import Path
from mangavision.utils import load_page

def test_load_page_shape():
    sample = Path("data/test_pages/sample.png")  # put an actual page here
    assert sample.exists(), "Add one test image under data/test_pages/"
    img = load_page(sample)
    # basic sanity checks
    assert img.ndim == 3 and img.shape[2] == 3        # H, W, C
    assert img.dtype.name == "uint8"
