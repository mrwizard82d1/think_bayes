"""
According to the CDC, "Compared to smokers, men who smoke are about 23 times more likely to develop lung cancer and
women who smoke are about 13 times more likely."

If you learn a woman has been diagnosed with lung cancer, and you know nothing else about her, what is the probability
that she is a smoker?
"""

import fractions


def hypotheses():
    """
    :return: An enumeration of the hypotheses.
    """

    return {'A': 'The woman was a smoker',
            'B': 'The woman was not a smoker'}


def priors():
    """
    :return: The prior probabilities for each hypothesis.
    """

    return {hypotheses().keys()[0]: 17.9,
            hypotheses().keys()[1]: 82.1}


def likelihoods():
    """
    :return: The likelihood that the woman contracted lung cancer given ...
    """

    return {hypotheses().keys()[0]: 13,
            hypotheses().keys()[1]: 1}


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
