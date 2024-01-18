morse_alphabet = {
 'A': ".- ",
 'B': "-... ",
 'C': "-.-. ",
 'D': "-.. ",
 'E': ". ",
 'F': "..-. ",
 'G': "--. ",
 'H': ".... ",
 'I': ".. ",
 'J': ".--- ",
 'K': "-.- ",
 'L': ".-.. ",
 'M': "-- ",
 'N': "-. ",
 'O': "--- ",
 'P': ".--. ",
 'Q': "--.- ",
 'R': ".-. ",
 'S': "... ",
 'T': "- ",
 'U': "..- ",
 'V': "...- ",
 'W': ".-- ",
 'X': "-..- ",
 'Y': "-.-- ",
 'Z': "--.. ",
 '0': "----- ",
 '1': ".---- ",
 '2': "..--- ",
 '3': "...-- ",
 '4': "....- ",
 '5': "..... ",
 '6': "-.... ",
 '7': "--... ",
 '8': "---.. ",
 '9': "----. ",
 }

text = input("Write somthing!")

morse_text = ""

for letter in text:
    symbol = morse_alphabet.get(letter.upper())
    morse_text += symbol

print(morse_text)