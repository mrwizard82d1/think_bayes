import fractions
import thinkbayes


class Cookie(thinkbayes.Pmf):

    def __init__(self, hypotheses):
        super(Cookie, self).__init__()
        self.mixes = {'Bowl 1': {'vanilla': fractions.Fraction(30, 40),
                                 'chocolate': fractions.Fraction(10, 40)},
                      'Bowl 2': {'vanilla': fractions.Fraction(20, 40),
                                 'chocolate': fractions.Fraction(20, 40)}}

        # All hypotheses have equal mass
        for hypothesis in hypotheses:
            self.set(hypothesis, 1)

        self.normalize()

    def update(self, data):
        """Update this Pmf using the `likelihood` of `data` given a hypothesis."""
        for hypothesis in self.values():
            self.multiply(hypothesis, self.likelihood(data, hypothesis))

        self.normalize()

    def likelihood(self, data, hypothesis):
        return self.mixes[hypothesis][data]
