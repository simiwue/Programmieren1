# ==================================================================================
# Palindrome is a number which reads the same from beginning and from end, e.g. 9009
# Find the largest palindrome made from a product of two 3-digit number.
# ==================================================================================


num1 = 999
num2 = 999
searching = True
largest = 0

while searching:
    product = num1 * num2
    if str(product) == str(product)[::-1]:
        # print(f'{product} = {num1} * {num2}')
        if product > largest:
            largest = product
    
    num1 -= 1

    if num1 <= 800:
        num2 -= 1
        num1 = 999

    if num2 <= 800:
        searching = False

print(largest)