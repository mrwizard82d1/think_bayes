import fractions


class MnMTable:
    def __init__(self):
        """Construct an instance."""
        self.hypotheses = 'AB'
        self.priors = {'A': fractions.Fraction(1, 2),
                       'B': fractions.Fraction(1, 2)}
        self.mix_1994 = {'brown': 30,
                         'yellow': 20,
                         'red': 20,
                         'green': 10,
                         'orange': 10,
                         'tan': 10}
        self.mix_1996 = {'blue': 24,
                         'green': 20,
                         'orange': 16,
                         'yellow': 14,
                         'red': 13,
                         'brown': 13}
        self.likelihoods = {'A': 1, 'B': 1}

    def not_hypothesis(self, hypothesis):
        return [c for c in self.hypotheses if c != hypothesis][0]

    def observe(self, data1, data2):
        for hypothesis in self.hypotheses:
            factor1 = self.mix_1994[data1] if hypothesis == self.hypotheses[0] else self.mix_1996[data1]
            factor2 = self.mix_1994[data2] if \
                self.not_hypothesis(hypothesis) == self.hypotheses[0] else self.mix_1996[data2]
            self.likelihoods[hypothesis] *= (factor1 * factor2)

    def posteriors(self, hypothesis):
        product = self.priors[hypothesis] * self.likelihoods[hypothesis]
        not_hypothesis = [c for c in self.hypotheses if c != hypothesis][0]
        not_product = self.priors[not_hypothesis] * self.likelihoods[not_hypothesis]

        normalizing_factor = product + not_product

        return product / normalizing_factor
