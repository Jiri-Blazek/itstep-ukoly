import os.path
from pathlib import Path


print(os.path.expanduser("~"))
print(Path.cwd())
print(Path(".").exists())
print(Path("../40").exists())
stat = Path("pid_prodejni_mista.py").stat()
print(stat)

for f in Path(".").iterdir():
    print(f)

path = r"C:\Users\blaze\OneDrive\Plocha\Programovani\Github\itstep-ukoly\39\sonet29.txt"

with open(path) as file:
    a = file.readlines()


for n in a:
    print(n)

with open(path) as file:
    for line in file:
        print(line, end="")

with open(path, "a", encoding="utf-8") as file:  # 'a' append mode
    file.write(
        f"\nJak něco máme,\nhned chceme mít víc.\nTak moc to chceme,\naž nezbyde nám nic."
    )
with open(path, encoding="utf-8") as file:
    for line in file:
        print(line, end="")
