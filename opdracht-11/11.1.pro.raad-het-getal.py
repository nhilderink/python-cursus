import random

getal = random.randint(0, 10)
gok = input("Raad het getal: ")
gok = int(gok)

if gok == getal:
    print("Je hebt het geraden")

if gok < getal:
    print("Niet geraden, het getal was hoger")

if gok > getal:
    print("Niet geraden, het getal was lager")
