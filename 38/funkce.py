import math


def obvod_kruhu(r):
    return 2 * math.pi * r


def obsah_kruhu(r):
    return math.pi * r**2


def get_quadrangle(a, b, c, d):
    if a == b == c == d:
        print("It is square.")
    if a == c and b == d:
        print("It is rectangel")
    else:
        print("It is general quadragle")


print(obsah_kruhu(10))
print(obvod_kruhu(10))

get_quadrangle(
    10,
    20,
    30,
    40,
)
print("A dalsi text uz bude na dalsim radku,\njak jsem napsal :)")
print(r"A dalsi text uz bude na dalsim radku,\njak jsem napsal :)")
print("A dalsi text uz bude na dalsim radku,\tjak jsem napsal :)")
print("A dalsi text uz bude na dalsim radku,jak jsem napsal :)")
print("A dalsi text uz bude na dalsim radku,\\jak jsem napsal :)")
print("A dalsi text uz bude na dalsim radku,\bjak jsem napsal :)")
print("A dalsi text uz bude na dalsim radku,\000jak jsem napsal :)")
print("A dalsi text uz bude na dalsim radku,\rjak jsem napsal :)")
print(
    """Ze by se
      
     zachoval format
          textu? """
)
zprava = "Julali"
print(zprava[0])
print(zprava[::-1])
print("auto" not in "auta a kone")
stiznost = "Tak si to vsechno velkyma pismenama napis sam!"
print(stiznost.upper())
odpoved = "Ja si to radsi napisu malyma!"
print(odpoved.lower())
titulek = "ti taky napisu"
print(titulek.title())

print(odpoved.islower())
print(zprava.isalpha())
print(zprava.isalnum())
print(zprava.isdecimal())
print(zprava.isspace())
print(zprava.startswith("Ju"))
print(zprava.endswith("li"))

name = ["Jana", "Petr", "Huhňa"]
name2 = " z Pardubic, ".join(name)
print(name2)
name3 = "Jana-Petr-Pavel"
name4 = name3.split("-")
print(name4)
print("kcencecne".rjust(50, "*"))

spam = "     lala   lili   lele     "
spam2 = spam.strip()
print(spam2)
print(spam.count("l"))

message = "Ja vam to dam."
print(message.replace("dam", "nedam"))
