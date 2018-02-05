"""
Two people have left traces of their own blood at the scene of a crime. A suspect, Oliver, is tested and found to have
type O blood. The blood groups of the two traces are found to be of type O (a common type in the local population,
having frequency 60%) and of type AB (a rare type, with frequency 1%). Do these data (the blood types found at the
scene) give evidence in favor of the proposition that Oliver was one of the two people whose blood was found at the
scene.
"""

import fractions


def hypotheses():
    """
    :return: An enumeration of the hypotheses.
    """

    return {'A': 'Oliver is one of the people whose blood was found',
            'B': 'Oliver is not one of the people whose blood was found'}


def likelihoods():
    """
    :return: The likelihoods that the blood at the fair was due to Oliver
    """

    return {
        # Probability that the AB sample is from the general population
        'A': fractions.Fraction(1, 100),
        # Probability that O sample is from the general population and AB sample is from the general population
        # or AB sample is from general population and O sample is also from the general population.
        'B': 2 * fractions.Fraction(1, 100) * fractions.Fraction(60, 100)}


def ratio():
    """
    :return: The ratio of the likelihoods of the two hypotheses.
    """

    return likelihoods()['A'] / likelihoods()['B'];


if __name__ == '__main__':
    print('The Bayes ratio = {}'.format(ratio()))
    print('Since the Bayes ratio is *less than* 1, the blood samples are slightly exculpatory.')
