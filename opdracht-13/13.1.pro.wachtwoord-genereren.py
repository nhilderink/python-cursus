import random

letters = "abcdefghijklmnopqstruvwxyz"
code = ""

for n in range(10):
    for i in range(4):
        code += random.choice(letters)

    print(code)
    code = ""
