"""Defines the MontyHallRandomPickTable class."""


import fractions

from think_bayes.monty_hall_table import MontyHallTable


class MontyHallRandomPickTable(MontyHallTable):
    """Models the Monty Hall probability problem using the Bayesian table method.

    In this implementation, Monty Hall randomly picks door "B" or "C" which does
    not have the car behind it.
    """

    def open_door_and_no_car(self, door):
        """Update the probabilities after observing no car behind `door`."""

        if door == 'B':
            self.likelihood['A'] = fractions.Fraction(1, 2)
            self.likelihood['B'] = 0
            self.likelihood['C'] = 1

        self.calculate_product()

        normalizing_factor = sum(self.product.values())
        for hypothesis in self.prior.keys():
            self.probability[hypothesis] = self.product[hypothesis] / normalizing_factor
