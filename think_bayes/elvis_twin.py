"""
Elvis Presley had a twin brother who died at birth. What is the probability that Elvis was fan identical twin?
"""

import fractions


def hypotheses():
    """
    :return: An enumeration of the hypotheses.
    """

    return {'A': 'Elvis was an identical twin',
            'B': 'Elvis was a fraternal twin'}


def priors():
    """
    :return: The prior probabilities for each hypothesis.
    """

    return {hypotheses().keys()[0]: 8,
            hypotheses().keys()[1]: 92}


def likelihoods():
    """
    :return: The likelihood that Elvis' twin was male given that he was ...

    The key to this problem is realizing that the sex of the twin provides relevant information.
    """

    return {hypotheses().keys()[0]: 1, # Elvis twin was male given that he was an identical twin
            hypotheses().keys()[1]: fractions.Fraction(1, 2)} # Elvis twin was male given that he was a fraternal twin


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
