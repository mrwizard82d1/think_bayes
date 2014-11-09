"""Defines the unit tests for the bayes_calc module."""


__author__ = 'l.jones'


import unittest

import think_bayes.bayes_calc


class BayesCalcTest(unittest.TestCase):
    """Defines the unit tests for the BayesCalc class."""


    def test_ctor_one_hypo_has_hypo(self):
        """Verify that constructing an instance with one hypothesis has that hypothesis."""

        hypothesis = 'advertebas'

        cut = think_bayes.bayes_calc.BayesCalc([hypothesis])

        self.assertIn(hypothesis, cut.hypotheses)

    def test_ctor_one_hypo_has_two_hypos(self):
        """Verify that constructing an instance with one hypothesis has two hypotheses."""

        cut = think_bayes.bayes_calc.BayesCalc([''])

        self.assertEqual(2, len(cut.hypotheses))

    def test_ctor_one_hypo_has_not_hypo(self):
        """Verify that constructing an instance with one hypothesis adds not hypothesis."""

        hypothesis = 'pomi'
        cut = think_bayes.bayes_calc.BayesCalc([hypothesis])

        self.assertIn('not %s' % hypothesis, cut.hypotheses)

    def test_ctor_no_hypo_raises_error(self):
        "Verify that constructing an instance with no hypotheses raises an error."

        self.assertRaises(ValueError, think_bayes.bayes_calc.BayesCalc, [])

    def test_ctor_two_hypos_has_hypos(self):
        """Verify that constructing an instance with two hypotheses has two hypotheses."""

        hypotheses = ['officiem', 'lapidarie']

        cut = think_bayes.bayes_calc.BayesCalc(hypotheses)

        self.assertEqual(hypotheses, cut.hypotheses)