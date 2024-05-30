import unittest
from foo_param.core import foo_parameterization

class TestFooParameterization(unittest.TestCase):
    def test_foo_parameterization(self):
        self.assertAlmostEqual(foo_parameterization(1), 4.1887866666666665)