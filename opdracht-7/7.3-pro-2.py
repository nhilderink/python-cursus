autos = [
    {"merk": "Volkswagen", "model": "Golf"},
    {"merk": "Volvo", "model": "V60"},
    {"merk": "Toyota", "model": "RAV4"},
    {"merk": "Fiat", "model": "Punto"},
    {"merk": "Opel", "model": "Corsa"}
]

print("Autos")
print("=====")
for auto in autos:
    output = ""
    for key in auto:
        output += auto[key] + " "
    print(output)
