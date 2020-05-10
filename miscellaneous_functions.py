"""
A place to keep random functions.
"""


def spongebob_case(s: str) -> str:
    """
    mAkEs tExT LiKe tHiS
    """
    lst = [ch for ch in s]
    for i in range(len(lst)):
        char = lst[i]
        if i % 2 == 0:
            lst[i] = char.lower()
        else:
            lst[i] = char.upper()
    return ''.join(lst)
