"""Defines the unit tests for the cookie problem based on the Pmf class."""


import unittest

from think_bayes.cookie_pmf import CookiePmf


__author__ = 'l.jones'


class TestCookiePmf(unittest.TestCase):
    """Defines a test for the 'Cookie' problem using the Pmf class."""

    def test_one_update_cookie_correct(self):
        hypotheses = ['Bowl 1', 'Bowl 2']
        cookie = CookiePmf(hypotheses)

        cookie.update('vanilla')

        self.assertAlmostEqual(0.6, cookie._pmf[hypotheses[0]], 1)
        self.assertEqual(0.4, cookie._pmf[hypotheses[1]])

    def test_many_updates_cookie_correct(self):
        hypotheses = ['Bowl 1', 'Bowl 2']
        cookie = CookiePmf(hypotheses)

        for datum in ['vanilla', 'chocolate', 'vanilla']:
            cookie.update(datum)

        self.assertAlmostEqual(0.529, cookie._pmf[hypotheses[0]], 3)
        self.assertAlmostEqual(0.471, cookie._pmf[hypotheses[1]], 3)
