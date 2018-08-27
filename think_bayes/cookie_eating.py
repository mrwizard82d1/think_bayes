import fractions

import think_bayes


class CookieEating(think_bayes.Suite):

    vanilla_bowl_1 = ('Vanilla', 'Bowl 1')
    vanilla_bowl_2 = ('Vanilla', 'Bowl 2')
    chocolate_bowl_1 = ('Chocolate', 'Bowl 1')
    chocolate_bowl_2 = ('Chocolate', 'Bowl 2')

    def __init__(self):
        think_bayes.Suite.__init__(self, ['Bowl 1', 'Bowl 2'])

        self.mixes = {'Bowl 1': Bowl(30, 10),
                      'Bowl 2': Bowl(20, 20)}

    def likelihood(self, data, hypothesis):
        """Calculate the likelihood of `data `if `hypothesis` is true."""

        mixture_for_hypothesis = self.mixes[hypothesis]
        numerator = mixture_for_hypothesis.__dict__[data.lower()]
        result = fractions.Fraction(numerator, (mixture_for_hypothesis.vanilla + mixture_for_hypothesis.chocolate))

        return result

    def update(self, data):
        """Update my probability mass on seeing `data`."""

        cookie, bowl = data
        for hypothesis in self.values():
            likelihood = self.likelihood(cookie, hypothesis)
            self.multiply(hypothesis, likelihood)

        self.normalize()

        # Update my bowls based on data
        prior_bowl_1 = self.mixes['Bowl 1']
        prior_bowl_2 = self.mixes['Bowl 2']
        if cookie == 'Vanilla' and bowl == 'Bowl 1':
            posterior_bowl_1 = Bowl(prior_bowl_1.vanilla - 1, prior_bowl_1.chocolate)
            self.mixes = {'Bowl 1': posterior_bowl_1, 'Bowl 2': prior_bowl_2}
        elif cookie == 'Vanilla' and bowl == 'Bowl 2':
            posterior_bowl_2 = Bowl(prior_bowl_2.vanilla - 1, prior_bowl_2.chocolate)
            self.mixes = {'Bowl 1': prior_bowl_1, 'Bowl 2': posterior_bowl_2}
        elif cookie == 'Chocolate' and bowl == 'Bowl 1':
            posterior_bowl_1 = Bowl(prior_bowl_1.vanilla, prior_bowl_1.chocolate - 1)
            self.mixes = {'Bowl 1': posterior_bowl_1, 'Bowl 2': prior_bowl_2}
        elif cookie == 'Chocolate' and bowl == 'Bowl 2':
            posterior_bowl_2 = Bowl(prior_bowl_2.vanilla, prior_bowl_2.chocolate - 1)
            self.mixes = {'Bowl 1': prior_bowl_1, 'Bowl 2': posterior_bowl_2}
        else:
            raise ValueError('Unrecognized cookie, "{}", or bowl, "{}".'.format(cookie, bowl))


class Bowl:
    def __init__(self, vanilla, chocolate):
        self.vanilla = vanilla
        self.chocolate = chocolate

    def __repr__(self):
        return 'Bowl(vanilla={}, chocolate={})'.format(self.vanilla, self.chocolate)
