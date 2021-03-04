#--Gobal VAriables
game_still_going = True
winner = None
current_player = "X"
#
#
#board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

#Display_Board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#paly game
def play_game():

    display_board()

    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()
        #flip to the player
        flip_player()
    if winner == "X" or winner == "O":
        print(winner + "Won.")
    elif winner == None:
        print("Tie.")

def handle_turn(player):

    print(player + "'S turn")
    position = input('Choose a position form 1-9: ')

    if position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Invalid input, choose a position from 1-9:")
    position = int(position) - 1

    board[position] = player
    display_board()



def check_if_game_over():
    check_if_winner()
    check_if_tie()

def check_if_winner():
    global winner
    row_winner = check_row()

    columns_winner = check_columns()

    diagonals_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif columns_winner:
        winner = columns_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None

def check_row():

    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
      game_still_going = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None


def check_columns():
    global game_still_going

    columns_1 = board[0] == board[3] == board[6] != "-"
    columns_2 = board[1] == board[4] == board[7] != "-"
    columns_3 = board[2] == board[5] == board[8] != "-"

    if columns_1 or columns_2 or columns_3:
        game_still_going = False
    if columns_1:
        return board[0]
    elif columns_2:
        return board[1]
    elif columns_3:
        return board[2]
    else:
        return None

def check_diagonals():
    global game_still_going

    diagonals_1 = board[0] == board[3] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"

    if diagonals_1 or diagonals_2:
        game_still_going = False
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    else:
        return None

def check_if_tie():
    global game_still_going

    if "-" not in board:
        game_still_going = False

    return


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
        return


    return

play_game()
#Add command
#Add hello