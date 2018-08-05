"""Test the probability mass function class (Pmf)."""


import fractions
import unittest

import think_bayes


class TestPmf(unittest.TestCase):
    def test_constructor(self):
        cut = think_bayes.Pmf()

        self.assertNotEqual(cut, None)

    def test_set_new_value(self):
        cut = think_bayes.Pmf()
        cut.set('pernicitas', 552)

        self.assertEqual(cut.probability('pernicitas'), 552)

    def test_change_value(self):
        cut = think_bayes.Pmf()
        cut.set('pernicitas', 552)
        cut.set('pernicitas', 551)

        self.assertEqual(cut.probability('pernicitas'), 551)

    def test_set_multiple_values(self):
        cut = think_bayes.Pmf()
        cut.set(['pernicitas', 'specit', 'medii'], 984)

        self.assertEqual(cut.probability('pernicitas'), 984)
        self.assertEqual(cut.probability('specit'), 984)
        self.assertEqual(cut.probability('medii'), 984)

    def test_increment(self):
        cut = think_bayes.Pmf()
        text = """
        Four score and seven years ago, our fathers brought forth on this continent, a new nation, 
        conceived in Liberty and dedicated to the proposition that all men are created equal.
        """
        for c in text:
            cut.increment(c)

        self.assertEqual(cut.probability('o'), 14)

    def test_normalize(self):
        cut = think_bayes.Pmf()
        chars = 'regimen octavum mordet'
        for c in chars:
            cut.increment(c)
        cut.normalize()

        raw_expected_counts = [('r', 2), ('e', 3), ('g', 1), ('i', 1),
                               ('m',  3), ('o', 2), ('c', 1), ('t', 2),
                               ('a', 1), ('v', 1), ('u', 1), ('d', 1)]
        expected_counts = [(pr[0], fractions.Fraction(pr[1], len(chars))) for pr in raw_expected_counts]

        expected = dict(expected_counts)
        for value in expected.keys():
            self.assertEqual(cut.probability(value), expected[value])

    def test_multiply(self):
        cut = think_bayes.Pmf()
        cut.set(['pernicitas', 'specit', 'medii'], 984)
        cut.normalize()

        cut.multiply('medii', 3)
        cut.normalize()

        self.assertEqual(cut.probability('pernicitas'), fractions.Fraction(1, 5))
        self.assertEqual(cut.probability('specit'), fractions.Fraction(1, 5))
        self.assertEqual(cut.probability('medii'), fractions.Fraction(3, 5))

    def test_values(self):
        cut = think_bayes.Pmf()
        cut.set(['pernicitas', 'specit', 'medii'], 984)

        self.assertEqual({'pernicitas', 'specit', 'medii'}, cut.values())
