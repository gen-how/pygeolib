# coding=utf-8
import unittest

from src.pygeolib import Point2D


class Point2DTestCase(unittest.TestCase):

    def setUp(self):
        self.origin = Point2D(0, 0)
        self.pt = Point2D(3, 4)

    def test_distance_to(self):
        result = self.origin.distance_to(self.pt)
        self.assertEqual(result, 5,
                         f"Incorrect distance, expect: 5 but get: {result}.")
