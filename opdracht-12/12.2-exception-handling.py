while True:
    gok = input("Geef een getal: ")

    try:
        gok = int(gok)
    except ValueError:
        print("Dit is geen geldig getal")
        continue
