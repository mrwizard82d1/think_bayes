import fractions
import thinkbayes


class Monty(thinkbayes.Pmf):

    def __init__(self, hypotheses):
        super(Monty, self).__init__()

        # All hypotheses have equal mass
        for hypothesis in hypotheses:
            self.set(hypothesis, 1)

        self.normalize()

    def update(self, data):
        """Update this Pmf using the `likelihood` of `data` given a hypothesis."""
        for hypothesis in self.values():
            self.multiply(hypothesis, self.likelihood(data, hypothesis))

        self.normalize()

    @staticmethod
    def likelihood(data, hypothesis):
        if data == hypothesis:
            return 0

        if hypothesis == 'A':
            return fractions.Fraction(1, 2)

        return 1


class MontyB(thinkbayes.Pmf):

    def __init__(self, hypotheses):
        super(MontyB, self).__init__()

        # All hypotheses have equal mass
        for hypothesis in hypotheses:
            self.set(hypothesis, 1)

        self.normalize()

    def update(self, data):
        """Update this Pmf using the `likelihood` of `data` given a hypothesis."""
        for hypothesis in self.values():
            self.multiply(hypothesis, self.likelihood(data, hypothesis))

        self.normalize()

    @staticmethod
    def likelihood(data, hypothesis):
        if data == hypothesis:
            return 0

        return 1

