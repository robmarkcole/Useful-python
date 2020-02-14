from PIL import Image
import numpy as np
from unittest.mock import patch


def get_noise_array():
    shape = (100, 100)
    img_array = np.zeros(shape)

    mean = 0
    gauss = np.random.normal(mean, 1, img_array.shape)

    # normalize image to range [0,255]
    noisy = img_array + gauss
    minv = np.amin(noisy)
    maxv = np.amax(noisy)
    noisy = (255 * (noisy - minv) / (maxv - minv)).astype(np.uint8)
    return noisy


def main():
    image = Image.fromarray(get_noise_array())
    image.save("noise.jpg")


def test_main():
    with patch("PIL.Image.Image.save") as mock_save:
        main()
        mock_save.assert_called_with("noise.jpg")  # kwargs={format: "JPEG"}


if __name__ == "__main__":
    main()
