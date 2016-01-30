from math import sin, cos, pi

from config import latitude, longditude, target_x_degrees, target_z_degrees

def spherical_to_cartesian(azimuth, inclination, radius=1):
  ''' Azimuth is the number of radians across the horizon
      Inclination is the number of radians from the zenith
      returns x, y, z coordinates in radians where:
      x runs east/west
      y runs north/south
      z runs up/down
  ''' 
  x = radius * sin(inclination) * cos(azimuth)
  y = radius * sin(inclination) * sin(azimuth)
  z = radius * cos(inclination)
  return (x, y, z)

def normal_vector(sun_vector, growbed_vector):
  ''' The normal vector describes the direction we want the heliostat to point.
      In this case, that's half way between the sun and the location we want to point to.
  '''
  sun_x, sun_y, sun_z = spherical_to_cartesian(sun_vector)
  normal_x = (growbed_x - sun_x)/2 + sun_x
  normal_z = sun_z/2
  return normal_x, normal_z
  
# def normal_vector_to_motor_coordinates(normal_vector):
#   normal_x, normal_z = 
#   coord_6 = 
#   coord_4 = 

def degrees_to_radians(degrees):
  radians = degrees * pi/180
  return radians

def radians_to_degrees(radians):
  degrees = radians * 180/pi
  return degrees

def target_coords(target_x_degrees, target_z_degrees):
  target_x = degrees_to_radians((target_x_degrees + 90) % 360)
  target_z = degrees_to_radians(target_z_degrees)
  return target_x, target_z