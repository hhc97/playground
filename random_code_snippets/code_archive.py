BOX_CHAR = '#'
OBSTACLE_CHAR = '*'
EMPTY_CHAR = '.'


def get_box_locations(board: list) -> list:
    return [(row, col) for row in range(len(board))
            for col in range(len(board[0])) if board[row][col] == BOX_CHAR]


def fallAndCrush2(board: list) -> list:
    row_max, col_max = len(board) - 1, len(board[0]) - 1
    box_locations = get_box_locations(board)

    not_done = True
    while not_done:
        explosions = []
        for row, col in box_locations[::-1]:
            # no move condition
            new_row = row + 1
            if row == row_max or board[new_row][col] == BOX_CHAR:
                continue
            fall_position = board[new_row][col]
            if fall_position == OBSTACLE_CHAR:
                explosions.append((new_row, col))
            else:
                board[new_row][col] = BOX_CHAR
            board[row][col] = EMPTY_CHAR
        for row, col in explosions:
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if i >= 0 and j >= 0:
                        try:
                            if board[i][j] == BOX_CHAR:
                                board[i][j] = EMPTY_CHAR
                        except IndexError:
                            pass
        new_box_locations = get_box_locations(board)
        if new_box_locations == box_locations:
            not_done = False
        box_locations = new_box_locations
    return board


def pretty(list):
    for row in list:
        print(row)
    print()


test1 = [['#', '.', '#', '#', '*'],
         ['#', '.', '.', '#', '#'],
         ['.', '#', '.', '#', '.'],
         ['.', '.', '#', '.', '#'],
         ['#', '*', '.', '.', '.'],
         ['.', '.', '*', '#', '.']]

test2 = [['#', '#', '*'],
         ['#', '.', '*'],
         ['#', '.', '*'],
         ['.', '#', '#'],
         ['*', '.', '#'],
         ['*', '.', '.'],
         ['*', '.', '.']]

test3 = [['#', '.', '#', '#', '*'],
         ['#', '.', '.', '#', '#'],
         ['.', '#', '.', '#', '.'],
         ['.', '.', '#', '.', '#'],
         ['#', '*', '.', '.', '.'],
         ['.', '.', '*', '#', '.']]

# thing = [['.'] * 5 for _ in range(6)]
# print(thing)

pretty(fallAndCrush2(test1))
pretty(fallAndCrush2(test2))
pretty(fallAndCrush2(test3))

bubble1 = [[3, 2, 4, 4],
           [3, 1, 2, 1],
           [1, 1, 1, 4],
           [3, 1, 2, 2],
           [3, 3, 3, 4]], [[3, 2], [5, 1], [4, 3], [3, 2]]


def bubblesPopping(bubbles: list, operations: list):
    row_max, col_max = len(bubbles) - 1, len(bubbles[0]) - 1
    for row, col in operations:
        row -= 1
        col -= 1
        curr_color = bubbles[row][col]
        if curr_color == 0:
            continue
        to_pop = []
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if i >= 0 and j >= 0 and (i == row or j == col):
                    try:
                        if bubbles[i][j] == curr_color:
                            to_pop.append([i, j])
                    except IndexError:
                        pass
        if len(to_pop) > 2:
            for r, c in to_pop:
                bubbles[r][c] = 0
        bubble_locations = [(row, col) for row in range(len(bubbles))
                            for col in range(len(bubbles[0])) if bubbles[row][col] != 0]
        for row, col in bubble_locations[::-1]:
            bubble_color = bubbles[row][col]
            new_row = row
            while new_row + 1 <= row_max and bubbles[new_row + 1][col] == 0:
                new_row += 1
            if new_row != row:
                bubbles[new_row][col] = bubble_color
                bubbles[row][col] = 0
    return bubbles


pretty(bubblesPopping(*bubble1))


def outage_interval(trade_data: list) -> str:
    trade_data.sort()
    for i in range(len(trade_data) - 1):
        trade1, trade2 = trade_data[i], trade_data[i + 1]
        trade1second = int(trade1[6:8])
        trade2second = int(trade2[6:8])
        if trade1second == 59 and trade2second == 0:
            continue
        if trade2second - trade1second > 1 or trade2second < trade1second:
            return f'{trade1}-{trade2}'
    return ''


print(outage_interval(
    ['12:31:04.04', '12:31:05.01', '12:31:06.21', '12:31:14.39', '12:31:15.13', '12:31:16.98', '12:31:17.09']))

from datetime import datetime


class Trader:
    def __init__(self):
        self.akuna = []
        self.exchange = []

    def process(self, line: str):
        entity, stock, number, when = line.split(',')
        value = stock, number, when
        if entity == "EXCHANGE":
            self.exchange.append(value)
        else:
            self.akuna.append(value)

    def reconciliate(self):
        self.akuna.sort(key=lambda x: x[-1], reverse=True)
        self.exchange.sort(key=lambda x: x[-1])
        found = False
        while self.akuna:
            curr = self.akuna.pop()
            a_time = datetime.strptime(curr[-1], '%H:%M:%S')
            for thing in self.exchange:
                b_time = datetime.strptime(thing[-1], '%H:%M:%S')
                time_diff = abs((b_time - a_time).seconds)
                if time_diff <= 300 and curr[0] == thing[0] and curr[1] == thing[1]:
                    self.exchange.remove(thing)
                    found = True
                    break
            if not found:
                return False
            found = False
        return True


def knapSack(W, wt, val):
    """
    :param W: capacity of knapsack
    :param wt: list containing weights
    :param val: list containing corresponding values
    :return: Integer
    """
    # code here
    dp_table = [[0 for _ in range(W + 1)] for _ in range(len(wt) + 1)]
    for i in range(1, len(dp_table)):
        for j in range(1, len(dp_table[0])):
            if wt[i - 1] <= j:
                dp_table[i][j] = max(val[i - 1] + dp_table[i - 1][j - wt[i - 1]], dp_table[i - 1][j])
            elif wt[i - 1] > j:
                dp_table[i][j] = dp_table[i - 1][j]

    return dp_table[-1][-1]


print(knapSack(15, [1, 2, 3], [1, 2, 3]))


def num_diffs(a, b):
    n = len(a)
    c = [0] * n

    for i in range(n):
        c[i] = a[i] + b[i]

    frequencies = dict()

    for i in range(n):
        if c[i] in frequencies.keys():
            frequencies[c[i]] += 1
        else:
            frequencies[c[i]] = 1

    totalPairs = 0

    for x in frequencies:
        y = frequencies[x]
        totalPairs = (totalPairs + y * (y - 1) // 2)

    return n + totalPairs


def min_keypad_count(text: str) -> int:
    freqs = {}
    for c in text:
        freqs[c] = freqs.get(c, 0) + 1
    freqs = list(freqs.items())
    freqs.sort(key=lambda x: x[1], reverse=True)
    counter = 0
    total = 0
    print(freqs)
    for k, f in freqs:
        cost = counter // 9 + 1
        total += cost * f
        counter += 1
    print(total)
    return total


min_keypad_count('abcghdiefjoba')
