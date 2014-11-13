"""Models a probability mass function."""


__author__ = 'l.jones'


class Pmf(object):
    """Models a probability mass function."""

    def __init__(self):
        """Construct an instance."""
        self._repr = {}

    def __getitem__(self, item):
        """Returns the probability mass of item."""
        return self._repr[item]

    def __setitem__(self, key, value):
        """Sets the probability mass of key to value."""
        self._repr[key] = value
