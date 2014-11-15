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

    def increase(self, value, amount):
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

