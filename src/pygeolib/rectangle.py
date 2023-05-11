# coding=utf-8
"""Implement rectangle class."""
from __future__ import annotations

from typing import Optional

from .point import Point2D


class Rectangle(object):
    """A rectangle in 2D space."""

    def __init__(self, pt1: tuple[float, float], pt2: tuple[float, float]):
        """Initialize the rectangle by given top left and bottom right points."""
        self.vertices = [
            Point2D(pt1[0], pt1[1]),  # Top left corner
            Point2D(pt2[0], pt1[1]),  # Top right corner
            Point2D(pt2[0], pt2[1]),  # Bottom right corner
            Point2D(pt1[0], pt2[1]),  # Bottom left corner
        ]

    @staticmethod
    def from_centroid(centroid: tuple[float, float], width: float,
                      height: float) -> Rectangle:
        """Initialize the rectangle by given centroid, width and height."""
        pt1 = (centroid[0] - width / 2, centroid[1] - height / 2)
        pt2 = (centroid[0] + width / 2, centroid[1] + height / 2)
        return Rectangle(pt1, pt2)

    @property
    def width(self) -> float:
        """Return the width of the rectangle."""
        return self.vertices[1].x - self.vertices[0].x

    @property
    def height(self) -> float:
        """Return the height of the rectangle."""
        return self.vertices[2].y - self.vertices[0].y

    @property
    def area(self) -> float:
        """Return the area of the rectangle."""
        return self.width * self.height

    @property
    def centroid(self) -> Point2D:
        """Return the centroid of the rectangle."""
        return (self.vertices[0] + self.vertices[3]) / 2

    @property
    def top_left(self) -> Point2D:
        """Return the top left corner of the rectangle."""
        return self.vertices[0]

    @property
    def bottom_right(self) -> Point2D:
        """Return the bottom right corner of the rectangle."""
        return self.vertices[2]

    def intersection(self, other: Rectangle) -> Optional[Rectangle]:
        """Return the intersection of two rectangles. If the two rectangles do 
        not intersect, return `None`.
        """
        x1 = max(self.top_left.x, other.top_left.x)
        y1 = max(self.top_left.y, other.top_left.y)
        x2 = min(self.bottom_right.x, other.bottom_right.y)
        y2 = min(self.bottom_right.y, other.bottom_right.y)

        if (x1 < x2) and (y1 < y2):
            return Rectangle((x1, y1), (x2, y2))
        return None

    def intersection_over_union(self, other: Rectangle) -> float:
        """Return the intersection over union (IoU) of two rectangles. If the
        two rectangles do not intersect, return `0`.
        """
        inter = self.intersection(other)
        if inter is None:
            return 0

        union = self.area + other.area - inter.area
        return inter.area / union
