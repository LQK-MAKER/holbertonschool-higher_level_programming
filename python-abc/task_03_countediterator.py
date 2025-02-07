#!/usr/bin/env python3
"""
write class
"""


class CountedIterator:
    """
    class CountedIterator
    Attributs:
    iterator (iter):
    __count (int):
    """

    def __init__(self, item):
        """
        Args:
        item (iterable):
        """
        self.iterator = iter(item)
        self.__count = 0

    def __next__(self):
        """
        Returns:
        object:
        Raises:
        StopIteration:
        """
        item = next(self.iterator)
        self.__count += 1
        return item

    def get_count(self):
        """
        Returns:
        int:
        """
        return self.__count
