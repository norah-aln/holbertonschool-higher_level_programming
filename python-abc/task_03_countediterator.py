#!/usr/bin/env python3
"""Module that implements a counted iterator"""


class CountedIterator:
    """An iterator that keeps track of the number of items iterated"""

    def __init__(self, iterable):
        """Initialize the CountedIterator

        Args:
            iterable: The iterable to iterate over
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Fetch the next item and increment the counter

        Returns:
            The next item from the iterator

        Raises:
            StopIteration: When there are no more items
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Get the number of items that have been iterated

        Returns:
            int: The count of items iterated
        """
        return self.count
