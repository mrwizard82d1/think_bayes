

import think_bayes


class Suite(think_bayes.Pmf):
    """Model a probability mass suite.

    A suite is a Bayesian problem in which all hypotheses are equally likely; that is,
    an uninformative prior.
    """

    def __init__(self, hypotheses):
        think_bayes.Pmf.__init__(self)

        self.set(list(hypotheses), 1)
        self.normalize()

    def update(self, data):
        """Update my probability mass on seeing `data`."""
        for hypothesis in self.values():
            likelihood = self.likelihood(data, hypothesis)
            self.multiply(hypothesis, likelihood)

        self.normalize()

    def likelihood(self, data, hypothesis):
        """Return the likelihood of observing `data` if `hypothesis` is true."""
        raise NotImplementedError
