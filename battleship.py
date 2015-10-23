from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print "You can play up to 4 times. Think wise!"
print_board(board)

def random_row(board):
    return randint(1, len(board))

def random_col(board):
    return randint(1, len(board[0]))

ship_row = random_row(board)
ship_col = random_col(board)
print "The battleship is here: ", ship_row, ship_col

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!


for turn in range(25):
    print "\nTurn", turn + 1
    print "Row and Column are from 1 to 5. Please input the right info."
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print "\nCongratulations! You sank my battleship!"
        break
    else:
        if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row-1][guess_col-1] == "X"):
            print "\nYou guessed that one already."
        else:
            print "\nResult: You missed my battleship!"
            print "Here is what you have guessed:"
            board[guess_row-1][guess_col-1] = "X"
            print_board(board)
    
    if turn == 24:
        print "\nYou have guessed for 4 times."
        print "Game Over"