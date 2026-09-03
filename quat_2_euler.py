## Quaternions to Euler Angles
## Spherical Linear Interpolation of Quaternions
## Author: Luka Bjellos
## Useful sources:
##  Wikipedia: https://en.wikipedia.org/wiki/Quaternion

import numpy as np

# Uses q = (w,x,y,z)
def quat_2_euler(q):

    theta1 = 0
    theta2 = 0
    theta3 = 0

    return theta1, theta2, theta3