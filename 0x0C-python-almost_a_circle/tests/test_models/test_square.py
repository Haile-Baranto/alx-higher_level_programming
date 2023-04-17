import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestSquareConstructor(unittest.TestCase):
    """unittest for the square constructor
        Id id, x and y attributes are optional

    Args:
        unittest (module): module to run unittest
    """
    def test_init_normal_case(self):
        # Test normal case with int size and id
        square = Square(5, id="1")
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertEqual(square.id, "1")
        # Test edge case with float size and int id
        with self.assertRaises(TypeError):
            square = Square(4.5, id=2)
        with self.assertRaises(TypeError):
            square = Square(4, 4.5, id=2)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_init_edge_cases(self):
        # Test edge case with zero size
        with self.assertRaises(ValueError):
            Square(0, id="3")
        # Test edge case with negative size
        with self.assertRaises(ValueError):
            Square(-3, id=4)
        # Test edge case with string size
        with self.assertRaises(TypeError):
            Square("size", id="5")
        # Test edge case with negative x and y
        with self.assertRaises(ValueError):
            Square(5, x=-1, y=-2, id="6")
        # Test edge case with string x
        with self.assertRaises(TypeError):
            Square(5, x="x", y=0, id="7")
        # Test edge case with string y
        with self.assertRaises(TypeError):
            Square(5, x=0, y="y", id="8")
        # Test edge case with negative id
        square = Square(5, id=-1)
        self.assertEqual(square.id, -1)


class TestSquare_str(unittest.TestCase):
    """Tests str method of Square"""

    def test_normal(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertIsNotNone(s.id)

    def test_edge_size_type(self):
        with self.assertRaises(TypeError):
            s = Square("not an int")

    def test_edge_size_value(self):
        with self.assertRaises(ValueError):
            s = Square(0)
        with self.assertRaises(ValueError):
            s = Square(-1)

    def test_edge_x_type(self):
        with self.assertRaises(TypeError):
            s = Square(5, x="not an int")

    def test_edge_x_value(self):
        with self.assertRaises(ValueError):
            s = Square(5, x=-1)

    def test_edge_y_type(self):
        with self.assertRaises(TypeError):
            s = Square(5, y="not an int")

    def test_edge_y_value(self):
        with self.assertRaises(ValueError):
            s = Square(5, y=-1)

    def test_edge_id_type(self):
        s = Square(5, id="an id")
        self.assertEqual(s.id, "an id")

    def test_edge_id_value(self):
        s = Square(5, id=0)
        self.assertEqual(s.id, 0)

    def test_edge_size_equals_1(self):
        s = Square(1)
        self.assertEqual(str(s), "[Square] ({}) 0/0 - 1".format(s.id))


class TestSquareSizeSetter(unittest.TestCase):
    """Tests size setter"""

    def setUp(self):
        self.sq = Square(5)

    def test_valid_size(self):
        self.sq.size = 10
        self.assertEqual(self.sq.width, 10)
        self.assertEqual(self.sq.height, 10)

    def test_size_zero(self):
        with self.assertRaises(ValueError):
            self.sq.size = 0

    def test_size_negative(self):
        with self.assertRaises(ValueError):
            self.sq.size = -5

    def test_size_non_integer(self):
        with self.assertRaises(TypeError):
            self.sq.size = 5.5

    def test_x_non_integer(self):
        with self.assertRaises(TypeError):
            self.sq.x = 5.5

    def test_y_non_integer(self):
        with self.assertRaises(TypeError):
            self.sq.y = 5.5

    def test_valid_id(self):
        self.sq.id = "test_id"
        self.assertEqual(self.sq.id, "test_id")


class TestRectangleUpdate(unittest.TestCase):
    """Tests update method of Square"""

    def setUp(self):
        self.r1 = Square(10, 10, 10, 10)

    def test_update_with_args(self):
        self.r1.update(1)
        self.assertEqual(self.r1.id, 1)

        self.r1.update(1, 2)
        self.assertEqual(self.r1.size, 2)

        self.r1.update(1, 2, 3)
        self.assertEqual(self.r1.x, 3)

        self.r1.update(1, 2, 3, 4)
        self.assertEqual(self.r1.y, 4)

    def test_update_with_kwargs(self):
        self.r1.update(id=1)
        self.assertEqual(self.r1.id, 1)

        self.r1.update(size=2)
        self.assertEqual(self.r1.size, 2)

        self.r1.update(x=3)
        self.assertEqual(self.r1.x, 3)

        self.r1.update(y=4)
        self.assertEqual(self.r1.y, 4)

    def test_update_with_args_and_kwargs(self):
        self.r1.update(1, size=2)
        self.assertEqual(self.r1.id, 1)
        self.assertNotEqual(self.r1.size, 2)

        self.r1.update(1, 2, x=3)
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r1.size, 2)
        self.assertNotEqual(self.r1.x, 3)

    def test_update_with_invalid_args(self):
        with self.assertRaises(ValueError):
            self.r1.update(1, -2)

    def test_update_with_invalid_kwargs(self):
        with self.assertRaises(ValueError):
            self.r1.update(size=0)

        with self.assertRaises(ValueError):
            self.r1.update(x=-1)

    def test_update_with_args_and_kwargs_skips_kwargs(self):
        self.r1.update(1, 2, y=4)
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r1.size, 2)
        # y is not updated as it is given as kwarg and args is already present
        self.assertEqual(self.r1.y, 10)


class TestSquareToDictionary(unittest.TestCase):
    """Test to dict method of Sqaure"""
    def test_normal_square(self):
        s = Square(1, 2, 3, 4)
        expected_dict = {'id': s.id, 'size': 1, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_square_with_id_none(self):
        s = Square(1, 2, 3)
        expected_dict = {'id': s.id, 'size': 1, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_square_with_optional_values(self):
        s = Square(1)
        expected_dict = {'id': s.id, 'size': 1, 'x': 0, 'y': 0}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_square_with_invalid_size(self):
        with self.assertRaises(ValueError):
            s = Square(-1, 2, 3, 4)
            s.to_dictionary()

    def test_square_with_invalid_x(self):
        with self.assertRaises(ValueError):
            s = Square(1, -2, 3, 4)
            s.to_dictionary()

    def test_square_with_invalid_y(self):
        with self.assertRaises(ValueError):
            s = Square(1, 2, -3, 4)
            s.to_dictionary()


if __name__ == '__main__':
    unittest.main()
