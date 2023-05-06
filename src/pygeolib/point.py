# coding=utf-8
"""Implement point-like classes."""
from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class Point2D:
    x: float
    y: float

    def distance_to(self, other: Point2D) -> float:
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    @property
    def coords(self) -> tuple[float, float]:
        return (self.x, self.y)

    @property
    def int_coords(self) -> tuple[int, int]:
        return (int(self.x), int(self.y))
