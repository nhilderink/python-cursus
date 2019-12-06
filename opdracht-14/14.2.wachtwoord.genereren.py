def genereer_wachtwoord():
    import random

    letters = "abcdefghijklmnopqrstuvwxyz"
    ww = ""
    for i in range(4):
        ww += random.choice(letters)
    return ww

wachtwoord = genereer_wachtwoord()
print(wachtwoord)