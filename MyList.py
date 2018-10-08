class MyList:
    """A base class providing a doubly linked list representation."""
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = "_element", "_prev", "_next"

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Create an empty list"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        """Return the number of elements in the list"""
        return self._size

    def is_empty(self):
        """Return True if list is empty"""
        return self._size == 0

    def append(self, x):
        """Add an item to the end of the list. Equivalent to a[len(a):] = [x]"""
        pass

    def extend(self, iterable_obj):
        """Extend the list by appending all the items from the iterable_obj. Equivalent to a[len(a):] = iterable_obj."""
        pass

    def insert(self, i, x):
        """Insert an item at a given position. The first argument is the index of the element before which to insert,
        so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x)."""
        pass

    def remove(self, x):
        """Remove the first item from the list whose value is x. It is an error if there is no such item."""
        pass

    def pop(self, i=None):
        """Remove the first item from the list whose value is x. It is an error if there is no such item.
        The i parameter is optional, it references to the index of the element."""
        pass

    def clear(self):
        """Remove all items from the list. Equivalent to del a[:]."""
        pass

    def index(self, x, start=None, end=None):
        """Return zero-based index in the list of the first item whose value is x. Raises a ValueError if there is no such item.
        The optional arguments start and end are interpreted as in the slice notation and are used to limit the search
        to a particular subsequence of the list. The returned index is computed relative to the beginning of the full
        sequence rather than the start argument."""
        pass

    def count(self, x):
        """Return the number of times x appears in the list."""
        pass

    def sort(self, key=None, reverse=False):
        """Sort the items of the list in place"""
        pass

    def reverse(self):
        """Reverse the elements of the list in place."""
        pass

    def __add__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __le__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __contains__(self, item):
        pass

    def __delitem__(self, key):
        pass

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __del__(self):
        pass

    def __str__(self):
        pass

    def __bool__(self):
        pass
