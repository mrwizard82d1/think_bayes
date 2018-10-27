def diachronic(data, priors, likelihoods, normalizing_factor):
    """Implement the diachronic interpretation of Bayes' law:

        P(H | D) = ( P(H) * P(D | H) ) / P(D)

    where:

        H is the hypothesis
        D is the data, or evidence

    P(H) is also called the prior probability; that is, the probability that the hypothesis is true *before* seeing any
    data. P(D | H) is the likelihood: the probability of seeing the data given the hypothesis is true. P(D) is the
    normalizing constant or the probability of seeing the data under any hypothesis. Although it is different to
    calculate generally, if the hypotheses are mutually exclusive and exhaustive, then P(D) is the total probability:

        P(D) = P(H-sub-1) * P(D | H-sub-1) + P(H-sub-2) * P(D | H-sub-2) + ... + P(H-sub-n) * P(D | H-sub-n)
    """

    posteriors = {}
    for hypothesis in iter(priors):
        posteriors[hypothesis] = (priors[hypothesis] * likelihoods[(data, hypothesis)]) / normalizing_factor;

    return posteriors
