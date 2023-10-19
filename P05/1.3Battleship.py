import random

board = []
num_rows = 10
num_cols = 15
num_guess = 10

ship_x = random.randrange(num_cols)
ship_y = random.randrange(num_rows)
ship = [ship_x, ship_y]
print(ship)

# fill board with o board is 
for i in range(num_rows):
    row = ["o"] * num_cols
    board.append(row)
    i += 1

while num_guess > 0:

    valid = False
    while valid == False:
        guess_x = int(input("Guess X of the ship. 1-" + str(num_cols)))-1
        guess_y = int(input("Guess Y of the ship. 1-" + str(num_rows)))-1
        
        if guess_x < num_cols and guess_x >= 0 and guess_y < num_rows and guess_y >= 0:
            valid = True


    guess = [guess_x, guess_y]

    if guess == ship:
        print("Harr!!! You killed the enemy ship!")

    else:
        board[guess_x][guess_y] = "x"
        print("You missed...")

    num_guess -= 1
   
    for i in range(num_rows):
        print(board[i])
        i += 1