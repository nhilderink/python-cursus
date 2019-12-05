import random

getal = random.randint(0, 100)
pogingen = 0

while True:
    gok = input("Voer een getal in: ")
    gok = int(gok)

    pogingen += 1

    if gok < getal:
        print("Hoger")

    if gok > getal:
        print("Lager")

    if gok == getal:
        print("Geraden! Het geheime getal was {}".format(gok))
        print("Je had er {} pogingen voor nodig".format(pogingen))
        break
