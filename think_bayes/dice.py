"""Models a suite for solving dice problems."""


import fractions

import think_bayes


class Dice(think_bayes.Suite):
    """A Suite for solving dice problems."""
    def likelihood(self, data, hypothesis):
        if hypothesis < data:
            return 0
        else:
            return fractions.Fraction(1, hypothesis)
