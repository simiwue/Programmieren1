import random

secret_num = random.randrange(1,11)

guess = 0

while guess != secret_num:

    guess = int(input("Make a guess. 1-10"))

    if guess < secret_num:
        print("higher")

    elif guess > secret_num:
        print("lower")


print("Hurray! You found my number it's the Number " + str(secret_num))