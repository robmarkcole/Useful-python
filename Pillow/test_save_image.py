from PIL import Image
from unittest.mock import patch
import os


def main():
    image = Image.open("cat.jpg")
    image.save("cat_2.jpg", format="JPEG")
    print("saved cat_2.jpg")


def test_main():
    with patch("PIL.Image.save") as mock_save:
        mock_save.assert_called_with("cat_2.jpg", format="JPEG")


if __name__ == "__main__":
    main()
