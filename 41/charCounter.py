from pathlib import Path


class charCounter:
    def __init__(self, path):
        self.path = path

    def open_file(self):
        content = Path(path).read_text(encoding="utf-8")
        print(content)
        return content

    def count_char(self):
        content = self.open_file()
        print("Počet znaků v souboru je:", len(content))

    def count_words(self):
        word_count = 0
        with open(self.path, "r", encoding="utf-8") as file:
            while True:
                line = file.readline()
                words = line.split(" ")
                word_count += len(words)
                if not line:
                    break
        print("Počet slov v souboru je:", word_count)


path = r"C:\Users\blaze\OneDrive\Plocha\Programovani\Github\itstep-ukoly\41\sonet29.txt"
file = charCounter(path)
file.count_char()
file.count_words()
