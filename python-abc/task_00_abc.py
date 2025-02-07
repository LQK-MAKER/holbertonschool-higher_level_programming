#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    class
    """

    @abstractmethod
    def sound(self):
        """
        class pass
        """
        pass


class Dog(Animal):
    """
    dog class
    """

    def sound(self):
        """
        dog sound
        """
        return "Bark"


class Cat(Animal):
    """
    cat class
    """

    def sound(self):
        """
        cat sound
        """
        return "Meow"
