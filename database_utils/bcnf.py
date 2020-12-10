from __future__ import annotations

from fd import FD
from relation import Relation


def bcnf(rel: Relation) -> list:
    for fd in rel.fds:
        if rel.closure(fd) != rel.relation:
            pass
    return [rel]


if __name__ == '__main__':
    relation = Relation('relation_input.txt')
    print(relation)
    print(relation.get_closures())
    test = bcnf(relation)
