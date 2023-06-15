#!/usr/bin/python3
# test_base.py
"""Defines unittests for base.py."""
import unittest
import os
import json
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from unittest.mock import mock_open, patch


class TestBaseConstructor(unittest.TestCase):
    """To test constructor of Base class"""

    def test_incrementation_class_variable(self):
        """ obj id increments """
        Base._Base__nb_objects = 0

        base1 = Base()
        self.assertEqual(base1.id, 1)

        base2 = Base()
        self.assertEqual(base2.id, 2)

        base3 = Base()
        self.assertEqual(base3.id, 3)
        base4 = Base()
        self.assertEqual(base4.id, 4)

    def test_inputs(self):
        """checks for valid input """
        Base._Base__nb_objects = 0

        first_base = Base()
        self.assertEqual(first_base.id, 1)

        positive_id_base = Base(20)
        self.assertEqual(positive_id_base.id, 20)

    def test_negative_id(self):
        negative_id_base = Base(-19)
        self.assertEqual(negative_id_base.id, -19)

    def test_float_id(self):
        float_id_base = Base(-6.5)
        self.assertEqual(float_id_base.id, -6.5)

        float_id_base = Base(6.5)
        self.assertEqual(float_id_base.id, 6.5)

    def test_public_id(self):
        base = Base(12)
        base.id = 20
        self.assertEqual(base.id, 20)

    def test_unique_id(self):
        self.assertEqual(20, Base(20).id)

    def test_str(self):
        """checks for valid id """
        string_id_base = Base("Hi")
        self.assertEqual(string_id_base.id, "Hi")

    def test_dict_id_base(self):
        dict_base = Base({'int': 1, 'base': "alx"})
        self.assertEqual(dict_base.id, {'int': 1, 'base': "alx"})

    def test_tuple_id(self):
        tuple_base = Base((1, 2, "hi"))
        self.assertEqual(tuple_base.id, (1, 2, "hi"))

    def test_id_list(self):
        b_list = Base([1, 2, 3])
        self.assertEqual(b_list.id, [1, 2, 3])

    def test_range_id(self):
        range_id = Base(range(4))
        self.assertEqual(range_id.id, range(4))

    def test_float_inf(self):
        b_float_inf = Base(float('inf'))
        self.assertEqual(b_float_inf.id, float('inf'))

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_error(self):
        """checks for error"""
        with self.assertRaises(TypeError):
            Base(5, 5)

        with self.assertRaises(TypeError):
            Base(5, None)

        with self.assertRaises(TypeError):
            Base(None, 5)


class TestBase_json_string(unittest.TestCase):

    def test_to_json_string_empty_list(self):
        empty_list = []
        expected_output = "[]"
        actual_output = Base.to_json_string(empty_list)
        self.assertEqual(actual_output, expected_output)

    def test_to_json_string_single_empty_dict(self):
        single_empty_dict = [{}]
        expected_output = "[{}]"
        actual_output = Base.to_json_string(single_empty_dict)
        self.assertEqual(actual_output, expected_output)

    def test_to_json_string_single_dict(self):
        single_dict = [{"name": "John", "age": 30}]
        expected_output = '[{"name": "John", "age": 30}]'
        actual_output = Base.to_json_string(single_dict)
        self.assertEqual(actual_output, expected_output)

    def test_to_json_string_multiple_dicts(self):
        multiple_dicts = [{"name": "John", "age": 30}, {"name": "Jane",
                                                        "age": 25}]
        exp_out = '[{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]'
        actual_output = Base.to_json_string(multiple_dicts)
        self.assertEqual(actual_output, exp_out)

    def test_to_json_string_none_input(self):
        none_input = None
        expected_output = "[]"
        actual_output = Base.to_json_string(none_input)
        self.assertEqual(actual_output, expected_output)

    def test_to_json_string_invalid_input(self):
        invalid_input = "invalid input"
        expected_output = "[]"
        actual_output = Base.to_json_string(invalid_input)
        self.assertNotEqual(actual_output, expected_output)


class TestBase_save_to_file(unittest.TestCase):

    def setUp(self):
        self.filename = "Base.json"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_save_to_file_empty_list(self):
        empty_list = []
        Base.save_to_file(empty_list)
        with open(self.filename, mode="r", encoding="utf-8") as f:
            expected_output = "[]"
            actual_output = f.read()
            self.assertEqual(actual_output, expected_output)

    def test_save_to_file_none_input(self):
        none_input = None
        Base.save_to_file(none_input)
        with open(self.filename, mode="r", encoding="utf-8") as f:
            expected_output = "[]"
            actual_output = f.read()
            self.assertEqual(actual_output, expected_output)

    def test_save_to_file_base_instance(self):
        instance = Base()
        with self.assertRaises(TypeError):
            Base.save_to_file(instance)

    def test_save_to_file_subclass_instance(self):
        class Sub(Base):
            pass
        instance = Sub()
        with self.assertRaises(TypeError):
            Base.save_to_file(instance)


class TestRectangleAndSquare(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(10, 5)
        self.r2 = Rectangle(2, 4, 1, 1)
        self.s1 = Square(3)
        self.s2 = Square(5, 2, 3)

    def tearDown(self):
        if os.path.exists('Rectangle.csv'):
            os.remove('Rectangle.csv')
        if os.path.exists('Square.csv'):
            os.remove('Square.csv')

    def test_load_from_file_csv_with_valid_csv_file(self):
        self.r1.save_to_file_csv([self.r1, self.r2])
        self.s1.save_to_file_csv([self.s1, self.s2])
        loaded_rectangles = Rectangle.load_from_file_csv()
        loaded_squares = Square.load_from_file_csv()
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertIsInstance(loaded_rectangles[0], Rectangle)
        self.assertIsInstance(loaded_rectangles[1], Rectangle)
        self.assertEqual(loaded_rectangles[0].width, 10)
        self.assertEqual(loaded_rectangles[0].height, 5)
        self.assertEqual(loaded_rectangles[1].x, 1)
        self.assertEqual(loaded_rectangles[1].y, 1)
        self.assertEqual(len(loaded_squares), 2)
        self.assertIsInstance(loaded_squares[0], Square)
        self.assertIsInstance(loaded_squares[1], Square)
        self.assertEqual(loaded_squares[0].size, 3)
        self.assertEqual(loaded_squares[1].x, 2)
        self.assertEqual(loaded_squares[1].y, 3)

    def test_load_from_file_csv_with_missing_csv_file(self):
        loaded_rectangles = Rectangle.load_from_file_csv()
        loaded_squares = Square.load_from_file_csv()
        self.assertEqual(len(loaded_rectangles), 0)
        self.assertEqual(len(loaded_squares), 0)


class TestLoadFromFile(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[]')
    def test_load_from_file_with_empty_file(self, mock_file):
        from models.rectangle import Rectangle
        expected_list = []
        self.assertEqual(Rectangle.load_from_file(), expected_list)

    @patch("builtins.open", new_callable=mock_open, read_data='')
    def test_load_from_file_with_nonexistent_file(self, mock_file):
        from models.rectangle import Rectangle
        expected_list = []
        self.assertEqual(Rectangle.load_from_file(), expected_list)


class TestCreateMethod(unittest.TestCase):

    def test_create_rectangle(self):
        r = Rectangle.create(id=1, width=2, height=3, x=4, y=5)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_create_square(self):
        s = Square.create(id=1, size=2, x=3, y=4)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)


class TestFromJsonString(unittest.TestCase):
    def test_valid_json_string(self):
        json_string = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        exp_out = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
        result = Base.from_json_string(json_string)
        self.assertEqual(result, exp_out)

    def test_empty_json_string(self):
        json_string = ''
        expected_result = []
        result = Base.from_json_string(json_string)
        self.assertEqual(result, expected_result)

    def test_none_json_string(self):
        json_string = None
        expected_result = []
        result = Base.from_json_string(json_string)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
