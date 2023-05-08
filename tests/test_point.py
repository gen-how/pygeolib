# coding=utf-8
import unittest

from src.pygeolib import Point2D


class Point2DTestCase(unittest.TestCase):

    def test_distance_to(self):
        origin = Point2D(0, 0)
        point = Point2D(3, 4)
        result = origin.distance_to(point)
        self.assertEqual(result, 5,
                         f"Incorrect distance, expect: 5 but get: {result}.")
