# -*- coding: utf-8 -*-

from .context import think_bayes

import unittest


class TestBayes(unittest.TestCase):

    def test_smoke(self):
        self.assertEqual(2 + 2, 4)


if __name__ == '__main__':
    unittest.main()
