import random

board = []
# Einstellungen für das Spiel
num_rows = 10
num_cols = 15
num_guess = 10

# Koordinaten vom Schiff werden zufällig gewählt
ship_x = random.randrange(num_cols)
ship_y = random.randrange(num_rows)
ship = [ship_x, ship_y]
# print(ship)

# Das Brett wird mit lauter o erstellt
for i in range(num_rows):
    row = ["o"] * num_cols
    board.append(row)
    i += 1


# Das Spiel beginnt
while num_guess > 0:

    valid = False
    while valid == False:
        # Der Spieler wähl x und y Koordinaten
        guess_x = int(input("Guess X of the ship. 1-" + str(num_cols)))-1
        guess_y = int(input("Guess Y of the ship. 1-" + str(num_rows)))-1
        
        # Es wird kontrolliert ob die Eingabe des Spielers korrekt ist
        if guess_x < num_cols and guess_x >= 0 and guess_y < num_rows and guess_y >= 0:
            valid = True
    # Guess wird aus den beiden gewählten Koordinaten gebildet       
    guess = [guess_x, guess_y]

    # Check ob Guess == Schiff ist
    if guess == ship:
        print("Harr!!! You killed the enemy ship!")

    else:
        board[guess_x][guess_y] = "x"
        print("You missed...")

    # Spieler hat nun einen Rateversuch weniger
    num_guess -= 1
   
   # aktuelles Brett wird geprintet
    for i in range(num_rows):
        print(board[i])
        i += 1