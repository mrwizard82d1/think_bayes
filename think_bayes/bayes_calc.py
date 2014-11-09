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
