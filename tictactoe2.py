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

def make_move(board, letter, move):
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

def is_space_open(board, move):
    # Return True if the players space is open on the board
    return board[move] == ' '

def get_player_move():
    # Lets player enter move
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_open(board, int(move)):
        print("What is your next move? (1-9) ")
        move = input()
    return int(move)

def choose_random_move(board, moves_list):
    #Returns fal move from the passed list on the passed board.
    #Returns None if not valid moves.
    possible_moves = []
    for i in moves_list:
        if is_space_open(board, i):
            possible_moves.append(i)
    
    if len(possible_moves) !=0:
        return random.choice(possible_moves)
    else:
        return None
    
def get_computer_move(board, computer_letter):
    # fived and board and the computer's leter, determine move, and return.
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # AI Algorithm for game
    # first check if we can win in the next move.
    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if is_space_open(board_copy, i):
            make_move(board_copy, computer_letter)
            if is_winner(board_copy, computer_letter):
                return i

    # move to corner if they are free
    move = choose_random_move(board, [2, 4, 7, 9])
    if move != None:
        return move

    # take center if free
    if is_space_open(board, 5):
        return 5
    
    # move to one of the sides
    return choose_random_move(board, [2, 4, 6, 8])

def is_board_full(board):
    # retrun True if every space on the board is taken, else return false
    for i in range(1, 10):
        if is_space_open(board, i):
            return False
    return True

print('Welcome to Tic-Tac-Toe!')

