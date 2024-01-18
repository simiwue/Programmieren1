# ==========================================================
# Sum up all the even fibonacci numbers smaller then 4000000
# ==========================================================

num = 1
sum = 0
last_num = num

while num < 4000000:
    if num % 2 == 0:
        sum += num
    new_num = num + last_num
    last_num = num
    num = new_num

print(sum)