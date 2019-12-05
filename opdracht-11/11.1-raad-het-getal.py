import random

# Genereer een getal tussen de 0 en 10
getal = random.randint(0, 10)

# Vraag om input
gok = input("Voer een getal in: ")

# Maak van de input
gok = int(gok)

if gok < getal:
    print("Niet geraden, je zat te laag")

if gok > getal:
    print("Niet geraden, je zat te hoog")

if gok == getal:
    print("Geraden!")
