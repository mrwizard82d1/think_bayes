import fractions
import unittest

import think_bayes


class TestMnmTable(unittest.TestCase):
    def test_yellow_1994(self):

        cut = think_bayes.MnMTable()
        cut.observe('yellow', 'green')

        self.assertEqual(fractions.Fraction(20, 27), cut.posteriors('A'))
