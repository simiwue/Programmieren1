import random

pc_score = 0
user_score = 0






# Values for rand_num:
# 0 -> rock
# 1 -> paper
# 2 -> scissors

while pc_score < 3 and user_score < 3:

    user_choice = input('rock, paper or scissors').lower()
    rand_num = random.randrange(0,3)

    if user_choice == 'rock':
        if rand_num == 0:
            print("It's a tie!")

        elif rand_num == 1:
            pc_score += 1
            print("You loose :-(")
        
        elif rand_num == 2:
            user_score += 1
            print("You win :-)")


    elif user_choice == 'paper':
        if rand_num == 0:
            user_score += 1
            print("You win :-)")

        elif rand_num == 1:
            print("It's a tie!")
        
        elif rand_num == 2:
            pc_score += 1
            print("You loose :-(")


    elif user_choice == 'scissors':
        if rand_num == 0:
            pc_score += 1
            print("You loose :-(")

        elif rand_num == 1:
            user_score += 1
            print("You win :-)")
        
        elif rand_num == 2:
            print("It's a tie!")



    else:
        print('Your selection is invalid. \nTry again.')


    if user_score < 3 and pc_score < 3:
        print("You: " + str(user_score), "PC: " + str(pc_score))


if pc_score > 2:
    print("You loose! \nPC: " + str(pc_score) + "\nYou: " + str(user_score))

elif user_score > 2:
    print("You win! \nPC: " + str(pc_score) + "\nYou: " + str(user_score))

