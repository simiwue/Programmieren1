# Zufall importieren
import random
# Dictionary mit allen Wörtern wird festgelegt
vocab = {
    'key': ['Schlüssel', 'Taste'],
    'door': 'Türe',
    'lock': 'Schloss',
    'dog': 'Hund',
    'cat': 'Katze'
}

# Die Englischen Wörter werden als Liste gespeichert.
en_words = list(vocab.keys())
# de_words = vocab.values()


# Frage Wörter, solange die Liste Wörter enthält (zusätzlich eingebaut; nicht in Aufgabe verlangt)
while len(en_words)>0:
    
    # Eine Zufallsezahl wird gewählt
    rand_num = random.randint(0, len(en_words)-1)
    # Damit wird ein Wort aus der Liste ausgewählt.
    word = en_words[rand_num]
    # User-Input wird als answer gespeichert.
    answer = input("Uebersetze: " + word)
    # Es wird kontrolliert, ob die Antwort richtig war.
    if answer in vocab[word]:
        print("Deine Antwort war richtig!")
        # löscht das Wort aus der Liste, damit keine Wiederholung auftritt
        en_words.remove(word)

    else:
        # Kontrolliere, ob die Lösung eine Liste ist oder ein einzelnes Wort
        if isinstance(vocab[word], list):
            # Wenn es eine Liste ist, verbinde die einzelnen Lösungen mit " oder " zu einem schönen String
            solution = ' oder '.join(vocab[word])

        else:
            solution = str(vocab[word])
            
        print("Falsch! \nRichtige Antwort wäre: " + solution)


# Wird getriggert, wenn alle Wörter richtig beantwortet wurden und keine Wörter mehr in der Liste vorhanden sind
print("Glückwunsch du hast alle Wörter gewusst!")

