from __future__ import annotations

from fd import FD
from relation import Relation


def _split(rel: Relation, fd: FD) -> tuple:
    """
    Splits a relation on a FD according to BCNF.
    """
    r1 = rel.closure(fd.determinants)
    r2 = rel.relation - (r1 - fd.determinants)

    new_r1 = Relation()
    new_r1.relation = r1
    new_r1.fds = rel.get_fds_copy()

    new_r2 = Relation()
    new_r2.relation = r2
    new_r2.fds = rel.get_fds_copy()

    return new_r1, new_r2


def bcnf(rel: Relation) -> list:
    """
    Applies the BCNF algorithm to a relation and returns a list of relations.
    """
    for fd in rel.fds:
        if fd.determinants.issubset(rel.relation):
            closure = rel.closure(fd.determinants)
            if closure != rel.relation and closure != fd.determinants:
                print(f'Chosen FD: {fd}')
                left, right = _split(rel, fd)
                left = bcnf(left)
                right = bcnf(right)
                return left + right
    return [rel]


if __name__ == '__main__':
    relation = Relation('relation_input.txt')
    decomposed = bcnf(relation)
    print(f'\nFinal number of relations: {len(decomposed)}')
    for i, r in enumerate(decomposed, 1):
        print(i)
        print(r)
        print(r.get_closures())
        print()
