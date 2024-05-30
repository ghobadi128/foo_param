import unittest
from foo_param.utils import validate_radius

class TestUtils(unittest.TestCase):
    def test_validate_radius(self):
        with self.assertRaises(ValueError):
            validate_radius(-1)