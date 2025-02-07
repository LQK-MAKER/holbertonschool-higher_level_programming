#!/usr/bin/env python3
"""
write class
"""


class VerboseList(list):
    """
    Class VerboseList
    """
    def append(self, item):
        """
        Args:
        item (Any):
        """
        print("Added [{}] to the list".format(item))
        super().append(item)

    def extend(self, items):
        """
        Args:
        items (list):
        """
        print("Extended the list with [{}] items.".format(len(items)))
        super().extend(items)

    def remove(self, item):
        """
        Args:
        item (Any):
        Raises:
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Args:
        Returns:
        Any:
        Raises:
        """
        if len(self) == 0:
            print("The list is empty, cannot pop an item.")
            return None
        print("Popped [{}] from the list.".format(self[index]))
        return super().pop(index)
