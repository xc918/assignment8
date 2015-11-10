#Author: Xing Cui
#NetID: xc918
#Data: 11/08

import unittest
from unittest import TestCase
import investment


class hw8_unittest(TestCase):
	"""This is the test for assignment8."""
	def setUp(self):
		pass

	def test_investment(self):
		x = investment.investment(1000)
		self.assertEqual(x.initial_investment, 1000)

	def test_trails(self):
		trails = 10000
		x = investment.investment(1000)
		self.assertTrue(len(x.daily_investment(10,trails))==trails)

if __name__ == '__main__':
    unittest.main()