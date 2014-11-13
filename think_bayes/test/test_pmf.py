"""Defines the unit tests for the Pmf class."""


__author__ = 'l.jones'


import fractions
import unittest

from think_bayes import Pmf


class TestPmf(unittest.TestCase):
    """Defines the unit tests for the Pmf class.

    A Pmf maps between values and probability (masses). Note that the probability mass returned for a value is
    only guaranteed to be a probability if the class has invoked the method normalize()."""

    def setUp(self):
        """Perform common set up for fixture."""

        self.many_int_values_mass_map = {'trepidis': 6, 'invidiae': 67, 'videbio': 27}

    def test_get_no_values_raises_error(self):
        """Verify that attempting to query a probability mass when none set raises error."""

        cut = Pmf()

        self.assertRaises(KeyError, cut.__getitem__, None)

    def test_increase_no_values_one_set_to_increase(self):
        """Verify increasing the mass with no values increases the probability mass of value."""

        cut = Pmf()

        expect_mass = fractions.Fraction(28, 42)
        value = 'fastidiosorum'
        cut.increase(value, expect_mass)

        self.assertEqual(expect_mass, cut[value])

    def test_increase_one_value_one_increased(self):
        """Verify increasing the mass with one value increases its probability mass."""

        cut = Pmf()

        start_mass = 80
        expect_value = 'aeternales'
        cut[expect_value] = start_mass

        cut.increase(expect_value, 72)

        self.assertEqual(start_mass + 72, cut[expect_value])

    def test_normalize_one_value_probability_is_one(self):
        """Verify that normalizing a Pmf with a single value makes probability one."""

        cut = Pmf()

        start_mass = 78.381141730761684
        value = 9
        cut[value] = start_mass

        cut.normalize()

        self.assertEqual(1, cut[value])

    def test_normalize_many_values_pmf_probability_is_one(self):
        """Verify that normalizing a Pmf with many values makes probability of any one."""

        cut = self.create_many_value_pmf(self.many_int_values_mass_map)

        cut.normalize()

        probability_sum = 0
        for value in cut:
            probability_sum += cut[value]

        self.assertEqual(1, probability_sum)

    def test_normalize_many_values_pmf_normalizes_all_masses(self):
        """Verify that normalizing a Pmf with many values normalizes all masses."""

        cut = self.create_many_value_pmf(self.many_int_values_mass_map)

        cut.normalize()

        mass_total = sum(self.many_int_values_mass_map.values())
        expect_normalized_map = {k: fractions.Fraction(v, mass_total)
                                 for (k, v) in self.many_int_values_mass_map.items()}
        for k in expect_normalized_map:
            self.assertEqual(expect_normalized_map[k], cut[k])


    def test_set_one_value_one_set(self):
        """Verify setting the probability mass for a single value sets that mass."""

        cut = Pmf()
        cut['pernas'] = 0.5

        actual_probability = cut['pernas']

        self.assertEqual(0.5, actual_probability)


    def test_set_many_values_many_set(self):
        """Verify setting the probability masses forr many values sets many masses."""

        cut = self.create_many_value_pmf(self.many_int_values_mass_map)

        for value in self.many_int_values_mass_map:
            self.assertEqual(self.many_int_values_mass_map[value], cut[value])

    def create_many_value_pmf(self, actual_value_mass_map):
        cut = Pmf()
        for value in actual_value_mass_map:
            cut[value] = actual_value_mass_map[value]
        return cut
