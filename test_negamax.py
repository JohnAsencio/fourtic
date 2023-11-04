import unittest 
from fourtic import *

def displayBoard(board):
    for i in board:
        print(i)

class tests(unittest.TestCase):
    #this tests to see if the value matches for the 
    #cases that were giving me the most trouble
    def test_out(self):
        input_files = [("hw-fourtic/play-3.txt", "O -3"),
                       ("hw-fourtic/play-7.txt", "O -2"),
                       ("hw-fourtic/play-4.txt", "X 3"),
                       ("hw-fourtic/rand-5.txt", "O 0")]
        
        for input_file, expected_output in input_files:
            with open(input_file, 'r') as file:
               board = readFile(input_file)

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

            # Run the Negamax algorithm on the board
            result = negamax(board, player)

            # Format the result as a string in the same format as the expected output
            result_str = player_mark + f" {result}".replace(',', '') 

            # Assert that the algorithm's output matches the expected output
            self.assertEqual(result_str, expected_output)

if __name__ == '__main__':
    unittest.main()
