# coding=utf-8
"""Implement point-like classes."""
from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class Point2D:
    """A point in 2D space."""
    x: float
    y: float

    def __eq__(self, other: Point2D) -> bool:
        return (self.x == other.x) and (self.y == other.y)

    def __add__(self, other: Point2D) -> Point2D:
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Point2D) -> Point2D:
        return Point2D(self.x - other.x, self.y - other.y)

    def __mul__(self, factor: float) -> Point2D:
        return Point2D(self.x * factor, self.y * factor)

    def __truediv__(self, divisor: float) -> Point2D:
        return Point2D(self.x / divisor, self.y / divisor)

    @property
    def coords(self) -> tuple[float, float]:
        """Return the coordinates of the point as a tuple."""
        return (self.x, self.y)

    @property
    def int_coords(self) -> tuple[int, int]:
        """Return the coordinates of the point as a tuple of `int`."""
        return (int(self.x), int(self.y))

    def distance_to(self, other: Point2D) -> float:
        """Return the distance to another point."""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
