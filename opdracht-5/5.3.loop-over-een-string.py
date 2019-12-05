# i = 0
# for letter in "hallo lekker hoor":
#     if letter == " ":
#         continue
#     i += 1
#     print(letter)
# print(i)

tekst = "hallo lekker hoor"
spaties = 0

for letter in tekst:
    if letter = " ":
        spaties += 1
        continue
    print(letter)

tekst_lengte = len(tekst) - spaties
print(tekst_lengte)
