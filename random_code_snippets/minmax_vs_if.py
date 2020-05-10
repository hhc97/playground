from timeit import timeit

x = 1
y = 2


def test_max(a, b):
    return max(a, b)


def test_if(a, b):
    if a > b:
        return a
    else:
        return b


max_time = timeit('test_max(x, y)', globals=globals())
if_time = timeit('test_if(x, y)', globals=globals())

print(f'Time taken for max comparison: {max_time}')
print(f'Time taken for if comparison: {if_time}')
print(f'Using max() is {max_time/if_time:.4f} times slower than using if.')
