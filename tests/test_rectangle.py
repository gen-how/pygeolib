# coding=utf-8
import unittest

from src.pygeolib import Rectangle


class RectangleTestCase(unittest.TestCase):

    def test_intersection_valid(self):
        a = Rectangle((0, 0), (10, 10))
        b = Rectangle((5, 5), (15, 15))
        result = a.intersection(b)
        assert result != None
        self.assertEqual(result.top_left.x, 5)
        self.assertEqual(result.top_left.y, 5)
        self.assertEqual(result.bottom_right.x, 10)
        self.assertEqual(result.bottom_right.y, 10)

    def test_intersection_invalid(self):
        c = Rectangle((0, 0), (5, 5))
        d = Rectangle((10, 10), (15, 15))
        result = c.intersection(d)
        self.assertIsNone(result)
    
    def test_intersection_over_union_valid(self):
        a = Rectangle((0, 0), (10, 10))
        b = Rectangle((5, 5), (15, 15))
        self.assertEqual(25 / 175, a.intersection_over_union(b))

    def test_intersection_over_union_invalid(self):
        c = Rectangle((0, 0), (5, 5))
        d = Rectangle((10, 10), (15, 15))
        self.assertEqual(0, c.intersection_over_union(d))
        