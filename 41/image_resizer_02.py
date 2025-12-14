from PIL import Image


class ImageResizer:
    def __init__(self, path):
        self.path = path

        # self.sizes = sizes

    def resize_images(self, name, *sizes):

        for item in sizes:

            self.resize_image(name, item)

    def resize_image(self, name, size):
        image_path = f"{self.path}\\{name}"
        self.image = Image.open(image_path)
        thumb = self.image.copy()
        thumb.thumbnail((size, size))
        path = self.get_path(size, image_path)
        thumb.save(path)
        # thumb.save("test-%s.jpg" % str(size))

    def get_path(self, size: int, image_path):
        index = image_path.rindex(".")
        extra_name = "-" + str(size)
        return image_path[:index] + extra_name + image_path[index:]


path = r"C:\Users\blaze\OneDrive\Plocha\Programovani\Github\itstep-ukoly\41\Pictures"
my_image_resizer = ImageResizer(path)
my_image_resizer.resize_images("citat_01.jpg", 400, 600, 800)
