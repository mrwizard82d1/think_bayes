import think_bayes


class MAndM(think_bayes.Suite):
    """Models a suite for solving the M&M problem."""

    def __init__(self):
        # Different years, 1994 and 1996, have different mixtures of colors.
        self._mix94 = dict(brown=30,
                           yellow=20,
                           red=20,
                           green=10,
                           orange=10,
                           tan=10)
        self._mix96 = dict(blue=24,
                           green=20,
                           orange=16,
                           yellow=14,
                           red=13,
                           brown=13)

        # We have two hypotheses: bag 1 is from 1994 (implies bag 2 is from 1996) and
        # bag 1 is from 1996 (implies bag 2 is from 1994).
        self._hypothesis_a = dict(bag1=self._mix94,
                                  bag2=self._mix96)
        self._hypothesis_b = dict(bag1=self._mix96,
                                  bag2=self._mix94)

        # We code the hypotheses as 'A' and 'B'
        self._hypotheses = dict(A=self._hypothesis_a,
                                B=self._hypothesis_b)

        # Using fractions seems appropriate to this problem.
        super().__init__(self._hypotheses, use_fractions=True)

    def likelihood(self, data, hypothesis):
        """Calculate the likelihood of the data given the hypothesis.

        :data: A tuple containing the bag and the color.
        :hypothesis The hypothesis being analyzed.
        """

        bag, color = data
        mix = self._hypotheses[hypothesis][bag]
        result = mix[color]
        return result
