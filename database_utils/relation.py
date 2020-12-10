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


if __name__ == '__main__':
    test = Relation('relation_input.txt')
    print(test)
