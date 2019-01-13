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


class TestLocomotivePower(unittest.TestCase):
    """Define the unit tests for the locamotive problem using a power law prior."""

    def test_correct_default_exponent_when_constructed(self):
        hypotheses = range(1, 10 + 1)
        sut = think_bayes.LocomotivePower(hypotheses)

        unnormalized_distribution = dict([(h, 1.0 / h) for h in hypotheses])
        expected_distribution = dict([(h, v / sum(unnormalized_distribution.values()))
                                     for (h, v)
                                     in unnormalized_distribution.items()])
        for h in hypotheses:
            self.assertAlmostEqual(sut.posterior()[h], expected_distribution[h], 9)

    def test_correct_posterior_many_observations(self):
        max_trains = [1000, 500, 2000]
        sut = dict([(max_train, think_bayes.LocomotivePower(range(1, max_train + 1))) for max_train in max_trains])
        for max_train in max_trains:
            sut[max_train].update(30)
            sut[max_train].update(60)
            sut[max_train].update(90)

        expected90 = {1000: 3.28063902e-2, 500: 3.29714522e-2, 2000: 3.27858406e-2}
        expected499 = {1000: 3.47157300e-05, 500: 3.48903986e-05, 2000: 3.46939844e-05}
        for mt in max_trains:
            self.assertEqual(0, sut[mt].posterior()[1])
            self.assertEqual(0, sut[mt].posterior()[30])
            self.assertEqual(0, sut[mt].posterior()[60])
            self.assertAlmostEqual(expected90[mt], sut[mt].posterior()[90], 9)
            self.assertAlmostEqual(expected499[mt], sut[mt].posterior()[499], 9)

    def test_correct_mean_many_observations(self):
        max_trains = [1000, 500, 2000]
        sut = dict([(max_train, think_bayes.LocomotivePower(range(1, max_train + 1))) for max_train in max_trains])
        for max_train in max_trains:
            sut[max_train].update(30)
            sut[max_train].update(60)
            sut[max_train].update(90)

        expected_results = {1000: 133, 500: 131, 2000: 134}
        actual_results = dict([(h, sut[h].mean()) for h in max_trains])
        for h in max_trains:
            self.assertEqual(round(actual_results[h]), expected_results[h])

