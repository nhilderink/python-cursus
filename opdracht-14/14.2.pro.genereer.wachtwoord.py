def genereer_wachtwoord(lengte=4):
    import random

    letters = "abcdefghijklmnopqrstuvwxyz"
    ww = ""
    for i in range(lengte):
        ww += random.choice(letters)
    return ww

wachtwoord = genereer_wachtwoord()
print(wachtwoord)
