'''
    Wanneer je iets invult dat geen getal is krijg
    je een ValueError. Met onderstaande constructie kun je
    dit ondervangen. Zie hiervoor de appendix A in de map.
'''

getal = input("Geef een getal: ")

try:
    getal = int(getal)
    print(getal * 2)
except ValueError:
    print("Dit was geen geldig getal")
