import unittest
from pawn import PurplePawn, RedPawn, BluePawn, OrangePawn, PinkPawn


class test_purple_pawn(unittest.TestCase):

    def setUp(self):
        self.pawn = PurplePawn()
        self.pawn.position = (3, 4)

    def test_name(self):
        self.assertEqual('purple pawn', self.pawn.name)

    def test_should_move_horizontally(self):
        self.assertTrue(self.pawn.can_move(3, 0))
        self.assertTrue(self.pawn.can_move(3, 4))
        self.assertTrue(self.pawn.can_move(3, 100))

    def test_should_not_move_in_other_directions(self):
        self.assertFalse(self.pawn.can_move(2, 0))
        self.assertFalse(self.pawn.can_move(4, 4))
        self.assertFalse(self.pawn.can_move(-3, 100))


class test_red_pawn(unittest.TestCase):

    def setUp(self):
        self.pawn = RedPawn()
        self.pawn.position = (4, 3)

    def test_name(self):
        self.assertEqual('red pawn', self.pawn.name)

    def test_should_move_horizontally(self):
        self.assertTrue(self.pawn.can_move(4, 0))
        self.assertTrue(self.pawn.can_move(4, 4))
        self.assertTrue(self.pawn.can_move(4, 100))

    def test_should_move_vertically(self):
        self.assertTrue(self.pawn.can_move(0, 3))
        self.assertTrue(self.pawn.can_move(4, 3))
        self.assertTrue(self.pawn.can_move(100, 3))

    def test_should_not_move_in_any_other_direction(self):
        self.assertFalse(self.pawn.can_move(2, 0))
        self.assertFalse(self.pawn.can_move(3, 4))
        self.assertFalse(self.pawn.can_move(-4, -3))


class test_blue_pawn(unittest.TestCase):

    def setUp(self):
        self.pawn = BluePawn()
        self.pawn.position = (6, 1)

    def test_name(self):
        self.assertEqual('blue pawn', self.pawn.name)

    def test_should_move_just_once(self):
        self.assertTrue(self.pawn.can_move(5, 0))
        self.assertTrue(self.pawn.can_move(5, 1))
        self.assertTrue(self.pawn.can_move(5, 2))
        self.assertTrue(self.pawn.can_move(6, 0))
        self.assertTrue(self.pawn.can_move(6, 1))
        self.assertTrue(self.pawn.can_move(6, 2))
        self.assertTrue(self.pawn.can_move(7, 0))
        self.assertTrue(self.pawn.can_move(7, 1))
        self.assertTrue(self.pawn.can_move(7, 2))

    def test_should_not_move_twice(self):
        self.assertFalse(self.pawn.can_move(5, 3))
        self.assertFalse(self.pawn.can_move(4, 1))
        self.assertFalse(self.pawn.can_move(8, 1))
        self.assertFalse(self.pawn.can_move(6, -1))
        self.assertFalse(self.pawn.can_move(6, 3))


class test_orange_pawn(unittest.TestCase):

    def setUp(self):
        self.pawn = OrangePawn()
        self.pawn.position = (2, 3)

    def test_name(self):
        self.assertEqual('orange pawn', self.pawn.name)

    def test_should_move_in_l(self):
        self.assertTrue(self.pawn.can_move(2, 3))  # same
        # Vertically and then horizontally
        self.assertTrue(self.pawn.can_move(0, 2))  # Up
        self.assertTrue(self.pawn.can_move(0, 4))
        self.assertTrue(self.pawn.can_move(4, 2))  # Down
        self.assertTrue(self.pawn.can_move(4, 4))
        # Horizontally and then vertically
        self.assertTrue(self.pawn.can_move(1, 1))  # Left
        self.assertTrue(self.pawn.can_move(3, 1))
        self.assertTrue(self.pawn.can_move(1, 5))  # Right
        self.assertTrue(self.pawn.can_move(3, 5))

    def test_should_not_move_in_other_directions(self):
        # move 1 pos
        self.assertFalse(self.pawn.can_move(2, 4))
        self.assertFalse(self.pawn.can_move(3, 3))
        self.assertFalse(self.pawn.can_move(3, 4))
        # horizontally 2 pos
        self.assertFalse(self.pawn.can_move(2, 5))


class test_pink_pawn(unittest.TestCase):

    def setUp(self):
        self.pawn = PinkPawn()
        self.pawn.position = (2, 3)

    def test_name(self):
        self.assertEqual('pink pawn', self.pawn.name)

    def test_should_move_horizontally(self):
        self.assertTrue(self.pawn.can_move(2, 0))
        self.assertTrue(self.pawn.can_move(2, 4))
        self.assertTrue(self.pawn.can_move(2, 100))

    def test_should_move_vertically(self):
        self.assertTrue(self.pawn.can_move(0, 3))
        self.assertTrue(self.pawn.can_move(4, 3))
        self.assertTrue(self.pawn.can_move(100, 3))

    def test_should_move_diagonally(self):
        self.assertTrue(self.pawn.can_move(2, 3))
        # Up left
        self.assertTrue(self.pawn.can_move(1, 2))
        self.assertTrue(self.pawn.can_move(0, 1))
        # Up right
        self.assertTrue(self.pawn.can_move(1, 4))
        self.assertTrue(self.pawn.can_move(0, 5))
        # Down left
        self.assertTrue(self.pawn.can_move(3, 2))
        self.assertTrue(self.pawn.can_move(4, 1))
        self.assertTrue(self.pawn.can_move(5, 0))
        # Down right
        self.assertTrue(self.pawn.can_move(3, 4))
        self.assertTrue(self.pawn.can_move(4, 5))
        self.assertTrue(self.pawn.can_move(5, 6))
        self.assertTrue(self.pawn.can_move(6, 7))

    def test_shoud_not_move_in_L(self):
        # Vertically and then horizontally
        self.assertFalse(self.pawn.can_move(0, 2))  # Up
        self.assertFalse(self.pawn.can_move(0, 4))
        self.assertFalse(self.pawn.can_move(4, 2))  # Down
        self.assertFalse(self.pawn.can_move(4, 4))
        # Horizontally and then vertically
        self.assertFalse(self.pawn.can_move(1, 1))  # Left
        self.assertFalse(self.pawn.can_move(3, 1))
        self.assertFalse(self.pawn.can_move(1, 5))  # Right
        self.assertFalse(self.pawn.can_move(3, 5))
