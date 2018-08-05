"""Defines the class modeling a probability mass function."""


class Pmf:
    """Models a probability mass function."""

    def __init__(self):
        self.mass = {}

    def set(self, value, mass):
        """Set the probability mass of value."""
        try:
            self.mass[value] = mass
        except TypeError:
            for v in value:
                self.set(v, mass)

    def probability(self, value):
        """Return the probability mass for `value`."""
        return self.mass[value]
