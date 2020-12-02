from timeit import timeit
import random

# Change the below value to 'hard' once your easy tests pass.
TEST_MODE = 'easy'

CHARACTERS = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4',
              '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
              'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^',
              '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
              't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']


def longest_substring(s: str) -> int:
    """
    Returns the length of the longest substring in <s> without repeating characters.

    Example: if <s> is 'CSC108', then the longest substring without repeating
    characters would be 'SC108', so the function should return 5.

    Another example:
    'Piazza' would return 4, from the 'Piaz'.

    Hint: try to implement this with a dictionary. Consider mapping characters to their
    indexes as you loop through the string, and seeing what you could do with that data.

    >>> longest_substring('aab')
    2
    >>> longest_substring('abcabcbb')
    3
    >>> longest_substring('tmmzuxt')
    5
    >>> longest_substring('')
    0
    >>> longest_substring('hhm, I wonder what the longest substring in this sentence is?')
    10
    """
    # TODO implement the function here
    pass


def solution(s: str) -> int:
    """
    A solution that is fast, but does not use dictionaries.
    An implementation that uses dictionaries could be up to 40% faster.
    (Don't copy this! Come up with a solution of your own!)
    """
    longest = 0
    sub = ''
    for char in s:
        if char not in sub:
            sub = sub + char
        else:
            sub = sub[sub.index(char) + 1:] + char
        if len(sub) > longest:
            longest = len(sub)
    return longest


def _check() -> bool:
    """
    Checks the user implementation for correctness.
    """
    from string import ascii_lowercase
    for _ in range(5):
        random_string = ''.join(random.choice(ascii_lowercase) for _ in range(50))
        student = longest_substring(random_string)
        sol = solution(random_string)
        if student != sol:
            print(f'Your solution is incorrect, when run on the following string:\n\n'
                  f'{random_string}\n\n'
                  f'Your solution returned {student} when it should return {sol}.')
            return False
    return True


if __name__ == '__main__':
    SIZE1 = [i for i in range(100, 600, 100)]
    SIZE2 = [i for i in range(1000000, 6000000, 1000000)]
    tests = SIZE1 if TEST_MODE == 'easy' else SIZE2

    test_string = str()
    reps = 1
    if _check():
        print('Your solution is correct :)\n')
        print(f'Test mode: {"easy" if TEST_MODE == "easy" else "hard"}')
        student_times = []
        solution_times = []
        for size in tests:
            test_string += ''.join(random.choice(CHARACTERS) for _ in range(size - len(test_string)))
            time = timeit('longest_substring(test_string)', number=reps, globals=globals())
            time1 = timeit('solution(test_string)', number=reps, globals=globals())
            student_times.append(time)
            solution_times.append(time1)
            print(
                f'Input string length: {size:,}\nNumber of repetitions: {reps:,}\n'
                f'Time for your method: {time}\nTime for solution: {time1}\n')
        time_diff = sum(student_times) - sum(solution_times)
        percentage_diff = (time_diff * 100) / sum(solution_times)
        if time_diff > 0:
            print(f'Your solution was {percentage_diff:.2f}% '
                  f'slower than an "optimal" solution.')
            if percentage_diff < 100:
                print('However, it is pretty fast, and almost certainly an O(n) solution. Great job!')
        else:
            print(f'Congratulations! '
                  f'Your solution was {-percentage_diff:.2f}% '
                  f'faster than the given solution.')
