"""
A short module that generates random memory access patterns.
"""

import random


def opt(ref_string: list):
    """
    Belady's algorithm for a memory size of 8.
    """
    cache = set()
    hit = 0
    miss = 0
    for i in range(len(ref_string)):
        pg = ref_string[i]
        if pg in cache:
            hit += 1
        else:
            miss += 1
            if len(cache) < 8:
                cache.add(pg)
            else:
                furthest = -1
                evict = ''
                for item in cache:
                    try:
                        index = ref_string.index(item, i + 1)
                        if index > furthest:
                            furthest = index
                            evict = item
                    except ValueError:
                        evict = item
                        break
                cache.remove(evict)
                cache.add(pg)
    print(f'Hit rate: {100 * hit / (hit + miss):.4f}%, Hits: {hit}, Misses: {miss}')
    return miss


if __name__ == '__main__':
    while 1:
        access = []
        for _ in range(50):
            page = random.randint(1, 9)
            access.append(f'L 10{page}000')
        if opt(access) > 11:
            print('\n'.join(access))
            break
