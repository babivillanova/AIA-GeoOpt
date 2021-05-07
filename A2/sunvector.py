""" Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable
        b: The b output variable
        c: The c output variable
"""

import Rhino.Geometry as rg
import math

#create a sun vector

#1. create a Sphere at point (0,0,0) with radius 1 and output it to a
#output the sphere to a
center = rg.Point3d(0,0,0)
a = rg.Sphere(center,1)


#2. evaluate a point in the sphere using rg.Sphere.PointAt() at coordintes x and y
#the point should only be on the upper half of the sphere (upper hemisphere)
#the angles are in radians, so you might want to use math.pi for this
#output the point to b

b = rg.Sphere.PointAt(a,x*math.pi*2,y*math.pi)


#create a vector from the origin  and reverse the vector
#keep in mind that Reverse affects the original vector
#output the vector to c
line = rg.Vector3d(b)
linerev = rg.Vector3d.Reverse(line)
c = line