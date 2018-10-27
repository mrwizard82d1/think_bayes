def total_probability(datum, priors, likelihoods):
    """Calculate the total probability of `datum` for a suite of hypotheses.

    A suite is a set of hypotheses that are:

        - Mutually exclusive
        - Exhaustive

    In this situation the total probability is given by the equation:

        P(D) = P(H-sub-1) * P(D | H-sub-1) + P(H-sub-2) * P(D | H-sub-2) + ... + P(H-sub-n) * P(D | H-sub-n)
    """

    result = sum([priors[h] * likelihoods[(datum, h)] for h in iter(priors)])

    return result

