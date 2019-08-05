# -*- coding: utf-8 -*-


def bayes_equation(p_of_a, p_of_b_given_a, p_of_b):
    return (p_of_a * p_of_b_given_a) / p_of_b


def diachronic(prob_hypothesis, prob_data_given_hypothesis, prob_data_given_any_hypothesis):
    # `prob_hypothesis` aka `prior`
    # `prob_data_given_hypothesis` aka `likelihood`
    # `prob_data_given_any_hypothesis` aka `normalizing constant`
    return (prob_hypothesis * prob_data_given_hypothesis) / prob_data_given_any_hypothesis


class Table:

    def __init__(self, hypotheses, priors, likelihoods):
        self._hypotheses = hypotheses
        self._priors = priors
        self._likelihoods = likelihoods
        self._products = dict([(h, self._priors[h] * self._likelihoods[h]) for h in self._hypotheses])
        self._sum = sum(self._products.values())
        self._posteriors = {h: p / self._sum for (h, p) in self._products.items()}

    def posterior(self, hypothesis):
        return self._posteriors[hypothesis]
