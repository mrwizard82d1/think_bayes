"""Defines a Bayesian probability calculator."""


__author__ = 'l.jones'


def posterior(prior, likelihood, total=1):
    """Calculate the posterior probability."""

    return prior * likelihood / total
