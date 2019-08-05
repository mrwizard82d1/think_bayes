import fractions

from .pmf import Pmf


class Cookie(Pmf):
    """Models the cookie problem using Pmf's."""

    def __init__(self, hypotheses):
        """Construct an instance with the specified hypotheses."""
        super().__init__()

        # Use a uniform prior.
        for hypothesis in hypotheses:
            self.set(hypothesis, 1)
        self.normalize()

    def update(self, data):
        """Update the probabilities of each hypothesis after seeing data."""

        for hypothesis in self._map.keys():
            self.multiply(hypothesis, self.likelihood(data, hypothesis))
        self.normalize()

    def likelihood(self, data, hypothesis):
        """Calculate the likelihood of data given the hypothesis."""
        mixes = {'bowl 1': {'vanilla': fractions.Fraction(30, (30 + 10)),
                            'chocolate': fractions.Fraction(10, (30 + 10))},
                 'bowl 2': {'vanilla': fractions.Fraction(20, (20 + 20)),
                            'chocolate': fractions.Fraction(20, (20 + 20))}}

        return mixes[hypothesis][data]
