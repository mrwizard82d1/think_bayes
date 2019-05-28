# -*- coding: utf-8 -*-


def bayes_equation(p_of_a, p_of_b_given_a, p_of_b):
    return (p_of_a * p_of_b_given_a) / p_of_b


def diachronic(prob_hypothesis, prob_data_given_hypothesis, normalizing_factor):
    return (prob_hypothesis * prob_data_given_hypothesis) / normalizing_factor
