# -*- coding: utf-8 -*-

from .context import think_bayes

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(think_bayes.hmm())


if __name__ == '__main__':
    unittest.main()
