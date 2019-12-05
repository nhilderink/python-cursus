import random

letters = "abcdefghijklmnopqstruvwxyz"
code = ""

for i in range(4):
    code += random.choice(letters)

print(code)
