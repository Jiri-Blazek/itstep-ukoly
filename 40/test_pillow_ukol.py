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
    extra_name = "-" + str(size[0])
    new_path = path[:comma_position] + extra_name + path[comma_position:]
    return new_path


path = Path(
    r"C:\Users\blaze\OneDrive\Plocha\Programovani\Github\itstep-ukoly\40\obrazky"
)

for file in path.iterdir():
    if file.is_file():

        path = str(file)
        print(path)
        save_to = get_thumb_path(path)
        resize_image(path, save_to)


# nacist obrazky a doplnit do nich do nazvu velikost
