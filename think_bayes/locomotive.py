"""Defines models of the locomotive problem."""


import think_bayes


class LocomotiveUniform(think_bayes.Suite):
    """Models a solution assuming a uniform prior."""

    def likelihood(self, data, hypothesis):
        """Calculate the likelihood of the data given the hypothesis."""
        if hypothesis < data:
            return 0
        else:
            return 1.0 / hypothesis
