"""Solves the M&M problem using a Suite."""


import think_bayes


class MAndM(think_bayes.Suite):
    """Models the M&M problem using a Suite."""

    def __init__(self, hypotheses):
        think_bayes.Suite.__init__(self, hypotheses)

        self.mix_94 = dict(brown=30,
                           yellow=20,
                           red=20,
                           green=10,
                           orange=10,
                           tan=10)
        self.mix_96 = dict(blue=24,
                           green=20,
                           orange=16,
                           yellow=14,
                           red=13,
                           brown=13)
        self.hypothesis_a = dict(bag_1=self.mix_94,
                                 bag_2=self.mix_96)
        self.hypothesis_b = dict(bag_1=self.mix_96,
                                 bag_2=self.mix_94)
        self.hypotheses = dict(A=self.hypothesis_a,
                               B=self.hypothesis_b)

    def likelihood(self, data, hypothesis):
        bag, color = data
        mix = self.hypotheses[hypothesis][bag]
        result = mix[color]
        return result
