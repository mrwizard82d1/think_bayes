"""Implements the Pmf (probability mass function) class."""


import fractions


class Pmf:
    """Models a probability mass function."""

    def __init__(self):
        """Construct a default instance."""
        self._distribution = {}

    def probability(self, value):
        """Return the probability or mass of value."""
        return self._distribution[value]

    def probabilities(self):
        """Return the probability (mass) of all values."""
        return dict(self._distribution)

    def increment(self, value):
        """Increment the probability (or mass) of value by 1."""
        self._distribution[value] = self._distribution.get(value, 0) + 1

    def multiply(self, value, factor):
        """Multiply the mass of value by factor."""
        self._distribution[value] *= factor

    def normalize(self):
        """Normalize the masses to probabilities."""
        normalizer = sum(self._distribution.values())
        for value in self._distribution.keys():
            self._distribution[value] = (self._distribution[value] / normalizer if
                                         (isinstance(self._distribution[value], float) or
                                          isinstance(normalizer, float)) else
                                         fractions.Fraction(self._distribution[value], normalizer))

    def set(self, value, probability):
        """Set the probability of value."""
        self._distribution[value] = probability


