# =================================================
# Find the sum of all multiples of 3 & 5 below 1000
# =================================================

num = 0

sum = 0

while num < 1000:
    if num % 3 == 0 or num % 5 == 0:
        sum += num
    num += 1

print(sum)