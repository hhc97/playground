from time import time
from re import sub


class SudokuPuzzle:
    """
    A sudoku puzzle that may be solved, unsolved, or even unsolvable.
    """
    def __init__(self, n: int, symbols, symbol_set, grid_map=None):
        self._n, self._symbols, self._symbol_set = n, symbols, symbol_set
        if grid_map is None:
            self._map = {}
            self._populate_map()
        else:
            self._map = grid_map

    def _populate_map(self) -> None:
        # updates the grid map with allowed symbols for each position
        for r in range(len(self._symbols)):
            for c in range(len(self._symbols[r])):
                if self._symbols[r][c] == '*':
                    subset = self._row_set(r) | self._column_set(c) |\
                             self._subsquare_set(r, c)
                    allowed_symbols = self._symbol_set - subset
                    self._map[(r, c)] = allowed_symbols

    def __eq__(self, other) -> bool:
        return (type(other) == type(self) and
                self._n == other._n and self._symbols == other._symbols and
                self._symbol_set == other._symbol_set)

    def __str__(self) -> str:
        def row_pickets(row) -> str:
            string_list = []
            r = round(self._n ** (1 / 2))
            for i in range(self._n):
                if i > 0 and i % r == 0:
                    string_list.append("|")
                string_list.append(row[i])
            return "".join(string_list)
        s = ''
        num = round(self._n ** (1 / 2))
        div = '-' * num
        for _ in range(num - 1):
            div += '+' + '-' * num
        div += '\n'
        for i in range(len(self._symbols)):
            if i > 0 and i % num == 0:
                s += div
            s += row_pickets(self._symbols[i])
            s += "\n"
        return s.rstrip()

    def is_solved(self) -> bool:
        n, symbols = self._n, self._symbols
        return (not any("*" in row for row in symbols))\
            and all([(self._row_set(i) == self._symbol_set and
                      self._column_set(j) == self._symbol_set and
                      self._subsquare_set(i, j) ==
                      self._symbol_set) for i in range(n) for j in range(n)])

    def extensions(self):
        """
        returns a list of extensions with the position with the least number
        of possible values filled in
        """
        if not self._map:
            return []
        position, possible, lst = None, {i for i in range(10)}, []
        for pos, values in self._map.items():
            if len(values) < len(possible):
                possible = values
                position = pos
        for value in possible:
            new_map = self._map.copy()
            for key in self._get_positions(position):
                new_map[key] = {i for i in self._map[key] if i != value}
            del new_map[position]
            new_symbols = [row[:] for row in self._symbols]
            new_symbols[position[0]][position[1]] = value
            lst.append(SudokuPuzzle(self._n, new_symbols,
                                    self._symbol_set, new_map))
        return lst

    def _get_positions(self, pos: tuple):
        # returns the keys of sets in _map that may need to be altered
        n = round(self._n ** (1 / 2))
        return [key for key in self._map if key[0] == pos[0] or
                key[1] == pos[1] or (key[0]//n == pos[0]//n and
                                     key[1]//n == pos[1]//n)]

    def _row_set(self, r: int):
        return set(self._symbols[r])

    def _column_set(self, c: int):
        return set([row[c] for row in self._symbols])

    def _subsquare_set(self, r: int, c: int):
        n, symbols = self._n, self._symbols
        ss = round(n ** (1 / 2))
        ul_row, ul_col = (r // ss) * ss, (c // ss) * ss
        return {symbols[ul_row + i][ul_col + j] for i in range(ss)
                for j in range(ss)}


def depth_first_solve(puzzle):
    """an iterative depth first solve for Sudoku"""
    stack, seen, back = [puzzle], 0, 0
    while stack:
        seen += 1
        curr = stack.pop()
        if curr.is_solved():
            return curr, seen, back
        elif curr.extensions():
            stack.extend(curr.extensions())
        else:
            back += 1
    return None


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


def make_9x9_sudoku_puzzle():
    """takes user input and returns a SudokuPuzzle object"""
    symbol_set = {str(i) for i in range(1, 10)}
    symbols = [[n for n in sub('[^1-9]', '*',
                input(f'Please type in row {r}:')[:9].ljust(9, '*'))]
               for r in range(1, 10)]
    if is_valid_grid(symbols, symbol_set):
        print(f'\npuzzle = SudokuPuzzle(9, {symbols}, {symbol_set})')
        return SudokuPuzzle(9, symbols, symbol_set)
    else:
        raise ValueError('Invalid Sudoku grid entered.')


if __name__ == '__main__':
    a = make_9x9_sudoku_puzzle()
    print(f'\nInput puzzle:\n{a}\nSolving...')
    time1 = time()
    sol = depth_first_solve(a)
    time2 = time()
    if sol:
        sol, num_checked, num_backed = sol
        print('\nSolved!\n\nSolution:')
        print(sol)
        print(f'\nPuzzles checked: {num_checked}')
        print(f'Times backtracked: {num_backed}')
        print(f'Solved in {time2 - time1:.3f} seconds.')
    else:
        print('No solution found :(')
