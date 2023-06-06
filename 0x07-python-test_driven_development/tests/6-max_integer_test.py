""" The following code is different edge case tests for
    the max integer function
    """
import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTestCase(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_empty_list(self):
        """Test with an empty list"""
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element_list(self):
        """Test with a list containing a single element"""
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_positive_numbers(self):
        """Test with a list of positive numbers"""
        result = max_integer([1, 3, 2, 5, 4])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        """Test with a list of negative numbers"""
        result = max_integer([-1, -3, -2, -5, -4])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """Test with a list of mixed positive and negative numbers"""
        result = max_integer([1, -3, 0, 5, -4])
        self.assertEqual(result, 5)

    def test_duplicate_numbers(self):
        """Test with a list containing duplicate numbers"""
        result = max_integer([1, 3, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_list_with_none(self):
        """Test with a list containing None"""
        with self.assertRaises(TypeError):
            max_integer([1, 3, None, 5])

    def test_large_numbers(self):
        """Test with a list of large numbers"""
        result = max_integer([10**9, 10**12, 10**15])
        self.assertEqual(result, 10**15)

    def test_large_number_of_elements(self):
        """Test with a large number of elements in the list"""
        result = max_integer(list(range(1, 100001)))
        self.assertEqual(result, 100000)

    def test_negative_infinity(self):
        """Test with negative infinity in the list"""
        result = max_integer([1, 2, float('-inf'), 5])
        self.assertEqual(result, 5)

    def test_positive_infinity(self):
        """Test with positive infinity in the list"""
        result = max_integer([1, 2, float('inf'), 5])
        self.assertEqual(result, float('inf'))

    def test_nan(self):
        """Test with NaN (Not a Number) in the list"""
        result = max_integer([1, 2, float('nan'), 5])
        self.assertEqual(result, 5)
