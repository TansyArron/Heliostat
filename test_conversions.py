import unittest
import math
from conversions import spherical_to_cartesian

class TestConversions(unittest.TestCase):
  def compare_vector(self, vector_one, vector_two):
    print(vector_one)
    self.assertAlmostEqual(vector_one[0], vector_two[0])
    self.assertAlmostEqual(vector_one[1], vector_two[1])

  def test_spherical_to_cartesian_dawn(self):
    test_dict = {
      (0, math.pi/2) : (1.0, 0.0, 0.0),
      (math.pi/4, math.pi/4) : (0.5, 0.5, 0.70710),
      (math.pi/2, 0.0) : (0.0, 0.0, 1.0)
    }
    for key in test_dict.keys():
      self.compare_vector(spherical_to_cartesian(key[0], key[1]), test_dict[key])

  # def test_spherical_to_cartesian_midmorning(self):
  #   azimuth = math.pi/4 # East Southeast = 45
  #   inclination = math.pi/4 # Up = 45
  #   self.compare_vector(spherical_to_cartesian(azimuth, inclination), (0.0, 1.0))

  # def test_spherical_to_cartesian_noon(self):
  #   azimuth = math.pi/2 # South = 90
  #   inclination = 0 # Up = 0
  #   self.compare_vector(spherical_to_cartesian(azimuth, inclination), (0.0, 1.0))


if __name__=="__main__":
    unittest.main()