"""Defines the class modeling a probability mass function."""


class Pmf:
    """Models a probability mass function."""

    def __init__(self):
        self.mass = {}

    def increment(self, value):
        """Increment the mass of value in my mass."""
        self.mass[value] = (self.mass.get(value, 0) + 1)

    def probability(self, value):
        """Return the probability mass for `value`."""
        return self.mass[value]

    def set(self, value, mass):
        """Set the probability mass of value."""
        try:
            self.mass[value] = mass
        except TypeError:
            for v in value:
                self.set(v, mass)
