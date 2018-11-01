import random

def draw_board(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0).
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def input_player_letter():
    # Lets the player pick the letter they want.
    # Returns a list with the player's letter as the first item and computer's
    # letter second.

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want be X or O: ')
        letter = input().upper()

    # The first elemnt in teh list is player's letter, 
    # the second is the computers.

    if letter == 'X':
        return ['X', 'O']
    if letter == 'O':
        return ['O', 'X']

def first_move():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def player_moves(board, letter, move):
    board[move] = letter

def is_winner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use "bo" instead of "board" and "le" instead of "letter" so wedon't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # Across the top
        (bo[4] == le and bo[5] == le and bo[6] == le) or # Across the middle
        (bo[1] == le and bo[2] == le and bo[3] == le) or # Across the bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or # Down the left side
        (bo[8] == le and bo[5] == le and bo[2] == le) or # Down the middle
        (bo[9] == le and bo[6] == le and bo[3] == le) or # Down the right side
        (bo[7] == le and bo[5] == le and bo[3] == le) or # Diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le)) # Diagonal

def get_board_copy(board):
    # make a copy of the board list and return it.
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy