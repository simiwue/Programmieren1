card_number = "9384 3405 3297 1129"


def check(card_num):
    number = card_num.replace(" ", "")
    checksum = 0

    for digit in number:
        if digit.isdigit() == True:
            checksum += int(digit)
        else:
            return("Your card is invalid!")
        
    if checksum%10 == 0:
        return("Your card is valid")
    else:
        return("Your card is invalid, checksum failed")


print(check(card_number))