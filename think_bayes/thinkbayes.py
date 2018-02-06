"""
Module to support "Think Bayes."
"""

class Pmf(object):
    """Models a probability mass function."""

    def __init__(self):
        """Constructs a default instance."""
        self.map = {} # maps values to their probabilities


    def set(self, value, mass):
        """Sets the probability mass of `value ` to `mass`."""
        self.map[value] = mass

    def probability(self, value):
        """Return the probability mass of `value`."""
        return self.map[value]

