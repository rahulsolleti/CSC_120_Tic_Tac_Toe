import random

board = [['-','-','-'],['-','-','-'],['-','-','-']]


def fix_spot(row, col, player):
    if board[row][col] == '-':
        board[row][col] = player
        return True
    else:
        return False

def is_player_win( player):
    win = False
    n = 3

    # checking rows
    for i in range(n):
        win = True
        for j in range(n):
            if board[i][j] != player:
                win = False
                break
        if win:
            return win

    # checking columns
    for i in range(n):
        win = True
        for j in range(n):
            if board[j][i] != player:
                win = False
                break
        if win:
            return win

    # checking diagonals
    win = True
    for i in range(n):
        if board[i][i] != player:
            win = False
            break
    if win:
        return win

    win = True
    for i in range(n):
        if board[i][n - 1 - i] != player:
            win = False
            break
    if win:
        return win
    return False

def is_board_filled():
    for row in board:
        for item in row:
            if item == '-':
                return False
    return True

def swap_player_turn(player):
    return 'X' if player == 'O' else 'O'

def print_board():
    for row in board:
        for item in row:
            print(item, end=" ")
        print()

def start():

    player = 'X'

    while True:
        print(f"Player {player} turn")

        print_board()

        # taking user input
        row, col = list(
            map(int, input("Enter row and column numbers to fix spot: ").split()))
        print()

        # fixing the spot
        if not fix_spot(row - 1, col - 1, player):
            continue

        # checking whether current player is won or not
        if is_player_win(player):
            print(f"Player {player} wins the game!")
            break

        # checking whether the game is draw or not
        if is_board_filled():
            print("Match Draw!")
            break

        # swapping the turn
        player = swap_player_turn(player)

    # showing the final view of board
    print()
    print_board()


# starting the game
start()
