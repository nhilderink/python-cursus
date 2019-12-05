'''
    Dit is commentaar. Je herkent dit aan de drie aanhalingstekens.
    Alles dat hier tussen wordt geschreven wordt door Python
    genegeerd.
'''

# Commentaar op 1 regel kan ook, met een hashtag.

# Hier importeren we functionaliteit uit een andere module
from random import randrange

# Definieer een functie met 'film' als parameter
def random_rating(film):
    rating = randrange(10)

    fun = None

    if rating < 6:
        fun = False
    else:
        fun = True

    print("{}: {}, {}".format(film, rating, fun))

# Maak een lijst met films
films = [
    "Lord of the Rings",
    "Jurassic Parc",
    "The It",
    "Saving Private Ryan"
]

# Met een zgn. for-loop gaan we alle films 1 voor 1 langs
for film in films:
    # En met elke film roepen we de functie 'random_rating' aan
    random_rating(film)
