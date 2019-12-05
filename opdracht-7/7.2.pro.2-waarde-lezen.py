auto = {
    "merk": "Volkswagen",
    "model": "Golf",
    "opties": ["airco", "cruise control", "automaat"],
    "top_snelheid": 140
}

key = "opties"
opties = auto[key]

for optie in opties:
    print(optie)
