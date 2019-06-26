import math

def polysum(n, s):
  """
  Params:
    n is the number of sides of the polygon, int
    s is the length of a side

  Returns the sum of the area and the perimeter squared, rounded to 4 decimal places 
  """
  # Formula for area of a polygon
  a = (.25*n*s**2)/(math.tan(math.pi/n))

  pSquared = (s * n) ** 2

  return round(a + pSquared, 4)