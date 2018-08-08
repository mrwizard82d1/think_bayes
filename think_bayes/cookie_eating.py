import fractions

import think_bayes


class CookieEating(think_bayes.Suite):
    def __init__(self):
        think_bayes.Suite.__init__(self, ['Bowl 1', 'Bowl 2'])

        self.mixes = {'Bowl 1': {'Vanilla': fractions.Fraction(30, 40),
                                 'Chocolate': fractions.Fraction(10, 40)},
                      'Bowl 2': {'Vanilla': fractions.Fraction(20, 40),
                                 'Chocolate': fractions.Fraction(20, 40)}}

    def likelihood(self, data, hypothesis):
        """Calculate the likelihood of `data `if `hypothesis` is true."""

        mixture_for_hypothesis = self.mixes[hypothesis]
        result = mixture_for_hypothesis[data]
        return result
