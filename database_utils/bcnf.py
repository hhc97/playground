from __future__ import annotations

from fd import FD
from relation import Relation


def get_r1_r2(rel: Relation, fd: FD) -> tuple:
    """
    Returns r1 and r2 according to BCNF decomposition.
    """
    r1 = rel.closure(fd)
    r2 = rel.relation - (r1 - set(fd.get_determinants()))
    return r1, r2


def bcnf(rel: Relation) -> list:
    for fd in rel.fds:
        if rel.closure(fd) != rel.relation:
            print(get_r1_r2(rel, fd))
    return [rel]


if __name__ == '__main__':
    relation = Relation('relation_input.txt')
    print(relation)
    print(relation.get_closures())
    test = bcnf(relation)
