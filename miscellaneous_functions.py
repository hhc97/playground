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


def unix_symlink(target: str, dest: str) -> str:
    r"""
    Returns the unix command to create a symbolic link to <target> at <dest>.
    Use:
        unix_symlink(r'C:\Users\user\folder', r'/var/www/html/dest')
    Output:
        sudo ln -s /mnt/c/Users/user/folder /var/www/html/dest
    """
    target = '/mnt/c' + target[2:]
    return f'sudo ln -s {target} {dest}'.replace('\\', '/')
