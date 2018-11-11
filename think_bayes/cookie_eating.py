import fractions

import think_bayes


class CookieEating(think_bayes.Suite):
    """Models the cookie problem - with eating!"""

    def __init__(self, hypotheses):
        super().__init__(hypotheses, use_fractions=True)
        self._mixes = {'bowl 1': dict(vanilla=30, chocolate=10),
                       'bowl 2': dict(vanilla=20, chocolate=20)}

    def eat_cookie(self, data):
        """Eat the cookie drown from the bowls"""
        cookie, bowl = data
        self._mixes[bowl][cookie] -= 1

    def likelihood(self, data, hypothesis):
        result = fractions.Fraction(self._mixes[hypothesis][data], sum(self._mixes[hypothesis].values()))
        return result

    def update(self, data):
        """Update the distribution after seeing data.

        This method plays the role of _Template Method_ in the _Template Method_ design pattern.

        In that role, this method defines an algorithm to update the distribution in terms of the
        _Primitive_ method, `likelihood`.
        """
        cookie, bowl = data
        super().update(cookie)

        self.eat_cookie(data)
