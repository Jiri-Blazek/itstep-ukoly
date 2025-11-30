import json
import random


with open(
    r"C:\Users\blaze\OneDrive\Plocha\Programovani\PYTHON\37\pokemon.json"
) as file:
    data = json.load(file)


seznam = []
for a in range(10):
    nahodne_cislo = random.randint(1, 100)
    seznam.append(nahodne_cislo)


novy_objekt = seznam[:]
novy_objekt[0] = 6
print(seznam)
print(novy_objekt)
print(len(novy_objekt))
soucet = seznam + novy_objekt
print(soucet)

pismena = ["a", "b", "c"]
cisla = [1, 2, 3]
pismena3 = 3 * pismena
print(pismena3)


for index, item in enumerate(pismena):
    print(index, item)

for item in zip(cisla, pismena):
    print(item)


print("a" in pismena)
print("d" in pismena)
print("d" not in pismena)


alpha, beta, gamma = pismena
print(alpha, beta, gamma)
cisla = [1, 2, 3]
auto, bus = cisla[:-1]
print(auto, bus)
alpha, beta = beta, alpha
print(alpha, beta)

print(pismena.index("c"))
pismena.insert(1, "d")
print(pismena)

del pismena[1]
print(pismena)

pismena.remove("c")
print(pismena)

animals = ["cat", "bat", "rat", "elephant"]
a = animals.pop()
print(a)
b = animals.pop(0)
print(b)

seznam.sort(reverse=True)
print(seznam)
animals.sort()
print(animals)

pismena2 = [
    "a",
    "C",
    "b",
    "B",
    "c",
    "A",
]
pismena2.sort(key=str.lower)
print(pismena2)

furniture = ("table", "chair", "rack", "shelf")
pismena3 = tuple(pismena2)
print(pismena3)
pismena4 = list(pismena3)
print(pismena4)
g = list("johoho")
print(g)
