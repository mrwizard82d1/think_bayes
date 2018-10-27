"""Unit tests calculations using the Bayes table method."""


import fractions
import unittest

import think_bayes


class TestMAndMTable(unittest.TestCase):

    def test_m_and_ms_bag1_1994_bag2_1996(self):
        table_data = {'a': think_bayes.Table.Row(fractions.Fraction(1, 2), 20 * 20),
                      'b': think_bayes.Table.Row(fractions.Fraction(1, 2), 10 * 14)}
        sut = think_bayes.Table(table_data)

        self.assertEqual(fractions.Fraction(20, 27), sut.posterior('a'))

    def test_m_and_ms_bag1_1996_bag2_1994(self):
        table_data = {'a': think_bayes.Table.Row(fractions.Fraction(1, 2), 20 * 20),
                      'b': think_bayes.Table.Row(fractions.Fraction(1, 2), 10 * 14)}
        sut = think_bayes.Table(table_data)

        self.assertEqual(fractions.Fraction(7, 27), sut.posterior('b'))


class TestMontyHallTableRandomChooseAvailable(unittest.TestCase):
    # The hypotheses, 'a', 'b', and 'c', model the situation in which the car is behind door named by the hypothesis.
    # For example, hypothesis 'a' means that car is *actually* behind door 'a'.
    #
    # To calculate the likelihoods, given that you have picked door 'a', we reason as follows:
    #
    # If the car is behind door 'a', Monty Hall can safely pick either door 'b' or 'c'. Assume he picks one at
    # random. Therefore, the likelihood of picking door 'b' is 1/2. If the car is behind door 'b', the likelihood of
    # Monty Hall picking door 'b' is 0. Finally, if the car is behind door 'c', the likelihood of Monty Hall picking
    # door 'b' is is 1. (He cannot pick door 'c'.)

    table_data = {'a': think_bayes.Table.Row(fractions.Fraction(1, 3), fractions.Fraction(1, 2)),
                  'b': think_bayes.Table.Row(fractions.Fraction(1, 3), 0),
                  'c': think_bayes.Table.Row(fractions.Fraction(1, 3), 1)}

    def test_monty_hall_stay_with_a(self):
        sut = think_bayes.Table(self.table_data)

        self.assertEqual(fractions.Fraction(1, 3), sut.posterior('a'))

    def test_monty_hall_cannot_pick_b(self):
        sut = think_bayes.Table(self.table_data)

        self.assertEqual(0, sut.posterior('b'))

    def test_monty_hall_change_to_c(self):
        sut = think_bayes.Table(self.table_data)

        self.assertEqual(fractions.Fraction(2, 3), sut.posterior('c'))

