import fractions

import think_bayes


class CookieEating(think_bayes.Suite):
    def __init__(self):
        think_bayes.Suite.__init__(self, ['Bowl 1', 'Bowl 2'])

        self.mixes = {'Bowl 1': Bowl(30, 10),
                      'Bowl 2': Bowl(20, 20)}

    def likelihood(self, data, hypothesis):
        """Calculate the likelihood of `data `if `hypothesis` is true."""

        mixture_for_hypothesis = self.mixes[hypothesis]
        result = mixture_for_hypothesis.__dict__[data.lower()]

        return result


class Bowl:
    def __init__(self, vanilla, chocolate):
        self.vanilla = vanilla
        self.chocolate = chocolate
