import sys
import os
#from tests import *

def readFile(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            row = list(line.strip())
            lines.append(row)

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
    return score

def checkFours(board, player):

    score = 0
    #check for row of 4
    for row in board:
        if all(cell == player for cell in row):
            score += 6
   
    #check for column of 4
    for col in range(4):
        if all(board[row][col] == player for row in range(4)):
            score += 6

    return score

def checkThrees(board, player):

    score = 0
    #check for 3s horizontally 
    for row in board:
        if all(cell == player for cell in row): 
            continue
        thwee = player*3
        if thwee in ''.join(row):
            score += 3

    #check for 3s vertically
    scoreCols = []
    for col in range(4):
        if all(board[row][col] == player for row in range(4)):
            continue
        thwee = player*3
        test = ''
        for row in range(4): 
            test += (board[row][col]) 
            if thwee in test and col not in scoreCols:
                score += 3
                scoreCols.append(col)
                continue

    #checking for the diagonals also includes checking the fours diagonals
    diaCords = [[(0,0), (1,1), (2,2), (3,3)],[(0,1), (1,2), (2,3)],
                [(1,0),(2,1), (3,2)],[(0,3), (1,2), (2,1), (3,0)],
                [(1,3),(2,2), (3,1)],[(0,2), (1,1), (2,0)]]
    
    threeDia = player*3
    fourDia = player*4

    for dia in diaCords:
        test = ''
        for row, col in dia:
            test += board[row][col] 
        if len(test) == 4:
           if fourDia in test:
            score += 6
           elif threeDia in test:
               score += 3
        elif threeDia in test:
            score += 3
    
    return score

def checkEdges(board, player):
    score = 0
    edges = [(0, 1), (0, 2), (0, 3), (1, 0), 
             (1, 3), (2, 0), (2, 3), (3, 1), 
             (3, 2), (3, 3), (0, 0), (3, 0)]
    
    for row, col in edges:
        if (board[row][col] == player):
            score += 1
    return score


def evaluate_position(board, player):

    Pscore = 0
    Oscore = 0
    player_mark = ' '
    O_mark = ' '
    if player == -1:
        player_mark = 'X'
        O_mark = 'O'
    elif player == 1:
        player_mark = 'O'
        O_mark = 'X'

    Pscore += checkFours(board, player_mark)
    Pscore += checkThrees(board, player_mark)
    Pscore += checkEdges(board, player_mark)
    
    Oscore += checkFours(board, O_mark)
    Oscore += checkThrees(board, O_mark)
    Oscore += checkEdges(board, O_mark)
    return Pscore-Oscore
    
def generate_moves(board):
    moves = []
    for row in range(4):
        for col in range(4):
            if board[row][col] == '.':
                moves.append((row, col))  
    return moves

def make_move(board, move, player):
    row = move[0]
    col = move[1]
    if board[row][col] == '.':
        if player == -1:
            board[row][col] = 'X'
        if player == 1:
            board[row][col] = 'O'

        return True  
    else:
        return False  

def undo_move(board, move):
    row = move[0]
    col = move[1]
    board[row][col] = '.'  


def negamax(board, player):
    if gameOver(board):
        return evaluate_position(board,player)

    best_value = -float('inf')
    for move in generate_moves(board):
        make_move(board, move, player)
        value = -negamax(board, -player)
        undo_move(board, move)
        best_value = max(best_value, value)

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
        board = readFile(sys.argv[1])
        pop = gamePop(board)

    player = 0
    if (pop[0] > pop[1]):
        player = 1
        player_mark = 'O'
    elif (pop[0] < pop[1]):
        player = -1
        player_mark = 'X'
    else:
        player_mark = 'X'
        player = -1

    #-1 is X
    #1 is O
    s = evaluate_position(board, player)

    moves = negamax(board, player)

    print(player_mark, moves)
    

if __name__ == '__main__':
    main()

