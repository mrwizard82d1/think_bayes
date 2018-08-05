"""Solve the cookie problem using a class."""


import fractions

import think_bayes


class Cookie(think_bayes.Pmf):
    """Model the cookie problem using a probability mass function."""

    def __init__(self, hypotheses):
        """Construct an instance with the hypotheses."""

        think_bayes.Pmf.__init__(self)
        self.set(hypotheses, 1)
        self.normalize()

        self.mixes = {'Bowl 1': {'Vanilla': fractions.Fraction(30, 40),
                                 'Chocolate': fractions.Fraction(10, 40)},
                      'Bowl 2': {'Vanilla': fractions.Fraction(20, 40),
                                 'Chocolate': fractions.Fraction(20, 40)}}

    def likelihood(self, data, hypothesis):
        """Calculate the likelihood of `data `if `hypothesis` is true."""

        mixture_for_hypothesis = self.mixes[hypothesis]
        result = mixture_for_hypothesis[data]
        return result
