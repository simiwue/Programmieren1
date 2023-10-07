text = "am a person who is positive about every aspect of life. There are many things I like to do, to see, and to experience. I like to read, I like to write; I like to think, I like to dream; I like to talk, I like to listen. I like to see the sunrise in the morning, I like to see the moonlight at night; I like to feel the music flowing on my face, I like to smell the wind coming from the ocean. I like to look at the clouds in the sky"

#Funktion um aus einem Text eine Liste von Wörtern zu erstellen
def create_word_list(text):
    word_list = text.split(" ")
    return(word_list)



#Funktion um aus einem Text eine Liste von Sätzen zu erstellen
def create_sentence_list(text):
    sentence_list = text.split(".")

    # leere Schnipsel werden gelöscht
    try:
        sentence_list.remove('' and ' ')
    except ValueError:
        pass

    # Wenn ein Satz mit " " startet, lösche den Leerschlag
    i = 0
    for sentence in sentence_list:
        if sentence[0] == ' ':
            new_sentence = sentence[1:]
            sentence_list[i] = new_sentence

        i += 1

    return(sentence_list)



#Funktion um aus einem Text die durchscnittliche Anzahl Wörter zu bestimmen
def num_words_in_sentence(text):
    num_word_list = []

    #Erstelle eine Liste mit einzelnen Sätzen
    sentence_list = create_sentence_list(text)

    # Für jeden Satz in der Liste zähle die Wörter und füge sie in eine Liste num_words_list ein
    for sentence in sentence_list:
        word_list = create_word_list(sentence)
        num_words = len(word_list)
        num_word_list.append(num_words)
    
    # Berechne den Durschnitt und runde auf 2 Stellen
    average_words = sum(num_word_list) / len(num_word_list)
    average_words = round(average_words, 2)

    return(average_words)




# Funktion, die Anzahl "Ich, mein,..." zählt
def detect_pronouns(text):
    num_pronouns = 0

    # Erstelle eine Liste aller Wörter mit Hilfe der Funktion create_word_list (siehe oben)
    word_list = create_word_list(text)

    # Kontrolliere wie viele Wörter aus der Liste "i, me oder my" sind
    for word in word_list:
        word = word.lower()
        if word == "i" or word == "me" or word == "my":
            num_pronouns += 1

    return(num_pronouns)



        
# Rufe die Funktionen auf und speichere die Werte in Variablen
num_words = len(create_word_list(text))
num_sentences = len(create_sentence_list(text))
average_words = num_words_in_sentence(text)
num_pronouns = detect_pronouns(text)
percentage_pronouns = round(100*(num_pronouns/num_words), 2)



# Printe alle Infos in der Konsole ( \n -> neue Zeile )
print("Number of Words: " + str(num_words) + "\nNumber of sentences: " +  str(num_sentences) + "\nAverage words per sentence: " + str(average_words) + "\nNumber of frist-person pronouns: " + str(num_pronouns) + "\nPercentage of pronouns: " + str(percentage_pronouns) + "%")



# Gender Detector
if num_words > 30 or percentage_pronouns >  0.2:
    print("I think the text is written by a WOMAN.")

else:
    print("I think the text is written by a MAN")