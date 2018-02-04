"""
There are many variations of the Monty Hall problem. One of the strengths of the Bayesian approach is that it
generalizes to handle these variations.

For example, suppose that Monty always chooses B if he can, and only chooses C if he has to (because the car is behind
B). In that case the revised table has different likelihoods below:
"""

import fractions


def hypotheses():
    """
    :return: An enumeration of the hypotheses.
    """

    return {'A': 'the car is behind Door A',
            'B': 'the car is behind Door B',
            'C': 'the car is behind Door C'}


def priors():
    """
    :return: The prior probabilities for each hypothesis.
    """

    return {hypotheses().keys()[0]: fractions.Fraction(1, 3),
            hypotheses().keys()[1]: fractions.Fraction(1, 3),
            hypotheses().keys()[2]: fractions.Fraction(1, 3)}


def likelihoods():
    """
    :return: The likelihood of yellow from bag1 and green from bag2
    """

    return {hypotheses().keys()[0]: 1,
            hypotheses().keys()[1]: 0,
            hypotheses().keys()[2]: 1}


def posteriors():
    """
    :return: The posteriors for all the hypotheses.
    """

    products = {hypothesis: priors()[hypothesis] * likelihoods()[hypothesis] for hypothesis in hypotheses()}
    total_probability = sum(products.values())
    return {hypothesis: products[hypothesis] / total_probability for hypothesis in hypotheses()}


if __name__ == '__main__':
    for hypothesis in sorted(hypotheses().keys()):
        print('The probability that {} = {}'.format(hypotheses()[hypothesis], posteriors()[hypothesis]))
