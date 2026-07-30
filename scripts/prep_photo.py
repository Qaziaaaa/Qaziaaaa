import sys
import os
from PIL import Image

try:
    import cv2
    import numpy as np
    CV2_OK = True
except ImportError:
    CV2_OK = False
    np = None

try:
    from rembg import remove
except ImportError:
    remove = None

INPUT = sys.argv[1] if len(sys.argv) > 1 else "profile.jpg"
OUTPUT = "profile-prepped.png"


def main():
    if not os.path.exists(INPUT):
        print(f"Input {INPUT} not found")
        sys.exit(1)

    img = Image.open(INPUT).convert("RGB")

    if remove is not None:
        try:
            img_no_bg = remove(img)
        except Exception:
            img_no_bg = img
    else:
        img_no_bg = img

    if CV2_OK and np is not None:
        img_cv = cv2.cvtColor(np.array(img_no_bg), cv2.COLOR_RGB2BGR)
        lab = cv2.cvtColor(img_cv, cv2.COLOR_BGR2LAB)
        l_ch, a_ch, b_ch = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        l_ch = clahe.apply(l_ch)
        lab = cv2.merge((l_ch, a_ch, b_ch))
        img_eq = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
        img_rgb = cv2.cvtColor(img_eq, cv2.COLOR_BGR2RGB)
        if img_no_bg.mode == "RGBA":
            alpha = np.array(img_no_bg)[:, :, 3:] / 255.0
            white = np.ones_like(img_rgb, dtype=np.uint8) * 255
            composite = (img_rgb * alpha + 255 * (1 - alpha)).astype(np.uint8)
        else:
            composite = img_rgb
        result = Image.fromarray(composite)
    else:
        result = img_no_bg.convert("L")

    result.convert("L").save(OUTPUT)
    print(f"Saved {OUTPUT}")


if __name__ == "__main__":
    main()
