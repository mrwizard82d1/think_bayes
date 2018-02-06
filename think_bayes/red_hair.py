"""
If you meet a man with (natural) red hair, what is the probability that neither of his parents has red hair?
"""

import fractions


def hypotheses():
    """
    :return: An enumeration of the hypotheses.
    """

    return {'A': 'Neither parent has red hair',
            'B': 'Only father has red hair',
            'C': 'Only mother has red hair',
            'D': 'Both parents have red hair'}


def priors():
    """
    :return: The prior probabilities for each hypothesis.
    """

    return {'A': pow(fractions.Fraction(98, 100), 2),
            'B': fractions.Fraction(2, 100) * fractions.Fraction(98, 100),
            'C': fractions.Fraction(98, 100) * fractions.Fraction(2, 100),
            'D': pow(fractions.Fraction(2, 100), 2)}


def likelihoods():
    """
    :return: The likelihood of the hypotheses given child with red hair
    """

    return {'A': fractions.Fraction(1, 4),
            'B': fractions.Fraction(1, 2),
            'C': fractions.Fraction(1, 2),
            'D': 1}


def posteriors():
    """
    :return: The posteriors for all the hypotheses.
    """

    products = {hypothesis: priors()[hypothesis] * likelihoods()[hypothesis] for hypothesis in hypotheses().keys()}
    total_probability = sum(products.values())
    return {hypothesis: products[hypothesis] / total_probability for hypothesis in hypotheses()}


if __name__ == '__main__':
    for hypothesis in sorted(hypotheses().keys()):
        print('The probability that {} = {}'.format(hypotheses()[hypothesis], posteriors()[hypothesis]))
