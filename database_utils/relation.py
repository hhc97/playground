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

    def _closure(self, curr_fd: FD) -> str:
        """
        Returns the closure of a FD.
        """
        closure = curr_fd.determinants.copy()
        running = True
        while running:
            running = False
            for fd in self.fds:
                if fd.determinants.issubset(closure) and not fd.dependents.issubset(closure):
                    closure.update(fd.dependents)
                    running = True
        return ''.join(sorted(list(closure)))

    def get_closures(self) -> str:
        """
        Gets the closures of all FDs in the relation.
        """
        closures = ['Closures:']
        for fd in self.fds:
            closures.append(f'{fd.get_determinants()}+ = {self._closure(fd)}')
        return '\n'.join(closures)


if __name__ == '__main__':
    test = Relation('relation_input.txt')
    print(test)
    print()
    print(test.get_closures())
