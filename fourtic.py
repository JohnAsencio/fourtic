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

    #check for diagonal of four
    if all(board[i][i] == player for i in range(4)) or all(board[i][3 - i] == player for i in range(4)):
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
    for col in range(4):
        column = [board[row][col] for row in range(4)]
        if column.count(player) == 4:
            continue  
        elif column.count(player) == 3:
            score += 3

    #check for 3s diagonally
    for i in range(1, 4):
        diagonal = [board[j][i + j] for j in range(4 - i)]
        if diagonal.count(player) == 4:
            continue 
        if diagonal.count(player) == 3:
            score += 3

    # Check the other diagonal (from top-right to bottom-left)
        other_diagonal = [board[j][3 - i - j] for j in range(4 - i)]
        if other_diagonal.count(player) == 4:
            continue
        if other_diagonal.count(player) == 3:
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
    print("Player", player_mark, "Score:", Pscore)
    
    Oscore += checkFours(board, O_mark)
    Oscore += checkThrees(board, O_mark)
    Oscore += checkEdges(board, O_mark)
    print("Opponent", O_mark, "Score:", Oscore)
    return abs(Pscore-Oscore)


    
def generate_moves(board):
    moves = []
    for row in range(4):
        for col in range(4):
            if board[row][col] == '.':
                moves.append((row, col))  
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
        print("CURRENT OPERATION")
        print(move)
        make_move(board, move, player)
        displayBoard(board)
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
        print("starting board")
        board = readFile(sys.argv[1])
        displayBoard(board)
        print("initial population")
        pop = gamePop(board)
        print(pop)

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
    #print("starting score", player, s)

    moves = negamax(board, player)

    print(player_mark, moves)
    

if __name__ == '__main__':
    main()

