"""Test the probability mass function class (Pmf)."""


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
