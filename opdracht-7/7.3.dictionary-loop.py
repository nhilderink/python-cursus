computer = {
    "hd": "1 tb",
    "ram": "8",
    "cpu": "Intel Core i9",
    "video_kaart": "NVidia"
}

for key in computer:
    # 1e key = "hd"
    # 2e key = "ram"
    # 3e key = "cpu"
    # 4e key = "video_kaart"

    waarde = computer[key]
    print(key + ": " + waarde)
