import unittest
from Day4.advent_day_4 import check_if_not_decreasing, check_for_adjacent_pair, check_for_sequences_of_two


class TestDayFour(unittest.TestCase):
    def test_check_if_not_decreasing_for_decreasing(self):
        expected = False
        result = check_if_not_decreasing(123451)
        self.assertEqual(result, expected)

    def test_check_if_not_decreasing_for_equal(self):
        expected = True
        result = check_if_not_decreasing(222222)
        self.assertEqual(result, expected)

    def test_check_if_not_decreasing_for_increasing(self):
        expected = True
        result = check_if_not_decreasing(123456)
        self.assertEqual(result, expected)

    def test_check_adjacent_pairs_for_no_pairs(self):
        expected = False
        result = check_for_adjacent_pair(123456)
        self.assertEqual(result, expected)

    def test_check_adjacent_pairs_for_no_adjacent_pair(self):
        expected = False
        result = check_for_adjacent_pair(121456)
        self.assertEqual(result, expected)

    def test_check_adjacent_pairs_for_pair(self):
        expected = True
        result = check_for_adjacent_pair(112345)
        self.assertEqual(result, expected)

    def test_check_for_sequences_of_two_quadruple(self):
        expected = False
        result = check_for_sequences_of_two(111123)
        self.assertEqual(result, expected)

    def test_check_for_sequences_of_two_triple(self):
        expected = False
        result = check_for_sequences_of_two(333456)
        self.assertEqual(result, expected)

    def test_check_for_sequences_of_two_exist(self):
        expected = True
        result = check_for_sequences_of_two(112223)
        self.assertEqual(result, expected)
