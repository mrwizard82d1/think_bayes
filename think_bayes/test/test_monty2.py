import unittest
import think_bayes


class TestMonty(unittest.TestCase):

    def test_monty_random(self):
        sut = think_bayes.Monty2('ABC')
        sut.update('B')
        sut.print_distribution()


if __name__ == '__main__':
    unittest.main()
