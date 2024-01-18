number = input("Write a big number")

def sum_of_digits(num):
    summ = 0
    for digit in num:
        summ += int(digit)

    return summ

print(sum_of_digits(number))