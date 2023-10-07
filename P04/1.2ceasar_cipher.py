#======== ASCII-INFO ============

# a = 97, b= 98, ... z= 122

# from number to letter use chr()
# from letter to number use ord()

# ===============================



def encrypt(message):
    # wird später noch gebraucht, muss innerhalb der Funktion definiert werden
    new_message=""

    # Nachricht wird in Kleinbuchstaben geschrieben
    message = message.lower()

    # Für jeden Buchstaben der Nachricht wird dieser Code durchgegangen
    for letter in message:
        
        # Buchstabe zu ASCII-Nummer umgeformt
        letter = ord(letter)

        # Ist das Zeichen ein Buchstabe oder ein unbekanntes Symbol, z.B. Leerschlag oder ! ? 
        # Falls nicht wird das Zeichen im else-Block direkt übernommen
        if letter >= 97 and letter <= 122:
            
            # der Buchstaben wird um 3 verschoben
            new_letter = 97 + (letter - 97 - 3)%26

        else:
            new_letter = letter

        # Die Zahl des Zeichens wird nun wieder in ein Buchstabe übersetzt und zu einer Nachricht zusammengefügt
        new_letter = chr(new_letter)
        new_message += new_letter

    return(new_message)




def decrypt(message):
    # wird später noch gebraucht, muss innerhalb der Funktion definiert werden
    new_message=""

    # Nachricht wird in Kleinbuchstaben geschrieben
    message = message.lower()

    # Für jeden Buchstaben der Nachricht wird dieser Code durchgegangen
    for letter in message:
        
        # Buchstabe zu ASCII-Nummer umgeformt
        letter = ord(letter)

        # Ist das Zeichen ein Buchstabe oder ein unbekanntes Symbol, z.B. Leerschlag oder ! ? 
        # Falls nicht wird das Zeichen im else-Block direkt übernommen
        if letter >= 97 and letter <= 122:
            
            # der Buchstaben wird um 3 verschoben
            new_letter = 97 + (letter - 97 + 3)%26

        else:
            new_letter = letter

        # Die Zahl des Zeichens wird nun wieder in ein Buchstabe übersetzt und zu einer Nachricht zusammengefügt
        new_letter = chr(new_letter)
        new_message += new_letter

    return(new_message)


message = input("write a message")

direction = ""

while direction != "e" and direction != "d":
    direction = input('write "e" for encryption\n or "d" for decryption').lower()

if direction == "e":
    print(encrypt(message))

elif direction == "d":
    print(decrypt(message))

else:
    print("Sorry I'm confused")



# print(chr(ord("f")))
