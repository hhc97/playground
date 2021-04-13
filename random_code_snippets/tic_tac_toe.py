"""
A simple two player tic tac toe implementation.
"""


def check_won(state: list) -> str:
    """
    Checks if a player has won the game and returns the winning symbol.
    """
    if state[0][0] == state[1][1] == state[2][2] and state[0][0] != ' ':
        return state[0][0]
    if state[0][2] == state[1][1] == state[2][0] and state[0][2] != ' ':
        return state[0][2]
    for r in range(3):
        if state[r][0] == state[r][1] == state[r][2] and state[r][0] != ' ':
            return state[r][0]
    for c in range(3):
        if state[0][c] == state[1][c] == state[2][c] and state[0][c] != ' ':
            return state[0][c]
    return ''


def have_space(state: list) -> bool:
    """
    Returns whether there is still space on the board
    for a player to make a move.
    """
    return any(' ' in row for row in state)


def print_board(state: list) -> None:
    """
    Prints the board.
    """
    components = []
    for row in state:
        components.append(' ' + ' | '.join(row))
    print('\n' + '\n---+---+---\n'.join(components))


def play_game() -> None:
    """
    Starts a new game played via the command line.
    """
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    won = ''
    current_player = 'X'
    row_map = {0: 'left', 1: 'center', 2: 'right'}
    col_map = {0: 'top', 1: 'middle', 2: 'bottom'}
    print_board(board)
    while have_space(board) and not won:
        moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    moves.append((i, j))
        move_lines = []
        for i, move in enumerate(moves, 1):
            move_lines.append(f'{i}. {col_map[move[0]]}-{row_map[move[1]]}')
        prompt = '\n'.join(move_lines) + \
                 f'\nPlayer {current_player}, choose a move from the above moves: '
        player_move = int(input(prompt)) - 1
        row_index, col_index = moves[player_move]
        board[row_index][col_index] = current_player
        print_board(board)
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
        won = check_won(board)

    if won:
        print(f'Player {won} won!')
    else:
        print('Nobody won, it was a tie :(')


if __name__ == '__main__':
    play_game()
