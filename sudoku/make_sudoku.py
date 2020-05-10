# from puzzle_tools import *
from sudoku_solver import *
from time import time
from re import sub


def is_valid_grid(lst: list, symbol_set: set) -> bool:
    """returns True if this is a valid Sudoku grid"""
    return not any([lst[r].count(sym) > 1 or
                    [row[c] for row in lst].count(sym) > 1
                    or _sbsq_lst(r, c, lst).count(sym) > 1
                    for r in range(len(lst)) for c in range(len(lst[r]))
                    for sym in symbol_set])


def _sbsq_lst(r: int, c: int, symbols: list) -> list:
    # returns the list of symbols in the subsquare containing [r][c]
    ss = round(len(symbols) ** (1 / 2))
    return [symbols[(r//ss)*ss + i][(c//ss)*ss + j]
            for i in range(ss) for j in range(ss)]


def make_9x9_sudoku_puzzle() -> SudokuPuzzle:
    """takes user input and returns a SudokuPuzzle object"""
    symbol_set = {str(i) for i in range(1, 10)}
    symbols = [[n for n in sub('[^1-9]', '*',
                input(f'Please type in row {r}:')[:9].ljust(9, '*'))]
               for r in range(1, 10)]
    if is_valid_grid(symbols, symbol_set):
        print(f'\npuzzle = SudokuPuzzle(9, {symbols}, {symbol_set})')
        return SudokuPuzzle(9, symbols, symbol_set)
    else:
        print(SudokuPuzzle(9, symbols, symbol_set))
        print('Invalid grid entered, please retry.')
        return make_9x9_sudoku_puzzle()


if __name__ == '__main__':
    a = make_9x9_sudoku_puzzle()
    print(f'\nInput puzzle:\n{a}\nSolving...')
    time1 = time()
    sol = depth_first_solve(a)
    time2 = time()
    if sol:
        print('\nSolved!\n\nSolution:')
        # while sol.children:
        #     sol = sol.children[0]
        # print(sol.puzzle)
        print(sol)
        print(f'\nSolved in {time2 - time1} seconds.')
    else:
        print('No solution found :(')
