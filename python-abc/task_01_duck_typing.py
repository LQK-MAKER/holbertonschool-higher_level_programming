#!/usr/bin/python3
"""
ok mek
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Class shape
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Class circle
    """
    def __init__(self, radius):
        self.__radius = abs(radius)

    def area(self):
        return (self.__radius ** 2) * math.pi

    def perimeter(self):
        return self.__radius * math.pi * 2


class Rectangle(Shape):
    """
    Class Rectangle
    """
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return (self.__height * 2) + (self.__width * 2)


def shape_info(shape):
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
