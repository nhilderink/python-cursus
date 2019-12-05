while True:
    treden = input("Geen aantal treden: ")

    try:
        treden = int(treden)

    except ValueError:
        print("Dit is geen geldig getal")
        continue

    for i in range(treden):
        print("#" * (i + 1))

    break
