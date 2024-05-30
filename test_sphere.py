import unittest
from foo_param.sphere import calculate_sphere_volume

class TestSphereVolume(unittest.TestCase):
    def test_calculate_sphere_volume(self):
        self.assertAlmostEqual(calculate_sphere_volume(1), 4.1887866666666665)