import random


round = 0
tries_list = []

for round in range(0,10000):

    secret_num = random.randrange(1,11)
    tries = 1
    num_min = 1
    num_max = 11
    #first guess in a game
    guess = random.randrange(1,11)

    #make a guess until you know the secret number
    while guess != secret_num:

        tries += 1

        if guess < secret_num:
            higher = True
            num_min = guess + 1

        elif guess > secret_num:
            higher = False
            num_max = guess

        #make a new guess
        guess = random.randrange(num_min, num_max)

    #found the secret number
    tries_list.append(tries)
    average_tries = sum(tries_list) / len(tries_list)
    round += 1


print(average_tries)