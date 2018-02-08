"""
Module to support "Think Bayes."
"""

import collections
import fractions


class Pmf(object):
    """Models a probability mass function."""

    def __init__(self, normalize_func=fractions.Fraction):
        """Constructs a default instance."""
        self.normalize_func = normalize_func
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
        normalized_map = {v: self.normalize_func(m) / constant for v, m in self.map.iteritems()}
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


class Suite(Pmf):
    """Models a suite of hypotheses and their corresponding probabilities.

    A suite is a probability mass function whose hypotheses are mutually exclusive and exhaustive.

    This class is an abstract base class implementing the template method function. The template methods is `update`.
    This method calls the (abstract) primitive method, `likelihood`.
    """

    def __init__(self, hypotheses=tuple(), normalize_func=fractions.Fraction):
        """Initializes the distribution."""
        super(Suite, self).__init__(normalize_func)
        for hypothesis in hypotheses:
            self.set(hypothesis, 1)

    def update(self, data):
        """Update the distribution based on observing `data`."""
        for hypothesis in self.values():
           self.multiply(hypothesis, self.likelihood(data, hypothesis))
        self.normalize()

    def print_distribution(self):
        """Prints the hypothesis and its corresponding probability."""
        for hypothesis in self.values():
            print('{}: {}'.format(hypothesis, self.probability(hypothesis)))

