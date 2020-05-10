def longest1(s: str):
    """
    returns the length of the longest substring in s without repeating characters
    >>> longest1('aab')
    2
    >>> longest1('abcabcbb')
    3
    >>> longest1('tmmzuxt')
    5
    >>> longest1('')
    0
    >>> longest1('hhm, I wonder what the longest substring in this sentence is?')
    10
    """
    tracker = {}
    longest = 0
    starting = 0
    for i, j in enumerate(s, 1):
        if j in tracker and tracker[j] > starting:
            starting = tracker[j]
        tracker[j] = i
        if i - starting > longest:
            longest = i - starting
    return longest


def longest3(s: str):
    """
    returns the length of the longest substring in s without repeating characters
    >>> longest3('aab')
    2
    >>> longest3('abcabcbb')
    3
    >>> longest3('tmmzuxt')
    5
    >>> longest3('')
    0
    >>> longest3('hhm, I wonder what the longest substring in this sentence is?')
    10
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


def longest2(s: str):
    """
    returns the length of the longest substring in s without repeating characters

    >>> longest2('aab')
    2
    >>> longest2('abcabcbb')
    3
    >>> longest2('tmmzuxt')
    5
    >>> longest2('')
    0
    >>> longest2('hhm, I wonder what the longest substring in this sentence is?')
    10
    """
    lst = []  # collection of all substrings
    lst2 = []  # all substrings that have unique characters
    for i in range(len(s) + 1):
        for j in range(i + 1, len(s) + 1):
            lst.append(s[i:j])
    for substring in lst:
        is_unique = True
        for letter in substring:
            if substring.count(letter) > 1:
                is_unique = False
        if is_unique:
            lst2.append(substring)
    return max(len(string) for string in lst2) if lst2 else 0


def longest4(s):
    """timing how long it takes to iterate through a string"""
    for char in s:
        assert char == char


SIZES = [2 ** i for i in range(21)]
SIZEs = [20, 40, 60, 80, 100, 120, 140, 160]
SIZE = [i for i in range(1000000, 6000000, 1000000)]

characters = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4',
              '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
              'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^',
              '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
              't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']

test = [i for i in range(2000)]

"""
for size in test:
    s = ''.join(random.choice(characters) for _ in range(size))
    a = longest1(s)
    b = longest3(s)
    print(a, b)
    if a != b:
        print('fail')
        break
    print(size, '\n')
print('finished')
"""

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    from timeit import timeit
    import random

    s = str()
    reps = 10
    for size in SIZE:
        s += ''.join(random.choice(characters) for _ in range(size - len(s)))
        time = timeit('longest1(s)', number=reps, globals=globals())
        time1 = timeit('longest3(s)', number=reps, globals=globals())
        print(f'Ratio = {time / time1}')
        print(
            f'Input string length: {size:,}\nNumber of repetitions: {reps:,}\n'
            f'Time for dictionary method: {time}\nTime for string method: {time1}\n')
        print(longest1(s), longest3(s))
