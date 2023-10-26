import sys
import os
from tests import *

def readFile(file_path):
    lines = []
    with open(file_path, 'r') as file:
        #line = file.readline()
        for line in file:
            row = list(line.strip())
            lines.append(row)
            #lines.append(line.strip())
           # line = file.readline()
    return lines

def gameOver(board):
    for i in board:
        for j in i:
            if j == '.':
                return False
    return True

def gamePop(board):
    score = [0] * 2
    for i in board:
        for j in i:
            if j == 'X':
                score[0]+=1
            if j == 'O':
                score[1]+=1
    #print(score)
    return score
    
#def evalPos(board):
    #score[0] is the score for X
    #score[1] is the score for O
    #score = gameScore(board)
    #if score[0] > score[1]:
    #    return 1 #if X wins 1, if O wins -1
    #else:

def checkFours(board, player):

    score = 0

    #check for row of 4
    for row in board:
        if all(cell == player for cell in row):
            score += 4
    #check for column of 4

    #check for diagonal of four
    print("THIS IS THE SCORE ", score)
    return score

def checkThrees(board):
    return 1

def checkEdges(board):
    return 1


def evaluate_position(board, player):

    score = 0
    player_mark = ' '
    if player == -1:
        player_mark = 'X'
    elif player == 1:
        player_mark = 'O'

    score += checkFours(board, player_mark)
#    score += checkThrees(board)
 #   score += checkEdges(board)
    return score


    
def generate_moves(board):
    moves = []
    for row in range(4):
        for col in range(4):
            if board[row][col] == '.':
                moves.append((row, col))  # (row, col) represents the empty cell
   #print(moves)
    return moves

def make_move(board, move, player):
    row = move[0]
    col = move[1]
    if board[row][col] == '.':
        if player == -1:
            board[row][col] = 'X'
        if player == 1:
            board[row][col] = 'O'

        return True  # Move successfully made
    else:
        return False  # Move is invalid, as the cell is not empty

def undo_move(board, move):
    row = move[0]
    col = move[1]
    board[row][col] = '.'  # Clear the cell at the specified position


def negamax(board, player):
    if gameOver(board):
        return evaluate_position(board,player) 

    best_value = -float('inf')
    for move in generate_moves(board):
        print("CURRENT OPERATION")
        print(move)
        make_move(board, move, player)
        displayBoard(board)
        value = -negamax(board, -player)
        undo_move(board, move)
        best_value = max(best_value, value)
        print(best_value)

    return best_value


def main():
    if len(sys.argv) != 2:
        print("forgor the filename")
        sys.exit(1)

    board = readFile(sys.argv[1])
    if not board:
        print("File is not working")
        sys.exit(1)

    if board:
        print("starting board")
        board = readFile(sys.argv[1])
        displayBoard(board)
        print("initial population")
        pop = gamePop(board)

    player = 0
    if (pop[0] > pop[1]):
        player = 1
    elif (pop[0] < pop[1]):
        player = -1
    else:
        player = -1
    moves = negamax(board, player)

    print('O', moves)
    

if __name__ == '__main__':
    main()

