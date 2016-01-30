import unittest
import math
from conversions import spherical_to_cartesian

class TestConversions(unittest.TestCase):
  def test_spherical_to_cartesian():
    azimuth = math.pi/2 # East
    inclination = 0 # Horizon
    raise Exception
    self.assertEqual(spherical_to_cartesian(azimuth, inclination), 0)
