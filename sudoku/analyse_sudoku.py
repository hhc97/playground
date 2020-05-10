from sudoku_solver import *

c = SudokuPuzzle(9, [['8', '*', '*', '*', '*', '*', '*', '*', '*'],
                     ['*', '*', '3', '6', '*', '*', '*', '*', '*'],
                     ['*', '7', '*', '*', '9', '*', '2', '*', '*'],
                     ['*', '5', '*', '*', '*', '7', '*', '*', '*'],
                     ['*', '*', '*', '*', '4', '5', '7', '*', '*'],
                     ['*', '*', '*', '1', '*', '*', '*', '3', '*'],
                     ['*', '*', '1', '*', '*', '*', '*', '6', '8'],
                     ['*', '*', '8', '5', '*', '*', '*', '1', '*'],
                     ['*', '9', '*', '*', '*', '*', '4', '*', '*']],
                 {'6', '9', '4', '7', '2', '1', '3', '8', '5'})


def analyse(s):
    s._populate_set_map()
    min_map = 9
    min_set_map = 9
    print('Naked positions:')
    for key, value in s._map.items():
        print(key, sorted(value))
        if len(value) < min_map:
            min_map = len(value)
    print('Hidden positions:')
    for key, value in s._set_map.items():
        print(key)
        for k, v in sorted(value.items()):
            print(k, sorted(v))
            if len(v) < min_set_map:
                min_set_map = len(v)
    print(f'\nSmallest naked branching factor: {min_map}')
    print(f'Smallest hidden branching factor: {min_set_map}')
    return min(min_map, min_set_map)


def main():
    p = make_9x9_sudoku_puzzle()
    analyse(c)


if __name__ == '__main__':
    main()
