import functools


class DiachronicCookie:
    def __init__(self, probabilities_of_bowls, probabilities_of_cookies_given_bowls):
        self.probabilities_of_bowls = probabilities_of_bowls
        self.probabilities_of_cookies_given_bowls = probabilities_of_cookies_given_bowls

    def probability(self, bowl, cookie):
        probability_of_hypotheses = self.probabilities_of_bowls[bowl]
        probability_of_data_given_hypothesis = self.probabilities_of_cookies_given_bowls[(cookie, bowl)]

        def reducer(so_far, hypothesis):
            product = self.probabilities_of_bowls[hypothesis] * \
                      self.probabilities_of_cookies_given_bowls[(cookie, hypothesis)]
            reduced = so_far + product

            return reduced

        normalizing_factor = functools.reduce(reducer, self.probabilities_of_bowls.keys(), 0)

        result = (probability_of_hypotheses * probability_of_data_given_hypothesis) / normalizing_factor

        return result
