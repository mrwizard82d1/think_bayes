"""The Monty Hall problem using the `Suite` abstract class."""


import fractions

import think_bayes


class Monty(think_bayes.Suite):
    """Solving the Monty Hall problem using a `Suite`."""

    def likelihood(self, data, hypothesis):
        """Calculate the likelihood of seeing `data` if `hypothesis` is true."""
        if hypothesis == data:
            return 0
        elif hypothesis == 'A':
            return fractions.Fraction(1, 2)
        else:
            return 1
