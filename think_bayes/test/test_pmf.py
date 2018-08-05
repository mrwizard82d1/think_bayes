"""Test the probability mass function class (Pmf)."""


import unittest

import think_bayes


class TestPmf(unittest.TestCase):
    def test_constructor(self):
        cut = think_bayes.Pmf()

        self.assertNotEqual(cut, None)
