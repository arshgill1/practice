# board
# display board
# play game
# handle turn
# check win
    # chek rows
    # check columns
    # check diagonals
# check tie
# flip player


# -------Global Variables------

# Game Board
board=["-", "-", "-",
       "-", "-", "-",
       "-", "-", "-"]
# If game is still going
game_still_going = True

# Who win? or tie?
winner=None

#Whose turn it is
current_player="X"

# func to display the board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


    #Play a game of Tic Tac Toe
def play_game():
    #Display initial board
    display_board()
    #a loop to turn over and over again until someone wins or tie
    while game_still_going:

    #handle a single turn of an arbitrary player
        handle_turn(current_player)

    # Check if the game has ended
        check_if_game_over()

    #Flip to the other player
        flip_player()


    #If the game has ended
    if winner == "X" or winner == "O":
        print(winner + " Won.")
    elif winner == None:
        print("Tie")

# handle a single turn of arbitrary player
def handle_turn(player):
    #Notifying the player turn
    print(player + "'s Turn.")

    #Getting position from user
    position=input("Choose a position from 1-9: ")

    #Handling invalid input by user
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
          position=input("Choose a position from 1-9: ")

    #Assigning position to the board
        position = int(position) - 1

        if board[position] =="-":
            valid=True
        else:
            print("Position already occupied. Try another position.")


    board[position] = player

    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    # Set up Global variables
    global winner

    #check rows
    row_winner=check_rows()

    #check columns
    column_winner=check_columns()

    #check diagonals
    diagonal_winner=check_diagonals()
    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None
    return

def check_rows():
    #returns X or O (winner) and flags while loop that game is off

    # Set Global Variable
    global game_still_going

    #check if any of the rows have same values and is not empty
    row_1= board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    #If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going=False

    # Return the winner (X or O), if board 0 is X then X is winner and so for row 2 and row 3.
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]



    return

def check_columns():
    # Set Global Variable
    global game_still_going

    # check if any of the column have same values and is not empty
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # If any column does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False

    # Return the winner (X or O), if board 0 is X then X is winner and so for column 2 and column 3.
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    # Set Global Variable
    global game_still_going

    # check if any of the diagonal have same values and is not empty
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    # If any diagonal does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False

    # Return the winner (X or O), if board 0 is X then X is winner and so for diagonal 2.
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]

    return


def check_if_tie():
    # Global Variables
    global game_still_going
    # check if no one wins or all the spots are filled
    if "-" not in board:
        game_still_going=False
    return


def flip_player():

    # Global Variable
    global current_player

    #flip the current_player from X to O and vice versa
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return



play_game()
