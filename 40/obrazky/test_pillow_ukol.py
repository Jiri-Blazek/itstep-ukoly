import os
from pathlib import Path
import PIL
from PIL import Image


def resize_image(path, save_to, size=(320, 320)):
    image = Image.open(path)
    image.thumbnail(size)
    image.save(save_to)


def get_thumb_path(path, size=(320, 320)):
    comma_position = path.rindex(".")
    extra_name = "-" + str(size[0] + "x" + size[1])
    new_path = path[:comma_position] + extra_name + path[comma_position:]
    return new_path


if __name__ == "__main__":



folder = Path("cesta/k/slozce")

for file in folder.iterdir():
    if file.is_file():
        print(file)



    def main():
        path = r"C:\Users\blaze\OneDrive\Plocha\Programovani\Github\itstep-ukoly\40\>"
        save_to = get_thumb_path(path)
        resize_image(path, save_to)

    main()
# nacist obrazky a doplnit do nich do nazvu velikost
