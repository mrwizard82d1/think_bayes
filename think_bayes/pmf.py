import fractions


class Pmf:
    """Models a probability mass function.

    A probability mass function is a mapping between a value and a probability mass.

    In some situations, the probability mass is an actual probability.
    """

    def __init__(self):
        """Construct an instance."""
        self._map = {}

    def __repr__(self):
        """Return a human-readable representation of myself."""
        return f'Pmf(_map={self._map})'

    def increment(self, value, by_amount=1):
        """Increments the probability mass for value by_amount."""
        self._map[value] = self._map.get(value, 0) + by_amount

    def normalize(self):
        """Convert all my masses to probabilities."""
        self._map = {v: fractions.Fraction(m, sum(self._map.values())) for v, m in self._map.items()}

    def probability(self, value):
        """Returns the probability mass for value."""
        return self._map[value]

    def set(self, value, mass):
        """Set the probability mass for value."""
        self._map[value] = mass
