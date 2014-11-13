"""Defines the unit tests for the Pmf class."""


__author__ = 'l.jones'


import unittest

from think_bayes import Pmf


class TestPmf(unittest.TestCase):
    """Defines the unit tests for the Pmf class.

    A Pmf maps between values and probability (masses). Note that the probability mass returned for a value is
    only guaranteed to be a probability if the class has invoked the method normalize()."""

    def test_get_no_values_raises_error(self):
        """Verify that attempting to query a probability mass when none set raises error."""

        cut = Pmf()

        self.assertRaises(KeyError, cut.__getitem__, None)

    def test_set_one_probability_one_set(self):
        """Verify setting the probability mass for a single value sets that mass."""

        cut = Pmf()
        cut['pernas'] = 0.5

        actual_probability = cut['pernas']

        self.assertEqual(0.5, actual_probability)

    def test_set_many_probabilities_many_set(self):
        """Verify setting the probability masses forr many values sets many masses."""

        cut = Pmf()
        actual_value_mass_map = {'trepidis': 6, 'invidiae': 67, 'videbio': 27}
        for value in actual_value_mass_map:
            cut[value] = actual_value_mass_map[value]

        for value in actual_value_mass_map:
            self.assertEqual(actual_value_mass_map[value], cut[value])
