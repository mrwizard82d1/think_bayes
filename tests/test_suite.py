"""Unit tests for Suite class."""


import fractions
import unittest

import think_bayes


class SuiteToTest(think_bayes.Suite):
    def __init__(self, hypotheses):
        think_bayes.Suite.__init__(self, hypotheses, use_fractions=True)

    def likelihood(self, data, hypothesis):
        mixes = {'b1': dict(v=30, c=10), 'b2': dict(v=20, c=20)}
        result = fractions.Fraction(mixes[hypothesis][data], sum(mixes[hypothesis].values()))
        return result


class SuiteToTestFloat(think_bayes.Suite):
    def likelihood(self, data, hypothesis):
        mixes = {'b1': dict(v=30, c=10), 'b2': dict(v=20, c=20)}
        result = mixes[hypothesis][data] / sum(mixes[hypothesis].values())
        return result


class TestSuite(unittest.TestCase):
    def uniform_posteriors_after_construction(self):
        sut = SuiteToTest(['collegorum', 'perpendent'])

        self.assertEqual({'collegorum': fractions.Fraction(1, 2),
                          'perpendent': fractions.Fraction(1, 2)},
                         sut.posterior())

    def test_update_v1(self):
        sut = SuiteToTest(['b1', 'b2'])
        sut.update('v')

        self.assertEqual({'b1': fractions.Fraction(3, 5),
                          'b2': fractions.Fraction(2, 5)},
                         sut.posterior())

    def test_update_v1_float(self):
        sut = SuiteToTestFloat(['b1', 'b2'])
        sut.update('v')

        self.assertEqual({'b1': 0.6, 'b2': 0.4}, sut.posterior())
