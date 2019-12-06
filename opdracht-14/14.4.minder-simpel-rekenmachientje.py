def rekenmachine(getal1, getal2, operatie):
    if operatie == "o":
        return getal1 + getal1

    if operatie == "a":
        return getal1 - getal2

    if operatie == "d":
        return getal1 / getal2

    if operatie == "v":
        return getal1 * getal2


som = rekenmachine(1, 4, "o")
af = rekenmachine(1, 4, "a")
delen = rekenmachine(4, 2, "d")
vermenigvuldig = rekenmachine(5, 4, "v")

print(som)
print(af)
print(delen)
print(vermenigvuldig)

