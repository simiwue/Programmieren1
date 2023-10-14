card_number = "9384 3495 3297 1123"

# print(card_number.isdigit())

def check(card_num):
    
    # Nummer wird beim Leerschlag geschnitten und in 4 Teilen als LISTE gespeichert
    parts = card_num.split(" ")

    checksum = 0

    for part in parts:
        valid = True
        #besteht jeder Teil nur aus Zahlen
        if part.isdigit() == False:
            valid = False

        # rechnet jede Zahl zur checksum
        for digit in part:
            checksum += int(digit)
    
    # Kontrolliert, ob die checksum mit 10 teilbar ist
    if checksum%10 != 0:
        valid = False


    return(valid)


valid = check(card_number)

if valid:
    print("Your Card is valid!")

else:
    print("Your card is invalid!")