## slerp
## Spherical linear interpolation of quaternions
## Useful sources:
##  MATLAB: https://www.mathworks.com/help/nav/ref/quaternion.slerp.html
##  Wikipedia: https://en.wikipedia.org/wiki/Spherical_linear_interpolation
##  Blog: https://www.euclideanspace.com/maths/algebra/realNormedAlgebra/quaternions/slerp/index.htm

import numpy as np

# Uses q = (w,x,y,z)
def slurp(quat1, quat2, t, method):
    qm = np.zeros(4)



    return qm

# Test case
quaternion_1 = np.array([1,0,0,0])
quaternion_2 = np.array([0,1,0,0])
interp_coef = 0.5
Method = "Short" # Can be "Short" or "Long"

print(slerp(quaternion_1, quaternion_2, interp_coef, Method))