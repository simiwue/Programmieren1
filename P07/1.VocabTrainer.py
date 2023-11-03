# Zufall importieren
import random
# Dictionary mit allen Wörtern wird festgelegt
vocab = {
    'key': 'Schlüssel',
    'door': 'Türe',
    'lock': 'Schloss',
    'dog': 'Hund',
    'cat': 'Katze'
}

# Die Englischen Wörter werden als Liste gespeichert.
en_words = list(vocab.keys())
# de_words = vocab.values()

cont = True

# In der while-Schleife fiindet das Abfragen der Wörter statt. 
while cont:

    # Eine Zufallsezahl wird gewählt
    rand_num = random.randint(0, len(en_words))
    # Damit wird ein Wort aus der Liste ausgewählt.
    word = en_words[rand_num]
    # User-INput wird als answer gespeichert.
    answer = input("Uebersetze: " + word)
    # Es wird kontrolliert, ob die Antwort richtig war.
    if answer == vocab[word]:
        print("Deine Antwort war richtig!")

    else:
        print("Falsch \nrichtige Antwort wäre " + vocab[word])

