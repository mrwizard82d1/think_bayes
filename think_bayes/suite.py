"""Defines a class for solving problems in Bayesian inforence."""


import fractions

import think_bayes


class Suite(think_bayes.Pmf):
    """Models a suite of exhaustive and exclusive hypotheses."""

    def __init__(self, hypotheses, use_fractions=False):
        """Construct an instance.

        :hypotheses: The exhaustive and exclusive hypotheses.
        :use_fractions: Set if we are using `fractions`. Defaults to `False`.
        """
        think_bayes.Pmf.__init__(self)
        self._hypotheses = hypotheses
        self._use_fractions = use_fractions
        for hypothesis in hypotheses:
            self.set(hypothesis, fractions.Fraction(1, len(hypotheses)))

    def likelihood(self, data, hypothesis):
        """Calculate the likelihood of data given hypothesis.

        Child classes must implement this method.
        """

        raise NotImplementedError();

    def posterior(self):
        """Return the posterior distribution."""
        return self.probabilities()

    def update(self, data):
        """Update the distribution after seeing data.

        This method plays the role of _Template Method_ in the _Template Method_ design pattern.

        In that role, this method defines an algorithm to update the distribution in terms of the
        _Primitive_ method, `likelihood`.
        """

        for hypothesis in self._distribution.keys():
            self.multiply(hypothesis, self.likelihood(data, hypothesis))

        self.normalize()
