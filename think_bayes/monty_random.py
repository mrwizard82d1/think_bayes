"""
The Monty Hall problem is based on one of the regular games on the show. If you are on the show, here's what happens:

- Monty shows yu three closed doors and tells yuo that there is a prize behind each door: one prize is a car, the other
two are less valuable prizes like peanut butter and fake finger nails. The prizes are arranged at random.
- The object of the game is to guess which door has the car. if you guess right, you get to keep the car.
- You pick a door, which we will call Door A. We'll call the other doors B and C.
- Before opening the door you choose, Monty increases the suspense by opening either Door B or C, whichever does not
have the car. (If the car is actually behind Door A, Monty can safely open B or C, so he chooses one at random.)
- Then Monty offers you the option to stick with your original choice or switch to the one remaining open door.

The question is, should you "stick" or "switch" or does it make no difference?
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

    return {hypotheses().keys()[0]: fractions.Fraction(1, 2),
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
