import random

getal = random.randint(0, 10)
gok = input("Geef een getal op: ")

if gok == getal:
    print("Je hebt het geraden! Het getal was {}".format(gok))
else:
    print("Helaas")
