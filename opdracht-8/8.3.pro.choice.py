import random
lijst = ["pepernoot", "schuimpje", "chocoladeletter"]
lengte = len(lijst)

willekeurig_getal = random.randint(0, lengte)
willekeurig_item = lijst[willekeurig_getal]

print(willekeurig_item)
