import random

letters = "abcdefghijklmnopqstruvwxyz"
code = ""

for i in range(4):
    code += random.choice(letters)

pogingen = 0
while True:
    gok = ""
    pogingen += 1

    for i in range(4):
        gok += random.choice(letters)

    if gok == code:
        print("De code was {} ({} pogingen)".format(gok, pogingen))
        break