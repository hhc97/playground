from __future__ import annotations

from fd import FD


class Relation:
    """
    A class that represents a relation and it's FDs.
    """

    def __init__(self, relation_file: str) -> None:
        """
        Parses the relation file to initialize the class properly.
        """
        self.fds = []
        with open(relation_file, 'r') as f:
            self.relation = set(f.readline().strip())
            for line in f:
                self.fds.append(FD(line))

    def __str__(self) -> str:
        """
        Returns the string representation of this relation.
        """
        rel = ''.join(sorted(list(self.relation)))
        fds = ', '.join(sorted(str(fd) for fd in self.fds))
        return f'Relation: {rel}\nFDs: {fds}'

    def closure(self, key: set) -> set:
        """
        Returns the closure of a FD.
        """
        closure = key.intersection(self.relation)
        running = True
        while running:
            running = False
            for fd in self.fds:
                deps = fd.dependents.intersection(self.relation)
                if fd.determinants.issubset(closure) and not deps.issubset(closure):
                    closure.update(deps)
                    running = True
        return closure

    def get_closures(self) -> str:
        """
        Gets the closures of all FDs in the relation.
        """
        closures = ['Closures:']
        for fd in self.fds:
            closures.append(f'{fd.get_determinants()}+ = '
                            f'{"".join(sorted(list(self.closure(fd.determinants))))}')
        return '\n'.join(closures)

    def get_fds_copy(self) -> list:
        """
        Returns a copy of the FDs in this relation.
        """
        return [fd.get_copy() for fd in self.fds]


if __name__ == '__main__':
    test = Relation('relation_input.txt')
    print(test)
    print()
    print(test.get_closures())
