"""Unit tests for the locomotive problem."""


import unittest

import think_bayes


class TestLocomotiveUniform(unittest.TestCase):
    """Defines unit tests for the locomotive problem with a uniform prior."""

    def test_correct_posterior_when_constructed(self):
        # Any number of locomotives from 1 to 1000, inclusive. All equally likely.
        prior = range(1, 1000 + 1)
        sut = think_bayes.LocomotiveUniform(prior)

        sut.update(60)

        self.assertEqual(float(sut.posterior()[1]), 0)
        self.assertEqual(float(sut.posterior()[59]), 0)
        self.assertAlmostEqual(float(sut.posterior()[60]), 0.005905, 6)
        self.assertAlmostEqual(float(sut.posterior()[370]), 9.57635e-4, 9)
        self.assertAlmostEqual(float(sut.posterior()[680]), 5.21066e-4, 9)
        self.assertAlmostEqual(float(sut.posterior()[1000]), 3.54325e-4, 9)

    def test_correct_posterior_mean_when_updated(self):
        maximum_trains = [1000, 500, 2000]
        # Any number of locomotives from 1 to maximum trains, inclusive. All equally likely.
        sut = dict([(m, think_bayes.LocomotiveUniform(range(1, m + 1))) for m in maximum_trains])

        for m in maximum_trains:
            sut[m].update(60)

        expected = {1000: 333, 500: 207, 2000: 552}
        for max_train, mean_trains in expected.items():
            self.assertEqual(int(sut[max_train].mean()), mean_trains)

    def test_correct_posterior_mean_many_updates(self):
        maximum_trains = [1000, 500, 2000]
        # Any number of locomotives from 1 to maximum trains, inclusive. All equally likely.
        sut = dict([(m, think_bayes.LocomotiveUniform(range(1, m + 1))) for m in maximum_trains])

        for m in maximum_trains:
            for train_number in [60, 30, 90]:
                sut[m].update(train_number)

        expected = {1000: 164, 500: 152, 2000: 171}
        for max_train, mean_trains in expected.items():
            self.assertEqual(round(sut[max_train].mean()), mean_trains)

