"""Defines the Cookie class."""


import fractions

import think_bayes


class Cookie:
    """Models a distribution for solving the cookie problem."""
    def __init__(self, hypotheses):
        self._pmf = think_bayes.Pmf()
        self._hypotheses = hypotheses
        for hypothesis in hypotheses:
            self._pmf.set(hypothesis, fractions.Fraction(1, len(hypotheses)))

    def hypotheses(self):
        """Return the hypotheses for the cookie problem."""
        return self._hypotheses

    def likelihood(self, data, hypothesis):
        """Calculate the likelihood of seeing data given hypothesis.

        This method is **very** specific to the cookie problem.
        """
        mixes = {'bowl 1': dict(vanilla=fractions.Fraction(3, 4), chocolate=fractions.Fraction(1, 4)),
                 'bowl 2': dict(vanilla=fractions.Fraction(1, 2), chocolate=fractions.Fraction(1, 2))}
        return mixes[hypothesis][data]

    def posterior(self):
        """Return the posterior distribution."""
        return self._pmf.probabilities()

    def update(self, data):
        """Update the distribution after seeing data."""
        for hypothesis in self.hypotheses():
            self._pmf.multiply(hypothesis, self.likelihood(data, hypothesis))

        self._pmf.normalize()
