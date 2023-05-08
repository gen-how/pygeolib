# coding=utf-8
"""Implement rectangle class."""
from __future__ import annotations

from typing import Optional

from .point import Point2D


class Rectangle(object):

    def __init__(self, pt1: tuple[float, float], pt2: tuple[float, float]):
        self.vertices = [
            Point2D(pt1[0], pt1[1]),  # Top left corner
            Point2D(pt2[0], pt1[1]),  # Top right corner
            Point2D(pt2[0], pt2[1]),  # Bottom right corner
            Point2D(pt1[0], pt2[1]),  # Bottom left corner
        ]

    @property
    def width(self) -> float:
        return self.vertices[1].x - self.vertices[0].x

    @property
    def height(self) -> float:
        return self.vertices[2].y - self.vertices[0].y

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def centroid(self) -> Point2D:
        return (self.vertices[0] + self.vertices[3]) / 2

    @property
    def top_left(self) -> Point2D:
        return self.vertices[0]

    @property
    def bottom_right(self) -> Point2D:
        return self.vertices[2]

    def intersection(self, other: Rectangle) -> Optional[Rectangle]:
        x1 = max(self.top_left.x, other.top_left.x)
        y1 = max(self.top_left.y, other.top_left.y)
        x2 = min(self.bottom_right.x, other.bottom_right.y)
        y2 = min(self.bottom_right.y, other.bottom_right.y)

        if (x1 < x2) and (y1 < y2):
            return Rectangle((x1, y1), (x2, y2))
        return None
