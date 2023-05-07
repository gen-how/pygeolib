# coding=utf-8
"""Implement rectangle class."""
from __future__ import annotations

from .point import Point2D


class Rectangle(object):

    def __init__(self, pt1: tuple[float, float], pt2: tuple[float, float]):
        self.vertices = [
            Point2D(pt1[0], pt1[1]),  # Top-left corner
            Point2D(pt2[0], pt1[1]),  # Top-right corner
            Point2D(pt2[0], pt2[1]),  # Bottom-right corner
            Point2D(pt1[0], pt2[1]),  # Bottom-left corner
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
