"""Defines a class for solving the 'cookie problem' using a Pmf."""


from think_bayes import Pmf

__author__ = 'l.jones'


class CookiePmf(object):
    """Defines a class to solve the 'cookie' problem based on the Pmf class."""

    def __init__(self, hypotheses):
        """Construct an instance with hypotheses."""

        self._pmf = Pmf()
        for hypothesis in hypotheses:
            self._pmf.increment(hypothesis, 1)
        self._pmf.normalize()

        self._mixes = {'Bowl 1': {'vanilla': 0.75, 'chocolate': 0.25},
                       'Bowl 2': {'vanilla': 0.5, 'chocolate': 0.5}}

    def likelihood(self, data, hypothesis):
        """Calculate the likelihood of data given hypothesis."""

        mixture = self._mixes[hypothesis]
        result = mixture[data]
        return result

    def update(self, data):
        """Update this instance having seen data."""

        for hypothesis in self._pmf.values():
            likelihood_of_data = self.likelihood(data, hypothesis)
            self._pmf.multiply(hypothesis, likelihood_of_data)
        self._pmf.normalize()