def posterior(prior, likelihood, normalizing_factor):
    """An implementation of canonincal Bayes law."""
    result = (prior * likelihood) / normalizing_factor

    return result
