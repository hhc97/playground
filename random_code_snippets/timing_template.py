"""
A template for easy timing of different functions.
"""


def func1():
    pass


def func2():
    pass


if __name__ == '__main__':
    from timeit import timeit

    reps = 1
    func1_name = 'func1'
    func2_name = 'func2'

    time1 = timeit('func1()', number=reps, globals=globals())
    time2 = timeit('func2()', number=reps, globals=globals())

    print(f'Value of {func1_name}/{func2_name}: {time1 / time2:.4f}')
    print(f'Time for {func1_name}: {time1}\nTime for {func2_name}: {time2}')
