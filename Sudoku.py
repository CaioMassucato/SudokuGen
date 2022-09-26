import copy
import random
from utils import board

class Sudoku:
    def __init__(self, code=None):
        self.resetSudoku()

        if code:
            self.code = code

            for row in range(9):
                for col in range(9):
                    self.board[row][col] = int(code[0])
                    code = code[1:]
        else:
            self.code = None
    
    def resetSudoku(self): # resets the board to an empty state
        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        return self.board
    
    def boardToCode(self, input_board=None): # turn a pre-existing board into a code
        if input_board:
            _code = ''.join([str(i) for j in input_board for i in j])
            return _code
        else:
            self.code = ''.join([str(i) for j in self.board for i in j])
            return self.code
    
    def getEmptyNum(self): # finds the first empty space in the board, which is represented by a 0
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == 0:
                    return (row, col)

        return False
    
    def checkSpace(self, num, space): #checks to see if a number can be fitted into a specifc space; row, col
        if not self.board[space[0]][space[1]] == 0: # check to see if space is a number already
            return False

        for col in self.board[space[0]]: # check to see if number is already in row
            if col == num:
                return False

        for row in range(len(self.board)): # check to see if number is already in column
            if self.board[row][space[1]] == num:
                return False

        _internalBoxRow = space[0] // 3
        _internalBoxCol = space[1] // 3

        for i in range(3): # check to see if internal box already has number
            for j in range(3):
                if self.board[i + (_internalBoxRow * 3)][j + (_internalBoxCol * 3)] == num:
                    return False
        
        return True
    
    def solveSudoku(self): # solveSudokus a board using recursion
        _spacesAvailable = self.getEmptyNum()

        if not _spacesAvailable:
            return True
        else:
            row, col = _spacesAvailable

        for n in range(1, 10):
            if self.checkSpace(n, (row, col)):
                self.board[row][col] = n
                
                if self.solveSudoku():
                    return self.board

                self.board[row][col] = 0

        return False
    
    def solveSudokuForCode(self): # solveSudokus a board and returns the code of the solveSudokud board
        return self.boardToCode(self.solveSudoku())
    
    def generateRandSudoku(self): # generates a brand new completely random board full of numbers
        self.resetSudoku()

        line = list(range(1, 10))
        for row in range(3):
            for col in range(3):
                number = random.choice(line)
                self.board[row][col] = number
                line.remove(number)

        line = list(range(1, 10))
        for row in range(3, 6):
            for col in range(3, 6):
                number = random.choice(line)
                self.board[row][col] = number
                line.remove(number)

        line = list(range(1, 10))
        for row in range(6, 9):
            for col in range(6, 9):
                number = random.choice(line)
                self.board[row][col] = number
                line.remove(number)

        return self.createSudokuBoard()
    
    def createSudokuBoard(self): # uses recursion to finish generating a random board
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 0:
                    number = random.randint(1, 9)

                    if self.checkSpace(number, (row, col)):
                        self.board[row][col] = number

                        if self.solveSudoku():
                            self.createSudokuBoard()
                            return self.board

                        self.board[row][col] = 0

        return False
    
    def generateQuestionSudoku(self, fullSudoku, difficulty): # generates a question board with a certain number of cells removed depending on the chosen difficulty
        self.board = copy.deepcopy(fullSudoku)
        
        if difficulty == 0:
            _squares_to_remove = 30
        elif difficulty == 1:
            _squares_to_remove = 40
        elif difficulty == 2:
            _squares_to_remove = 60
        else:
            return

        count = 0
        while count < 4:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                count += 1

        count = 0
        while count < 4:
            row = random.randint(3, 5)
            col = random.randint(3, 5)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                count += 1

        count = 0
        while count < 4:
            row = random.randint(6, 8)
            col = random.randint(6, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                count += 1

        _squares_to_remove -= 12
        count = 0
        while count < _squares_to_remove:
            _row = random.randint(0, 8)
            _col = random.randint(0, 8)

            if self.board[_row][_col] != 0:
                n = self.board[_row][_col]
                self.board[_row][_col] = 0

                count += 1

        return self.board, fullSudoku
    
    def generateQuestionSudokuCode(self, difficulty): # generates a new random board and its board code depending on the difficulty
        self.board, _solution_board = self.generateQuestionSudoku(self.generateRandSudoku(), difficulty)
        return self.boardToCode(), self.boardToCode(_solution_board)