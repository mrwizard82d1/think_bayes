"""Suite for solving the Monty Hall problem.

This `Suite` assumes that Monty Hall randomly picks between doors if he has a choice.
"""


import fractions

import think_bayes


class Monty(think_bayes.Suite):
    """Models the Monty Hall problem."""
    def __init__(self, hypotheses):
        super().__init__(hypotheses, use_fractions=True)

    def likelihood(self, data, hypothesis):
        if data == hypothesis:
            return 0
        elif hypothesis == 'A': # Car is behind door 'A'
            return fractions.Fraction(1, 2)
        else:
            return 1

