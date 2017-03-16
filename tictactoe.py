# Tic Tac Toe from invent with python

import random

 def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
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

    def inputPlayerLetter():
        # Lets the player type which letter they want to be.
        # Returns a list with the player’s letter as the first item,
        # and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = input().upper()

            # the first element in the list is the player’s letter,
            # the second is the computer's letter.
            if letter == 'X':
                return ['X', 'O']
            else:
                return ['O', 'X']


def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

        return dupeBoard

    def isSpaceFree(board, move):
        # Return true if the passed move is free on the passed board.
        return board[move] == ' '

    def getPlayerMove(board):
        # Let the player type in their move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

    def chooseRandomMoveFromList(board, movesList):
        # Returns a valid move from the passed list on the passed board.
        # Returns None if there is no valid move.
        possibleMoves = []
        for i in movesList:
            if isSpaceFree(board, i):
                possibleMoves.append(i)

            if len(possibleMoves) != 0:
                return random.choice(possibleMoves)
            else:
                return None

    def getComputerMove(board, computerLetter):
        # Given a board and the computer's letter, determine where to move and return that move.
        if computerLetter == 'X':
            playerLetter = 'O'
        else:
            playerLetter = 'X'

        # Here is our algorithm for our Tic Tac Toe AI:
        # First, check if we can win in the next move
        for i in range(1, 10):
            copy = getBoardCopy(board)
            if isSpaceFree(copy, i):
                makeMove(copy, computerLetter, i)
                if isWinner(copy, computerLetter):
                    return i

112.     # Check if the player could win on their next move, and block them.
113.     for i in range(1, 10):
114.         copy = getBoardCopy(board)
115.         if isSpaceFree(copy, i):
116.             makeMove(copy, playerLetter, i)
117.             if isWinner(copy, playerLetter):
118.                 return i
119.
120.     # Try to take one of the corners, if they are free.
121.     move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
122.     if move != None:
123.         return move
124.
125.     # Try to take the center, if it is free.
126.     if isSpaceFree(board, 5):
127.         return 5
128.
129.     # Move on one of the sides.
130.     return chooseRandomMoveFromList(board, [2, 4, 6, 8])
131.
132. def isBoardFull(board):
133.     # Return True if every space on the board has been taken. Otherwise return False.
134.     for i in range(1, 10):
135.         if isSpaceFree(board, i):
136.             return False
137.     return True
138.
139.
140. print('Welcome to Tic Tac Toe!')
141.
142. while True:
143.     # Reset the board
144.     theBoard = [' '] * 10
145.     playerLetter, computerLetter = inputPlayerLetter()
146.     turn = whoGoesFirst()
147.     print('The ' + turn + ' will go first.')
148.     gameIsPlaying = True
149.
150.     while gameIsPlaying:
151.         if turn == 'player':
152.             # Player’s turn.
153.             drawBoard(theBoard)
154.             move = getPlayerMove(theBoard)
155.             makeMove(theBoard, playerLetter, move)
156.
157.             if isWinner(theBoard, playerLetter):
158.                 drawBoard(theBoard)
159.                 print('Hooray! You have won the game!')
160.                 gameIsPlaying = False
161.             else:
162.                 if isBoardFull(theBoard):
163.                     drawBoard(theBoard)
164.                     print('The game is a tie!')
165.                     break
166.                 else:
167.                     turn = 'computer'
168.
169.         else:
170.             # Computer’s turn.
171.             move = getComputerMove(theBoard, computerLetter)
172.             makeMove(theBoard, computerLetter, move)
173.
174.             if isWinner(theBoard, computerLetter):
175.                 drawBoard(theBoard)
176.                 print('The computer has beaten you! You lose.')
177.                 gameIsPlaying = False
178.             else:
179.                 if isBoardFull(theBoard):
180.                     drawBoard(theBoard)
181.                     print('The game is a tie!')
182.                     break
183.                 else:
184.                     turn = 'player'
185.
186.     if not playAgain():
187.         break
