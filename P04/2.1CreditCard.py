card_number = "9384 3405 3297 1129"

# Funktion, welche die Checks durchführt
def check(card_num):

    # Abstände werden gelöscht (mit nichts ersetzt)
    number = card_num.replace(" ", "")
    checksum = 0

    # Für jede Ziffer wird gecheckt
    for digit in number:
        # Ist es eine Zahl oder nicht
        if digit.isdigit() == True:
            # wird der Kontrollsumme dazugerechnet
            checksum += int(digit)
        else:
            return("Your card is invalid!")
    
    # Kontrolle, ob die Kontrollesumme durch 10 teilbar ist
    if checksum%10 == 0:
        return("Your card is valid")
    else:
        return("Your card is invalid, checksum failed")


print(check(card_number))