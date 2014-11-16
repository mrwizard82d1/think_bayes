"""Models a probability mass function."""
import fractions


__author__ = 'l.jones'


class Pmf(object):
    """Models a probability mass function."""

    def __init__(self):
        """Construct an instance."""
        self._repr = {}

    def __getitem__(self, item):
        """Returns the probability mass of item."""
        return self._repr[item]

    def __len__(self):
        """Return the number if items in this instance."""
        return len(self._repr)

    def __iter__(self):
        """Returns an iterator over the values of this instance."""
        return iter(self._repr)

    def __setitem__(self, key, value):
        """Sets the probability mass of key to value."""
        self._repr[key] = value

    def add_all(self, values):
        """Adds all values to this instance with the same weight and allowing duplicates."""

        for value in values:
            self.increment(value, 1)

    def add_uniform(self, values):
        """Adds all values to this instance giving each a mass of 1."""

        for value in values:
            self[value] = 1

    def items(self):
        """Returns the items in this Pmf."""
        return self._repr.items()

    def increment(self, value, amount):
        """Increase the probability mass of value by amount."""
        self._repr[value] = self._repr.get(value, 0) + amount

    def multiply(self, value, amount):
        """Multiply probability mass of value by amount."""
        self._repr[value] *= amount

    def normalize(self):
        """Normalize the probability mass to actual probabilities."""

        weight = sum(self._repr.values())
        try:
            factor = fractions.Fraction(1, weight)
        except TypeError:
            factor = 1 / weight
        for value in self._repr:
            self.multiply(value, factor)

    def values(self):
        """Return all the values in this instance."""

        return self._repr.keys()

