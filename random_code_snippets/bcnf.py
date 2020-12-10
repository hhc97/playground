class FD:
    """
    A class representing a functional dependency.
    """

    def __init__(self, fd: str) -> None:
        """
        Takes in a string in the form of 'A->B'.
        """
        attribs = [s.strip() for s in fd.split('->')]
        self.determinants = set(attribs[0])
        self.dependents = set(attribs[1])

    def __str__(self):
        """
        Returns the string representation of this FD.
        """
        dets = ''.join(sorted(list(self.determinants)))
        deps = ''.join(sorted(list(self.dependents)))
        return f'{dets}->{deps}'


if __name__ == '__main__':
    test = FD(' AB -> CD ')
    print(test.determinants)
    print(test.dependents)
    print(test)
