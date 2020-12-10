from __future__ import annotations


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

    def get_determinants(self) -> str:
        """
        Returns the determinants of this FD alphabetically.
        """
        return ''.join(sorted(list(self.determinants)))

    def get_dependents(self) -> str:
        """
        Returns the dependents of this FD alphabetically.
        """
        return ''.join(sorted(list(self.dependents)))

    def __str__(self) -> str:
        """
        Returns the string representation of this FD.
        """
        return f'{self.get_determinants()}->{self.get_dependents()}'

    def __eq__(self, other: FD) -> bool:
        """
        Compares if two FDs are equivalent.
        """
        dets = self.determinants == other.determinants
        deps = self.dependents == other.dependents
        return dets and deps


if __name__ == '__main__':
    test = FD(' AB -> CD ')
    print(test.determinants)
    print(test.dependents)
    print(test)
