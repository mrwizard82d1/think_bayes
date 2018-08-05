import fractions


class MontyHallTable:
    def __init__(self):
        self.hypotheses = 'ABC'
        self.prior = {'A': fractions.Fraction(1, 3),
                      'B': fractions.Fraction(1, 3),
                      'C': fractions.Fraction(1, 3)}
        self.likelihood = {'A': 1, 'B': 1, 'C': 1}
        self.probability = {}
        self.product = {}

        self.calculate_product()

    def open_door_and_no_car(self, door):
        """Update the probabilities after observing no car behind `door`."""

    def calculate_product(self):
        """Calculate the product of my prior ond likelihood."""
        for hypothesis in self.prior.keys():
            self.product[hypothesis] = self.prior[hypothesis] * self.likelihood[hypothesis]

    def posterior(self, door):
        """Return the posterior probabilities."""

        return self.probability[door]
