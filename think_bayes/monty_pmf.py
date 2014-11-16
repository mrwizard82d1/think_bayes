"""Defines class (with different assumptions) for solving 'Monty Hall' problems."""

from abc import abstractmethod
import fractions
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
        """Returns the likelihood of data given hypothesis."""
        raise NotImplementedError

    def update(self, data):
        """Update this instance having seen data."""

        for hypothesis in self._pmf.values():
            likelihood = self.likelihood(data, hypothesis)
            self._pmf.multiply(hypothesis, likelihood)
        self._pmf.normalize()


class MontyPmfRandom(MontyPmfBase):
    """"Class to solve the 'Monty Hall' problem using a Pmf with assumption that Monty selects randomly."""

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


class MontyPmfAlwaysB(MontyPmfBase):
    """Class for solving the 'Monty Hall' problems assuming Monty always picks door 'B' if he can."""

    def likelihood(self, data, hypothesis):
        """Returns the likelihood of data given hypothesis."""

        if hypothesis == data:
            # Monty Hall NEVER shows the door selected by the contestant.
            return 0

        if data == 'B':
            # Monty Hall always tries to pick door 'B'.
            return 1

        # Otherwise, Monty Hall shows the other door.
        return 1