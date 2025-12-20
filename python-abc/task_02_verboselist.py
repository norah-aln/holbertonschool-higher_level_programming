#!/usr/bin/env python3
"""Module that extends Python list with notifications"""


class VerboseList(list):
    """A list subclass that prints notifications for modifications"""

    def append(self, item):
        """Append an item to the list with notification

        Args:
            item: The item to append
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list with an iterable with notification

        Args:
            iterable: The iterable to extend the list with
        """
        count = len(list(iterable))
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove an item from the list with notification

        Args:
            item: The item to remove
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the list with notification

        Args:
            index: The index of the item to pop (default: -1)

        Returns:
            The popped item
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
