"""
=== CSC148 Summer 2024 - Test 2 Live Coding Task ===

The purpose of this component is to provide a more authentic evaluation that requires skills that employers
assess during coding interviews. As such, the marking scheme for this portion has not been publicized to mimic
the conditions of a real life interview.


=== Copyright Information ===
Prof. Marc De Benedetti, Department of Mathematical and Computational Sciences,
University of Toronto Mississauga, June 2024.

=== Module Description ===
The below module is a replica of a retro computer "math" game from Math Circus (~1994), where
the user was presented with some number of beakers needed to "fill", "empty", or "pour" various
beakers to obtain a certain amount of medicine for the circus elephant (I'm not sure why the elephant was sick...).

Portions of the implementation have been omitted intentionally for you to complete for this Coding Task.

During this task, students should start by spending some time familiarizing themselves with the code, docstrings,
methods, and game play.

Your Tasks:
    There are 2 (2) to-do's in code that require you to implement the provided methods according to the provided
    docstrings. One (1) of the to-do's is comprised of implementing "pour" - the last of the 3 possible moves
    (fill, empty, and pour). The second (and last) to-do requires you to implement a "hint" feature which tells
    the user what their next move should be to bring them one step closer to the quickest solution.



What to submit:
    beakergame.py to Midterm 2 - Coding Task on Quercus

Allowed aides:
    - Python
    - A python editor/IDE of the student's preference (but no additional auto-complete features)
    - Built-in python libraries
    - Any code/libraries provided in the zip file

Not permitted:
    - Use of the internet (except to download this zip file, and to upload your solutions to Quercus)
    - Communication with others (digital or otherwise)
    - Discussion boards (of any kind)
    - Everything else
"""
from __future__ import annotations
import random
from typing import Any, Optional


class Beaker:
    """A beaker to be used in the 1994 Math Circus Elephant Medicine
     measuring game.

    -- Attributes --
    capacity : int
       The maximum volume (mL) of liquid the beaker can hold
    volume : int
        The current volume of liquid the beaker is holding

    -- Representation Invariants --
        - A beaker's capacity is a non-negative integer
        - The volume is an integer 0 <= volume <= capacity
     """

    capacity: int
    volume: int

    def __init__(self, capacity: int, volume: int = 0) -> None:
        """Initialize a new Beaker with maximum volume <capacity>
        and initial <volume> mL of liquid, defaulting empty."""

        self.capacity = capacity
        self.volume = volume

    def __repr__(self):
        s = "Volume:\t" + str(self.volume) + "\n"
        s = s + "Capacity:\t" + str(self.capacity)

    def __eq__(self, other: Beaker) -> bool:
        """Return True iff the current volume and capacity
        of both beakers are the same."""

        return self.volume == other.volume and self.capacity == other.capacity

    def __hash__(self):
        return hash((self.volume, self.capacity))


class ElephantMedicineGame:
    """The Elephant Medicine Game is from Math Circus (1994),
     where some number (depending on the set difficulty level)
     of beakers, with varying amounts of medicine, are poured
     between each other to obtain a desired amount of medicine."""

    _target: int
    _beakers: list[Beaker]
    _moves: int
    _is_over: bool

    def __init__(self, level: int = 1):
        """Initialize the game with difficulty
        1 (default) to 5.

        Execute the play method to start game play. """

        if level == 5:
            beakers = 2
        elif level == 4:
            beakers = 3
        elif level == 3:
            beakers = 3
        elif level == 2:
            beakers = 4
        else:
            beakers = 5

        self._moves = 0
        self._is_over = False
        self._beakers = []
        self._curr_move = None
        self._prev_game = None

        capacities = [17, 11, 7, 4, 3]
        for b in range(beakers):
            self._beakers.append(Beaker(capacities.pop(random.randint(0, len(capacities) - 1))))

        target = random.randint(1, max(self._get_Capacities()))
        # ensure the target isn't exactly one of the capacities
        # if the level is greater than 1
        while level > 1 and target in self._get_Capacities():
            target = random.randint(1, max(self._get_Capacities()))
        self._target = target

    def __hash__(self):

        return hash(tuple([b for b in self._beakers]))

    def __repr__(self):

        s = f"Target:\t{self._target}\n"
        s += "Beakers:\n"
        capacities = "\t"
        volumes = "\t"
        names = "\t"
        for i in range(len(self._beakers)):
            names += f"Beaker {i + 1}\t"
            volumes += f"Amt: {self._beakers[i].volume} mL\t"
            capacities += f"Max: {self._beakers[i].capacity} mL\t"

        s += names + "\n" + volumes + '\n' + capacities

        return s

    def __eq__(self, other: ElephantMedicineGame) -> bool:
        """Return True iff the states of all the beakers
        between the two games are the same. Does not consider
        the number of moves in the equality."""

        if len(self._beakers) == len(other._beakers):
            for beaker in self._beakers:
                if beaker not in other._beakers:
                    return False
            return True
        return False

    def _get_Capacities(self) -> list[int]:
        """Return a list of capacities of the beakers in the game. """
        l = []
        for beaker in self._beakers:
            l.append(beaker.capacity)
        return l

    def copy(self) -> ElephantMedicineGame:
        """Copy <game> into a new instance. """
        game = ElephantMedicineGame()
        game._moves = self._moves
        game._target = self._target
        game._is_over = self._is_over

        game._beakers = []
        for beaker in self._beakers:
            game._beakers.append(Beaker(beaker.capacity, beaker.volume))

        return game

    def is_over(self) -> bool:
        """Return True iff one of the beakers in the game
        has the same volume as target."""

        return any([True for b in self._beakers if b.volume == self._target])

    def fill(self, b: int) -> None:
        """Fill beaker number <b>."""

        if 1 <= b <= len(self._beakers):
            self._beakers[b - 1].volume = self._beakers[b - 1].capacity

            self._moves += 1
            self._curr_move = f'fill {b}'

    def empty(self, b: int) -> None:
        """Drain/Empty beaker number <b> completely."""

        if 1 <= b <= len(self._beakers):
            self._beakers[b - 1].volume = 0

            self._moves += 1
            self._curr_move = f'empty {b}'

    def pour(self, _from: int, _to: int) -> None:
        """Pour as many of the contents of beaker <_from>
        into beaker <_to>, without over flowing. Any remaining
        liquid should remain in beaker <_from>."""

        # ToDo - implement the pouring of one beaker into another
        if 1 <= _from <= len(self._beakers) and 1 <= _to <= len(self._beakers):
            to_beaker = self._beakers[_to - 1]
            from_beaker = self._beakers[_from - 1]
            max_transfer = to_beaker.capacity - to_beaker.volume
            available_transfer = min(from_beaker.volume, max_transfer)
            to_beaker.volume += available_transfer
            from_beaker.volume -= available_transfer
            self._moves += 1
            self._curr_move = f'pour {_from} into {_to}'

    def _extensions(self) -> list[ElephantMedicineGame]:
        """
        this method generates all possible extensions of the current game
        """
        extensions = []
        for i in range(1, len(self._beakers) + 1):
            beaker1 = self._beakers[i - 1]
            beaker1_full = beaker1.capacity == beaker1.volume
            beaker1_empty = beaker1.volume == 0
            if not beaker1_full:
                fill_extension = self.copy()
                fill_extension.fill(i)
                fill_extension._prev_game = self
                extensions.append(fill_extension)

            if not beaker1_empty:
                empty_extension = self.copy()
                empty_extension.empty(i)
                empty_extension._prev_game = self
                extensions.append(empty_extension)

            for j in range(1, len(self._beakers) + 1):
                if i != j:
                    beaker2 = self._beakers[j - 1]
                    beaker2_full = beaker2.capacity == beaker2.volume
                    beaker2_empty = beaker2.volume == 0
                    if not beaker2_full and not beaker1_empty:
                        pour_extension1 = self.copy()
                        pour_extension1.pour(i, j)
                        pour_extension1._prev_game = self
                        extensions.append(pour_extension1)
                    if not beaker1_full and not beaker2_empty:
                        pour_extension2 = self.copy()
                        pour_extension2.pour(j, i)
                        pour_extension2._prev_game = self
                        extensions.append(pour_extension2)
        return extensions

    def _bfs(self):
        if self.is_over():
            return self
        q = self._extensions()
        seen = set()
        while q:
            # print(len(q))
            curr = q.pop(0)
            if curr in seen:
                continue
            else:
                seen.add(curr)
            # print(curr)
            if curr.is_over():
                return curr
            q.extend(curr._extensions())
        return None

    def hint(self) -> str:
        """Return a properly formatted command (among the available commands)
        that the player should make as their next move.

        Consider a tree of game states, rooted at self, generated one layer at
        a time. Children are created by making one of the available moves to self's
        game state. The tree should stop being generated when a game results in a
        win, and the initial move that was made along that path is returned.

        The algorithm should not explore redundant branches.
        """
        solution = self._bfs()
        if solution is None:
            return 'No hint'
        else:
            curr = solution
            while curr._prev_game is not self:
                curr = curr._prev_game
            return curr._curr_move

    def play(self):
        message = "Welcome to the Elephant Medicine Game (circa 1994 Math Circus)!\n"
        message += f"Your goal is to obtain {self._target} mL of medicine in one \n"
        message += "of the beakers. You may pour one beaker into another one, fill \n"
        message += "a beaker, or empty a beaker. Below is a list of available commands .\n\n"
        message += "pour <#> into <#>\n"
        message += "fill <#> \n"
        message += "empty <#>\n"
        message += "exit\n"
        message += "hint"
        print(message)

        while not self.is_over() and not self._is_over:
            print(self)
            c = input("Command:")

            # parse command
            c = c.split(" ")
            command = c[0].lower()
            if command == "pour" and len(c) == 4:
                self.pour(int(c[1]), int(c[3]))
            elif command == "fill" and len(c) == 2:
                self.fill(int(c[1]))
            elif command == "empty" and len(c) == 2:
                self.empty(int(c[1]))
            elif command == "hint" and len(c) == 1:
                print(self.hint())
            elif command == "exit":
                self._is_over = True
            else:
                print("That is not a recognized command")

        if not self._is_over:
            print(f"Congratulations, you won in {self._moves} moves!")
        else:
            print(f"You exited after {self._moves} moves. Better luck next time.")


if __name__ == "__main__":
    game = ElephantMedicineGame(4)
    # print(game._dfs())
    game.play()
