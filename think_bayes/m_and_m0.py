"""
...Mars, Inc., which makes M&M's, changes the mixture of colors from time to time.

In 1995, they introduced blue M&M's. Before then, the color mix in a bag of plain M&M's was:

- 30% brown
- 20% yellow
- 20% red
- 10% green
- 10% orange
- 10% tan

Afterward it was:

- 24% blue
- 20% green
- 16% orange
- 14% yellow
- 13% red
- 13% brown

Suppose a friend of mine has two bags of M&M's, and he tells me that one is from 1994 and one from 1996. He won't tell
me which is which, but he gives me one M&M from each bag, One is yellow and one is green. What is the probability that
the yellow one came from the 1994 bag?

The first step is to enumerate the hypotheses:

- Bag 1 is from 1994 (therefore, bag 2 is from 1996)
- Bag 1 is from 1996 (therefore, bag 2 is from 1994)
"""

import fractions


def hypotheses():
    """
    :return: An enumeration of the hypotheses.
    """

    return ['bag1_1994', # bag 2 from 1996
            'bag1_1996'] # bag 2 from 1994


def priors():
    """
    :return: The prior probabilities for each hypothesis.
    """

    return {hypotheses()[0]: fractions.Fraction(1, 2),
            hypotheses()[1]: fractions.Fraction(1, 2)}


def likelihoods():
    """
    :return: The likelihood of yellow from bag1 and green from bag2
    """

    return {hypotheses()[0]: 20 * 20,
            hypotheses()[1]: 14 * 10}


def posteriors():
    """
    :return: The posteriors for all the hypotheses.
    """

    products = {hypothesis: priors()[hypothesis] * likelihoods()[hypothesis] for hypothesis in hypotheses()}
    total_probability = sum(products.values())
    return {hypothesis: products[hypothesis] / total_probability for hypothesis in hypotheses()}


if __name__ == '__main__':
    print('Probability that yellow is from 1994 and green from 1996 = {}', posteriors()['bag1_1994'])
    print('Probability that yellow is from 1996 and green from 1994 = {}', posteriors()['bag1_1996'])

