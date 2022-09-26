from unittest import case
from Sudoku import Sudoku

def printMenu():
    print(' ' + 79*'-' + ' ')
    for i in range(4):
        if(i == 1):
            print('|' + 25*' ' + 'Welcome to Sudoku Solver :)' + 27*' ' + '|')
            continue
        if(i == 2):
            print('|' + 15*' ' + 'Please, select an option from the menu below' + 20*' ' + '|')
            continue
        print('|' + 79*' ' + '|')
    print(' ' + 79*'-' + ' ')
    print()
    print("1 - Generate a Random 9x9 Sudoku")
    print("   0: Easy Level Sudoku")
    print("   1: Medium Level Sudoku")
    print("   2: Hard Level Sudoku")
    print("2 - Enter your own 9x9 Sudoku")
    game_option = input('Select your game choice: ')
    if(game_option == '1'):
        dif_level = input('Choose the difficulty level: ')
        if(dif_level == '0' or dif_level == '1' or dif_level == '2'):
            readChoice(game_option, dif_level)
    elif(game_option=='2'):
        readChoice(game_option)
    else: 
        print()
        print('Invalid choice, read the menu and try again.')
        printMenu()
        

def readChoice(game_option, dif_level=1):
    if(game_option == '1'):
        question_board_code = board.generateQuestionSudokuCode(int(dif_level)) # generates a medium level sudoku
        print()
        print('Generating...')
        print()
        print("Randomly generated Sudoku for level " + dif_level + ": ")
        print(question_board_code[0])
        print()
        print(81*'-')
        print()

        print("Solving...")
        print()
        print("Solution for Random Sudoku: ")
        solved_board_code = Sudoku(question_board_code[0]).solveSudoku()
        print(solved_board_code)
        print()
        print(81*'-')
        print()
    else:
        code = input('Type your 9x9 Sudoku: ')
        print()
        print(81*'-')
        print()
        print('Solution for input Sudoku: ')
        solved_board_code = Sudoku(code).solveSudokuForCode() # solves a hard level sudoku
        print(solved_board_code)

if __name__ == '__main__':
    board = Sudoku()

    printMenu()