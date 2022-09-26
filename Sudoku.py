import copy
import random

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

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
    
    def resetSudoku(self):
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
    
    def boardToCode(self, input_board=None):
        '''Transforms a board to a code format'''
        if input_board:
            _code = ''.join([str(i) for j in input_board for i in j])
            return _code
        else:
            self.code = ''.join([str(i) for j in self.board for i in j])
            return self.code
    
    def getEmptyNum(self):
        '''Get first empty spot on the board'''
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == 0:
                    return (row, col)

        return False
    
    def checkSpace(self, num, space):
        '''Checks if a number can be placed into a specifc row or col'''

        # checks if spot is a sudoku number
        if not self.board[space[0]][space[1]] == 0:
            return False

         # checks if number is in row
        for col in self.board[space[0]]:
            if col == num:
                return False

        # checks if number is in col
        for row in range(len(self.board)):
            if self.board[row][space[1]] == num:
                return False

        _internalBoxRow = space[0] // 3
        _internalBoxCol = space[1] // 3

        for i in range(3):
            for j in range(3):
                if self.board[i + (_internalBoxRow * 3)][j + (_internalBoxCol * 3)] == num:
                    return False
        
        return True
    
    def solveSudoku(self): 
        '''Recursively solves a Sudoku Board'''
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
    
    def solveSudokuToCode(self):
        '''Solves Sudoku and returns its code'''
        return self.boardToCode(self.solveSudoku())
    
    def generateRandSudoku(self):
        '''Generates a fully randomized board'''
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
    
    def createSudokuBoard(self):
        '''Uses recursion to finish generating the board'''
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
    
    def generateSudoku(self, fullSudoku, difficulty):
        '''Generates a board by removing a given number of cells based
            on the difficulty from the fully random generated board'''
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
    
    def generateSudokuCode(self, difficulty): # generates a new random board and its board code depending on the difficulty
        self.board, _solution_board = self.generateSudoku(self.generateRandSudoku(), difficulty)
        return self.boardToCode(), self.boardToCode(_solution_board)