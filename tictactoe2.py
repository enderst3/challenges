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

def moves(board, letter, move):
    board[move] = letter



