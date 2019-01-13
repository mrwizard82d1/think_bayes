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


class LocomotivePower(LocomotiveUniform):
    """"Models the locomotive problem using a power law prior."""

    def __init__(self, hypotheses, alpha=1.0):
        # Initialize the distribution ...
        super().__init__(hypotheses)

        # ... And then change it.
        for h in self._hypotheses:
            self.set(h, pow(h, -alpha))
        self.normalize()
