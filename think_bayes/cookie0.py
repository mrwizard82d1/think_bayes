"""
Code from chapter 1.

Suppose there are two bowls of cookies. Bowl 1 contains 30 vanilla  cookies  and 10 chocolate cookies. Bowl 2 contains
20 of each.

Now suppose yu choose one of the bowls at random and, without looking, select a cookie at random. The cookie is vanilla.
What is the probability it came from Bowl 1?
"""

import fractions

def inverse_conditional_probability():
    """
    Using Bayes theorem to calculate the inverse conditional probability.
    :return: None
    """
    p_bowl1 = fractions.Fraction(1, 2) # (unconditional) probability we choose bowl 1
    p_vanilla_given_bowl1 = fractions.Fraction(3, 4) # probability of vanilla given you selected bowl 1
    p_vanilla = fractions.Fraction(50, 80) # probability of selecting a vanilla cookie from either bowl
    # p_vanilla is also known as the total probability of a vanilla cookie.

    p_bowl1_given_vanilla = (p_vanilla_given_bowl1 * p_bowl1) / p_vanilla
    print('Computing the inverse probability.')
    print('P(B1 | V) = {}'.format(p_bowl1_given_vanilla))


def total_probability_of_vanilla_from_any_bowl():
    """
    Calculate the total probability of seeing a vanilla cookie assuming that the hypotheses are:

    - Mutually exclusive
    - Collectively exhaustive
    """
    p_bowl1 = fractions.Fraction(1, 2)
    p_bowl2 = fractions.Fraction(1, 2)
    p_vanilla_given_bowl1 = fractions.Fraction(30, 40)
    p_vanilla_given_bowl2 = fractions.Fraction(20, 40)
    return p_bowl1 * p_vanilla_given_bowl1 + p_bowl2 * p_vanilla_given_bowl2


def diachronic_interpretation():
    """
    Use the diachronic interpretation of Bayes Theorem to calculate the posterior from the likelihood, prior and total
    probability.

    In the diachronic interpretation of Bayes Theorem, H is the hypothesis and D is the observed data

        p(H ps| D) = ( p( H ) * p( D | H ) ) / p( D )

    That is,

    The probability of the hypothesis given the data (the posterior) is the product of the probability of the hypothesis
    (the prior) and the product of the data given the hypothesis (the likelihood) divided by the probability of the data
    independent of the hypotheses (the normalizing factor).

    :return:  None
    """

    p_hypothesis = fractions.Fraction(1, 2) # bowl 1
    p_data_given_hypothesis = fractions.Fraction(30, 40) # vanilla given bowl 1
    p_data = total_probability_of_vanilla_from_any_bowl()
    p_hypothesis_given_data = (p_hypothesis * p_data_given_hypothesis) / p_data

    print('Computing the hypothesis given the data')
    print('P(H | D) = {}'.format(p_hypothesis_given_data))


if __name__ == '__main__':
    inverse_conditional_probability()
    print('\n')
    diachronic_interpretation()

