getal = 0
while True:
    getal = input("Geef een getal: ")
    try:
        getal = int(getal)
        print(getal * 2)
        break
    except ValueError:
        print("Dit was geen geldig getal")
