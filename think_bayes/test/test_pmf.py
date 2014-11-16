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

    def test_increase_no_such_values_new_value_increase(self):
        """Verify increasing the mass of a new value increases the probability mass of that value."""

        cut = Pmf()

        expect_mass = fractions.Fraction(28, 42)
        value = 'fastidiosorum'
        cut.increment(value, expect_mass)

        self.assertEqual(expect_mass, cut[value])

    def test_increase_existing_value_existing_increased(self):
        """Verify increasing the mass of an existing value increases its probability mass."""

        cut = Pmf()

        start_mass = 80
        expect_value = 'aeternales'
        cut[expect_value] = start_mass

        cut.increment(expect_value, 72)

        self.assertEqual(start_mass + 72, cut[expect_value])

    def test_increase_corpus_corpus_created(self):
        """Verify incrementing the frequency of words in a corpus."""

        corpus = 'The quick little brown fox jumped over the lazy grey lambs.'
        cut = Pmf()
        for word in corpus.split():
            cut.increment(word.lower().rstrip('.'), 1)

        expected_corpus_map = {'the' : 2, 'quick': 1, 'little': 1, 'brown': 1, 'fox': 1, 'jumped': 1, 'over': 1,
                               'lazy': 1, 'grey': 1, 'lambs': 1}
        self.assertEqual(len(expected_corpus_map), len(cut))
        for word in expected_corpus_map:
            self.assertEqual(expected_corpus_map[word], cut[word])

    def test_many_items_get_many_items(self):
        """Verify getting many items from a Pmf instance."""

        cut = self.create_many_value_pmf(self.many_int_values_mass_map)

        actual_items = cut.items()

        self.assertEquals(self.many_int_values_mass_map.items(), cut.items())

    def test_multiply_mass_mass_multiplied(self):
        """Verify that multiplying an existing mass actually multiplies that mass."""

        cut = Pmf()
        cut['Bowl 1'] = fractions.Fraction(1, 2)
        cut['Bowl 2'] = fractions.Fraction(1, 2)

        cut.multiply('Bowl 1', fractions.Fraction(3, 4))
        self.assertEqual(fractions.Fraction(3, 8), cut['Bowl 1'])

        cut.multiply('Bowl 2', 0.5)
        self.assertEqual(0.25, cut['Bowl 2'])

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

    def test_many_values_get_many_values(self):
        """Verify querying values in a Pmf instance."""

        cut = self.create_many_value_pmf(self.many_int_values_mass_map)
        self.assertEqual(self.many_int_values_mass_map.keys(), cut.values())

    def create_many_value_pmf(self, actual_value_mass_map):
        cut = Pmf()
        for value in actual_value_mass_map:
            cut[value] = actual_value_mass_map[value]
        return cut
