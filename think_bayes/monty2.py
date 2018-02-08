"""Solving the Monty Hall problem using Suite."""

import fractions
import thinkbayes


class Monty2(thinkbayes.Suite):

    def __init__(self, hypotheses):
        super(Monty2, self).__init__(hypotheses)

    def likelihood(self, data, hypothesis):
        if hypothesis == data:
            return 0

        if hypothesis == 'A':
            return fractions.Fraction(1, 2)

        return 1
