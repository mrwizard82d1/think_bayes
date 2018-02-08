"""Solve the M&M problem using a Suite."""

import thinkbayes


class M_And_M(thinkbayes.Suite):
    """Models the M&M problem using a Suite."""

    def __init__(self, hypotheses):
        super(M_And_M, self).__init__(hypotheses)

        self.mix94 = {'brown': 30,
                      'yellow': 20,
                      'red': 20,
                      'green': 10,
                      'orange': 10,
                      'tan': 10}
        self.mix96 = {'blue': 24,
                      'green': 20,
                      'orange': 16,
                      'yellow': 14,
                      'red': 13,
                      'brown': 10}
        self.hypothesis_a = {'bag1': self.mix94,
                             'bag2': self.mix96}
        self.hypothesis_b = {'bag1': self.mix96,
                             'bag2': self.mix94}
        self.hypotheses = {'A': self.hypothesis_a,
                           'B': self.hypothesis_b}

    def likelihood(self, data, hypothesis):
        bag, color = data
        mixture = self.hypotheses[hypothesis][bag]
        result = mixture[color]
        return result


if __name__ == '__main__':
    suite = M_And_M('AB')
    suite.update(('bag1', 'yellow'))
    suite.update(('bag2', 'green'))
    suite.print_distribution()

