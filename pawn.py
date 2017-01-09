
class Pawn:
    def __init__(self, name):
        self.name = name
        self.set_pos(-1, -1)

    def can_move(self, row, col=None):
        p = row if col is None else (row, col)
        diff = (p[0] - self.pos[0], p[1] - self.pos[1])
        return self.can_move_relative(diff);

    def can_move_relative(self, relative_position):
        """
        Takes a relative position to the pawn and return wheter the pawn
        can move to that relative position
        Args:
            relative_position (tuple): The relative position, (row,
            column)
        """
        return False

    def set_pos(self, row, col = None):
        if col is None:
            self.pos = row # Row is a tuple
        else:
            self.pos = (row, col)

class PurplePawn(Pawn):
    """
    Pawn that moves horizontally
    """
    def __init__(self):
        # Change to call super class
        self.name = 'purple pawn'

    def can_move_relative(self, relative_position):
        # Same row
        return relative_position[0] == 0

class RedPawn(Pawn):
    """
    Pawn that moves horizontally and vertically (like a rock)
    """
    def __init__(self):
        self.name = 'red pawn'

    def can_move_relative(self, relative_position):
        # Same row or same column
        return relative_position[0] == 0 or relative_position[1] == 0


class BluePawn(Pawn):
    """
    Pawn that moves in all directions, once (like a king)
    """
    def __init__(self):
        self.name = 'blue pawn'

    def can_move_relative(self, relative_position):
        # move one row and one column max
        return abs(relative_position[0]) <= 1 and \
            abs(relative_position[1]) <= 1


class OrangePawn(Pawn):
    """
    Pawn that moves in an L (like a knight)
    """
    def __init__(self):
        self.name = 'orange pawn'

    def can_move_relative(self, relative_position):
        # move one row and 2 columns or viceversa
        y = abs(relative_position[0])
        x = abs(relative_position[1])
        return x == y ==  0 or x == 2 and y == 1 or x == 1 and y == 2

class PinkPawn(Pawn):
    """
    Pawn that moves in all directions (like a queen)
    """
    def __init__(self):
        self.name = 'pink pawn'

    def can_move_relative(self, relative_position):
        # move one row and 2 columns or viceversa
        y = abs(relative_position[0])
        x = abs(relative_position[1])
        return (
                    # Vertically
                    x == 0 or
                    # Horizontally
                    y == 0 or
                    # Diagonally
                    (x == y)
                )
