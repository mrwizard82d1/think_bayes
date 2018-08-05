import think_bayes


class CookieEating(think_bayes.Suite):
    def __init__(self):
        think_bayes.Suite.__init__(self, ['Bowl 1', 'Bowl 2'])

        self.bowl_1 = dict(vanilla=30, chocolate=10)
        self.bowl_2 = dict(vanilla=20, chocolate=20)

    def likelihood(self, data, hypothesis):
        """Return the likelihood of observing `data` if `hypothesis` is true."""
        if hypothesis == 'Bowl 1':
            return self.bowl_1[data]
        else:
            return self.bowl_2[data]

