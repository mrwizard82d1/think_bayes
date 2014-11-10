"""Defines the BayesCalc(ulator) class."""


__author__ = 'l.jones'


class BayesCalc():
    """Models a Bayes probability calculator."""

    def __init__(self, hypotheses):
        """Initializes an instance with hypotheses."""

        if len(hypotheses) == 0:
            raise ValueError('No hypothesis.')

        self.hypotheses = hypotheses[:]
        if len(hypotheses) == 1:
            self.hypotheses.append('not {0}'.format(hypotheses[0]))

        self.priors = {}
        self.likelihoods = {}
        self.posteriors = {}

    def update(self):
        """Update my posteriors."""

        # If one prior not set, set it to the remainder
        if len(self.hypotheses) == len(self.priors) + 1:
            all_hypotheses = set(self.hypotheses)
            all_prior_hypotheses = set(self.priors.keys())
            other_hypotheses = all_hypotheses - all_prior_hypotheses
            self.priors[list(other_hypotheses)[0]] = 1 - sum(self.priors.values())
        elif len(self.hypotheses) != len(self.priors):
            raise ValueError('Too few priors: {0}'.format(self.priors.keys()))

        for ((data, hypothesis), likelihood) in self.likelihoods.items():
            self.posteriors[(hypothesis, data)] = likelihood * self.priors[hypothesis]
        total = sum(self.posteriors.values())
        for k in self.posteriors:
            self.posteriors[k] /= total



