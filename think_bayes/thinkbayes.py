"""
Module to support "Think Bayes."
"""

import collections
import fractions


class Pmf(object):
    """Models a probability mass function."""

    def __init__(self):
        """Constructs a default instance."""
        self.map = collections.defaultdict(int) # maps values to their probabilities

    def set(self, value, mass):
        """Sets the probability mass of `value ` to `mass`."""
        self.map[value] = mass

    def probability(self, value):
        """Return the probability mass of `value`."""
        return self.map[value]

    def increment(self, word, by=1):
        self.map[word] += by

    def normalize(self):
        constant = sum(self.map.values())
        normalized_map = {v: fractions.Fraction(m) / constant for v, m in self.map.iteritems()}
        self.map = normalized_map

    def multiply(self, value, scale):
        """Scale the probability mass of `value` by `scale`."""
        self.map[value] *= scale

    def values(self):
        """Iterate over the values in this instance."""
        return self.map.iterkeys()

    def items(self):
        """Iterate over the value, mass pairs of this instance."""
        return self.map.iteritems()

