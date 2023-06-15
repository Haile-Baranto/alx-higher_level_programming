#!/usr/bin/python3
import unittest
import sys
import io
from models.rectangle import Rectangle
""" The nodule tests rectangle.py file
    """


class TestRectangleInit(unittest.TestCase):
    """Unit tests for the initialization of the Rectangle class."""

    def test_valid_args(self):
        """Test creating a rectangle with valid arguments."""
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, r1.id)

    def test_valid_args_with_id(self):
        """Test creating a rectangle with valid arguments and
            a specified ID."""
        r1 = Rectangle(10, 20, 0, 0, 123)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 123)

    def test_invalid_args(self):
        """Test creating a rectangle with invalid arguments."""
        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, 20)

        with self.assertRaises(ValueError):
            r2 = Rectangle(10, -20)

        with self.assertRaises(ValueError):
            r3 = Rectangle(0, 20)

        with self.assertRaises(TypeError):
            r4 = Rectangle(10, 20, "a", 0)

        with self.assertRaises(TypeError):
            r5 = Rectangle(10, 20, 0, "a")

        with self.assertRaises(ValueError):
            r6 = Rectangle(10, 20, -1, 0)

        with self.assertRaises(ValueError):
            r7 = Rectangle(10, 20, 0, -1)

    def test_valid_args_with_extra_args(self):
        """Test creating a rectangle with extra arguments."""
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 20, 0, 0, 123, "extra", True, None)


class TestRectangleWidth(unittest.TestCase):
    """test for initialization of Rectangle width attribute."""

    def test_width_none(self):
        with self.assertRaises(TypeError):
            Rectangle(None, 1, 2, 3, 4)
        with self.assertRaises(TypeError):
            Rectangle(None, 6)

    def test_width_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, 5, 7, 6, 7)

    def test_width_float_inf(self):
        with self.assertRaises(TypeError):
            Rectangle(float('inf'), 5, 0, 0, 5)

    def test_width_tuple(self):
        with self.assertRaises(TypeError):
            Rectangle(("hi", 2, True), 6, 8, 6, 2)

    def test_width_list(self):
        with self.assertRaises(TypeError):
            Rectangle(['if', 'list', 'type', 'error'], 4, 4, 5, 6)

    def test_width_float_nan(self):
        with self.assertRaises(TypeError):
            Rectangle(float('nan'), 7, 2, 3, 4)

    def test_width_float_point(self):
        with self.assertRaises(TypeError):
            Rectangle(5.0, 7, 0, 0, 1)

    def test_width_dictionary(self):
        with self.assertRaises(TypeError):
            Rectangle({'one': 1, 'two': 2}, 6, 8, 6, 5)

    def test_width_arguement(self):
        rect = Rectangle(17, 11, 1, 1, "Hello")
        self.assertEqual(rect.width, 17)

    def test_width_string(self):
        with self.assertRaises(TypeError):
            Rectangle("Hello", 7, 0, 0, 1)


class TestRectangleX(unittest.TestCase):
    """test for initialization of Rectangle x attribute."""

    def test_x_none(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 1, None, 3, 4)
        with self.assertRaises(TypeError):
            Rectangle(5, 6, None)

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 5, -7, 6, 7)

    def test_x_float_inf(self):
        with self.assertRaises(TypeError):
            Rectangle(float('inf'), 5, 0, 0, 5)

    def test_x_tuple(self):
        with self.assertRaises(TypeError):
            Rectangle(8, 6, ("hi", 2, True), 6, 2)

    def test_x_list(self):
        with self.assertRaises(TypeError):
            Rectangle(4, 4, ['if', 'list', 'type', 'error'], 5, 6)

    def test_x_float_nan(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 7, float('nan'), 3, 4)

    def test_x_float_point(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 7, 5.0, 0, 1)

    def test_x_dictionary(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 6, {'one': 1, 'two': 2}, 6, 5)

    def test_x_arguement(self):
        rect = Rectangle(17, 11, 1, 1, "Hello")
        self.assertEqual(rect.x, 1)

    def test_x_string(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 7, "Hello", 0, 1)


class TestRectangleHeight(unittest.TestCase):
    """test for initialization of Rectangle height attribute."""

    def test_height_none(self):
        with self.assertRaises(TypeError):
            Rectangle(1, None, 2, 3, 4)
        with self.assertRaises(TypeError):
            Rectangle(6, None)

    def test_height_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(5, -5, 7, 6, 7)

    def test_height_float_inf(self):
        with self.assertRaises(TypeError):
            Rectangle(5, float('inf'), 0, 0, 5)

    def test_height_tuple(self):
        with self.assertRaises(TypeError):
            Rectangle(6, ("hi", 2, True), 8, 6, 2)

    def test_height_list(self):
        with self.assertRaises(TypeError):
            Rectangle(4, ['if', 'list', 'type', 'error'], 4, 5, 6)

    def test_height_float_nan(self):
        with self.assertRaises(TypeError):
            Rectangle(7, float('nan'), 2, 3, 4)

    def test_height_float_point(self):
        with self.assertRaises(TypeError):
            Rectangle(7, 5.0, 0, 0, 1)

    def test_height_dictionary(self):
        with self.assertRaises(TypeError):
            Rectangle(1, {'one': 1, 'two': 2}, 8, 6, 5)

    def test_height_arguement(self):
        rect = Rectangle(17, 11, 1, 1, "Hello")
        self.assertEqual(rect.height, 11)

    def test_height_string(self):
        with self.assertRaises(TypeError):
            Rectangle(7, "hello", 0, 0, 1)


class TestRectangleY(unittest.TestCase):
    """test for initialization of Rectangle y attribute."""

    def test_y_none(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 1, 3, None, 4)
        with self.assertRaises(TypeError):
            Rectangle(5, 6, 4, None)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 5, 7, -6, 7)

    def test_y_float_inf(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, float('inf'), 5)

    def test_y_tuple(self):
        with self.assertRaises(TypeError):
            Rectangle(8, 6, 6, ("hi", 2, True), 2)

    def test_y_list(self):
        with self.assertRaises(TypeError):
            Rectangle(4, 4, 5, ['if', 'list', 'type', 'error'], 6)

    def test_y_float_nan(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 7, 3, float('nan'), 4)

    def test_x_float_point(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 7, 5, 5.5, 1)

    def test_y_dictionary(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 6, 5, {'one': 1, 'two': 2}, 5)

    def test_y_arguement(self):
        rect = Rectangle(17, 11, 1, 1, "Hello")
        self.assertEqual(rect.y, 1)

    def test_y_string(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 7, 0, "Hello", 1)


class TestRectangleId(unittest.TestCase):
    """test for initialization of id of rectangle"""

    def test_id_negative(self):
        rect = Rectangle(5, 5, 7, 6, -7)
        self.assertEqual(rect.id, -7)

    def test_id_float_inf(self):
        rect = Rectangle(1, 2, 3, 5, float('inf'))
        self.assertEqual(rect.id, float('inf'))

    def test_id_tuple(self):
        rect = Rectangle(8, 6, 6, 5, ("hi", 2, True))
        self.assertEqual(rect.id, ("hi", 2, True))

    def test_id_list(self):
        rect = Rectangle(4, 4, 5, 6, ['if', 'list', 'type', 'error'])
        self.assertEqual(rect.id, ['if', 'list', 'type', 'error'])

    def test_id_float_nan(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 7, 3, float('nan'), 4)

    def test_id_float_point(self):
        rect = Rectangle(1, 7, 5, 1, 5.5)
        self.assertEqual(rect.id, 5.5)

    def test_id_dictionary(self):
        rect = Rectangle(1, 6, 5, 5, {'one': 1, 'two': 2})
        self.assertEqual(rect.id, {'one': 1, 'two': 2})

    def test_id_arguement(self):
        rect = Rectangle(2, 1, 3, 4, "hello")
        self.assertEqual(rect.id, "hello")

    def test_id_string(self):
        rect = Rectangle(2, 1, 3, 4, "hello")
        self.assertEqual(rect.id, "hello")

    def test_wrong_id(self):
        with self.assertRaises(NameError):
            Rectangle(10, 2, 1, 1, hello)


class TestRectangleArea(unittest.TestCase):
    """test for  area of the Rectangle class."""

    def test_area_int(self):
        rect = Rectangle(3, 5)
        self.assertEqual(15, rect.area())

    def test_change_rect_area(self):
        rect = Rectangle(2, 10, 0, 0, 6)
        rect.width = 10
        rect.height = 10
        self.assertEqual(100, rect.area())

    def test_missing_height(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(4, None, 0, 0, 6)

    def test_area_intger(self):
        rect = Rectangle(3, 30, 0, 0, 6)
        self.assertEqual(90, rect.area())

    def test_missing_height_2(self):
        rect = Rectangle(4, 5, 0, 0, 6)
        with self.assertRaises(TypeError):
            rect(10)

    def test_width_missing(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(None, 10, 0, 0, 6)

    def test_missing_width_2(self):
        rect = Rectangle(6, 7, 0, 0, True)
        with self.assertRaises(TypeError):
            rect(7)


class TestRectangleDisplay(unittest.TestCase):
    def test_display(self):
        rectangle = Rectangle(3, 4)
        expected_output = '###\n###\n###\n###\n'
        captured_output = io.StringIO()
        sys.stdout = captured_output
        rectangle.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)


class TestRectangle_str(unittest.TestCase):
    """Unittest for Rectangle.__str__ methd"""

    def test_str_method_positive_integers(self):
        # Test case 1: width and height are positive integers,
        # x and y are non-negative integers
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (5) 3/4 - 1/2")

    def test_str_method_positive_floats(self):
        # Test case 2: width and height are positive floats,
        # x and y are non-negative floats
        with self.assertRaises(TypeError):
            r2 = Rectangle(1.5, 2.5, 3.5, 4.5, 6)

    def test_str_method_negative_width(self):
        # Test case 3: width is negative integer
        with self.assertRaises(ValueError):
            r3 = Rectangle(-1, 2, 3, 4, 7)

    def test_str_method_negative_height(self):
        # Test case 4: height is negative integer
        with self.assertRaises(ValueError):
            r4 = Rectangle(1, -2, 3, 4, 8)

    def test_str_method_negative_x(self):
        # Test case 5: x is negative integer
        with self.assertRaises(ValueError):
            r5 = Rectangle(1, 2, -3, 4, 9)

    def test_str_method_negative_y(self):
        # Test case 6: y is negative integer
        with self.assertRaises(ValueError):
            r6 = Rectangle(1, 2, 3, -4, 10)

    def test_str_method_zero_width(self):
        # Test case 7: width is zero
        with self.assertRaises(ValueError):
            r7 = Rectangle(0, 2, 3, 4, 11)

    def test_str_method_zero_height(self):
        # Test case 8: height is zero
        with self.assertRaises(ValueError):
            r8 = Rectangle(1, 0, 3, 4, 12)

    def test_str_method_zero_x(self):
        # Test case 9: x is zero
        r9 = Rectangle(1, 2, 0, 4, 13)
        self.assertEqual(str(r9), "[Rectangle] (13) 0/4 - 1/2")

    def test_str_method_zero_y(self):
        # Test case 10: y is zero
        r10 = Rectangle(1, 2, 3, 0, 14)
        self.assertEqual(str(r10), "[Rectangle] (14) 3/0 - 1/2")


class TestRectangleUpdate(unittest.TestCase):
    """unittest for Rectangle.update() method"""

    def setUp(self):
        self.rect = Rectangle(10, 10, 0, 0, 1)

    def test_update_args(self):
        self.rect.update(2)
        self.assertEqual(self.rect.id, 2)

        self.rect.update(3, 4)
        self.assertEqual(self.rect.id, 3)
        self.assertEqual(self.rect.width, 4)

        self.rect.update(5, 6, 7)
        self.assertEqual(self.rect.id, 5)
        self.assertEqual(self.rect.width, 6)
        self.assertEqual(self.rect.height, 7)

        self.rect.update(8, 9, 10, 11)
        self.assertEqual(self.rect.id, 8)
        self.assertEqual(self.rect.width, 9)
        self.assertEqual(self.rect.height, 10)
        self.assertEqual(self.rect.x, 11)

        self.rect.update(12, 13, 14, 15, 16)
        self.assertEqual(self.rect.id, 12)
        self.assertEqual(self.rect.width, 13)
        self.assertEqual(self.rect.height, 14)
        self.assertEqual(self.rect.x, 15)
        self.assertEqual(self.rect.y, 16)

    def test_update_kwargs(self):
        self.rect.update(id=2)
        self.assertEqual(self.rect.id, 2)

        self.rect.update(id=3, width=4)
        self.assertEqual(self.rect.id, 3)
        self.assertEqual(self.rect.width, 4)

        self.rect.update(id=5, width=6, height=7)
        self.assertEqual(self.rect.id, 5)
        self.assertEqual(self.rect.width, 6)
        self.assertEqual(self.rect.height, 7)

        self.rect.update(id=8, width=9, height=10, x=11)
        self.assertEqual(self.rect.id, 8)
        self.assertEqual(self.rect.width, 9)
        self.assertEqual(self.rect.height, 10)
        self.assertEqual(self.rect.x, 11)

        self.rect.update(id=12, width=13, height=14, x=15, y=16)
        self.assertEqual(self.rect.id, 12)
        self.assertEqual(self.rect.width, 13)
        self.assertEqual(self.rect.height, 14)
        self.assertEqual(self.rect.x, 15)
        self.assertEqual(self.rect.y, 16)

    def test_update_args_kwargs(self):
        self.rect.update(2, id=3)
        # *args should take priority over **kwargs
        self.assertEqual(self.rect.id, 2)
        self.assertNotEqual(self.rect.id, 3)
        # *args should take priority over **kwargs
        self.rect.update(4, 5, id=6, width=7)
        self.assertEqual(self.rect.id, 4)
        self.assertEqual(self.rect.width, 5)
        self.assertNotEqual(self.rect.id, 6)
        self.assertEqual(self.rect.width, 5)


class TestRectangleToDictionary(unittest.TestCase):
    """Unittests for testing to dictionary for rectangle class."""

    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == '__main__':
    unittest.main()
