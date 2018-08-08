"""Solve the Monty Hall problem using the MontyPmf class.

This implementation assumes that Monty Hall picks randomly between doors 'B' and
'C' whichever **does not** have the car.
"""


import fractions

import think_bayes


class MontyPmf(think_bayes.Pmf):
    """Customize the Pmf class to solve the Monty Hall problem."""

    def __init__(self, hypotheses):
        think_bayes.Pmf.__init__(self)
        self.set(list(hypotheses), 1)
        self.normalize()

    def update(self, data):
        """Update my probabilities having observed `data`."""

        for hypothesis in self.values():
            likelihood = self.likelihood(data, hypothesis)
            self.multiply(hypothesis, likelihood)
        self.normalize()

    @staticmethod
    def likelihood(data, hypothesis):
        """Return the likelihood of observing `data` if `hypothesis` is true."""
        if hypothesis == data:
            return 0
        elif hypothesis == 'A':
            return fractions.Fraction(1, 2)
        else:
            return 1
