import fractions

import think_bayes


class CookieEating(think_bayes.Suite):
    """Models the cookie problem - with eating!"""

    def __init__(self, hypotheses):
        super().__init__(hypotheses, use_fractions=True)
        self._mixes = {'bowl 1': dict(vanilla=30, chocolate=10),
                       'bowl 2': dict(vanilla=20, chocolate=20)}

    def likelihood(self, data, hypothesis):
        result = fractions.Fraction(self._mixes[hypothesis][data], sum(self._mixes[hypothesis].values()))
        return result

    def eat_cookie(self, cookie, bowl):
        """Eat the cookie drown from the bowl."""
        self._mixes[bowl][cookie] -= 1
