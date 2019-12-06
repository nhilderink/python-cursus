import random

def generate_pw(length=4):
    letters = "abcdefghijklmnopqrstuvwxyz"
    pw = ""
    for i in range(length):
        pw += random.choice(letters)
    return pw

given_password = ""
while True:
    given_password = input("Geef een wachtwoord: ")
    if len(given_password) != 4:
        print("Het wachtwoord moet 4 tekens bevatten")
        continue
    else:
        break

teller = 0
print("Ik ga jouw ww proberen te raden!")
while True:
    teller += 1
    password = generate_pw()
    if password == given_password:
        print("Geraden! Het wachtwoord was {}".format(password))
        print("Ik deed er {} pogingen over".format(teller))
        break
