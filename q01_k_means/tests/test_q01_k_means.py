from unittest import TestCase
from ..build import k_means
from inspect import getargspec


class TestK_means(TestCase):
    def test_k_means(self):

        # Input parameters tests
        args = getargspec(k_means)
        self.assertEqual(len(args[0]), 4, "Expected argument(s) %d, Given %d" % (4, len(args[0])))
        self.assertEqual(args[3], (10, 9), "Expected default values do not match given default values")

        # Return type tests
        # Nothing to check here

        # Return value tests
        # Nothing to check here
