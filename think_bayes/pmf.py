"""Defines the class modeling a probability mass function."""


import fractions


class Pmf:
    """Models a probability mass function."""

    def __init__(self):
        self.mass = {}

    def probability(self, value):
        """Return the probability mass for `value`."""
        return self.mass[value]

    def likelihood(self, data, hypothesis):
        """Calculate the likelihood of seeing `data` if `hypothesis` is true."""
        raise NotImplementedError

    def increment(self, value):
        """Increment the mass of value in my mass."""
        self.mass[value] = (self.mass.get(value, 0) + 1)

    def multiply(self, value, factor):
        """Multiply the mass of value by factor."""
        self.mass[value] = (self.mass.get(value, 0) * factor)

    def normalize(self):
        """Normalize my mass into an actual probability."""
        normalized_mass = dict([(vm[0], fractions.Fraction(vm[1], sum(self.mass.values()))) for
                                vm in self.mass.items()])
        self.mass = normalized_mass

    def set(self, value, mass):
        """Set the probability mass of value."""
        try:
            self.mass[value] = mass
        except TypeError:
            for v in value:
                self.set(v, mass)

    def update(self, data):
        """Update the probability mass after seeing `data`."""
        for hypothesis in self.mass.keys():
            likelihood = self.likelihood(data, hypothesis)
            self.multiply(hypothesis, likelihood)

        self.normalize()
