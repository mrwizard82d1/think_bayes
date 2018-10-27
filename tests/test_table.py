"""Unit tests calculations using the Bayes table method."""


import fractions
import unittest

import think_bayes


class TestMAndMTable(unittest.TestCase):
    table_data = {'a': think_bayes.Table.Row(fractions.Fraction(1, 2), 20 * 20),
                  'b': think_bayes.Table.Row(fractions.Fraction(1, 2), 10 * 14)}

    def test_m_and_ms_bag1_1994_bag2_1996(self):
        sut = think_bayes.Table(self.table_data)

        self.assertEqual(fractions.Fraction(20, 27), sut.posterior('a'))

    def test_m_and_ms_bag1_1996_bag2_1994(self):
        sut = think_bayes.Table(self.table_data)

        self.assertEqual(fractions.Fraction(7, 27), sut.posterior('b'))

