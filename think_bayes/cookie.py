"""
Solution to the "cookie problem" using the `Pmf` class.
"""

import fractions
import thinkbayes


bowl1_hypothesis = 'Bowl 1'
bowl2_hypothesis = 'Bowl 2'

def vanilla_posterior():
    """Calculate the posterior probability that the vanilla cookie was drawn from 'Bowl 1'."""

    # Randomly draw a cookie from either bowl with equal probability.
    prior = thinkbayes.Pmf()
    prior.set(bowl1_hypothesis, fractions.Fraction(1, 2))
    prior.set(bowl2_hypothesis, fractions.Fraction(1, 2))

    # Multiply the prior for each hypothesis with the likelihood of drawing a vanilla cookie given that hypothesis.
    prior.multiply(bowl1_hypothesis, fractions.Fraction(30, 40))
    prior.multiply(bowl2_hypothesis, fractions.Fraction(20, 40))

    # Convert the probability mass back into a probability (normalize)
    prior.normalize()

    return prior.probability(bowl1_hypothesis)


if __name__ == '__main__':
    print('The posterior probability that the vanilla cookie came from {} = {}'.format(bowl1_hypothesis,
                                                                                       vanilla_posterior()))
