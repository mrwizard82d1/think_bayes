"""Defines the unit tests for the MontyPmf class."""

from abc import abstractmethod
import fractions
import unittest

from think_bayes import Pmf


__author__ = 'l.jones'


class MontyPmfBase(object):
    """Specifies common services and data for solving 'Monty Hall' problems."""

    def __init__(self, hypotheses):
        """Construct an instance with the specified hypotheses."""

        self._pmf = Pmf()
        self._pmf.add_uniform(hypotheses)
        self._pmf.normalize()

    @abstractmethod
    def likelihood(self, data, hypothesis):
        """
        Returns the likelihood of data given hypothesis.
        """
        pass

    def update(self, data):
        """Update this instance having seen data."""

        for hypothesis in self._pmf.values():
            likelihood = self.likelihood(data, hypothesis)
            self._pmf.multiply(hypothesis, likelihood)
        self._pmf.normalize()


class MontyPmfRandom(MontyPmfBase):
    """"Implements a class to solve the 'Monty Hall' problem using a Pmf with assumption that Monty selects randomly."""

    def likelihood(self, data, hypothesis):
        """Returns the likelihood of data given hypothesis."""

        if hypothesis == data:
            # Monty Hall NEVER shows the door selected by the contestant.
            return 0

        if hypothesis == 'A':
            # Monty Hall randomly picks one of the other two doors.
            return fractions.Fraction(1, 2)

        # Otherwise, Monty Hall shows the other door.
        return 1


class TestMontyPmf(unittest.TestCase):
    """Defines the unit tests for the MontyPmf class."""

    def test_monty_picks_random(self):
        """Verify the posterior probabilities if Monty Hall picks randomly between doors that DO NOT have car."""
        # The car is behind door A, B or C.
        hypos = 'ABC'
        cut = MontyPmfRandom(hypos)

        # Monty shows door B (after you pick A)
        data = 'B'
        cut.update(data)

        expected_posterior = {'A': fractions.Fraction(1, 3), 'B': fractions.Fraction(0), 'C': fractions.Fraction(2, 3)}

        self.assertEqual(expected_posterior, dict(cut._pmf.items()))

