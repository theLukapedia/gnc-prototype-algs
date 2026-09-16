## slerp
## Spherical Linear Interpolation of Quaternions
## Author: Luka Bjellos
## Useful sources:
##  MATLAB: https://www.mathworks.com/help/nav/ref/quaternion.slerp.html
##  Wikipedia: https://en.wikipedia.org/wiki/Spherical_linear_interpolation
##  Blog: https://www.euclideanspace.com/maths/algebra/realNormedAlgebra/quaternions/slerp/index.htm

import numpy as np

# Uses q = (w,x,y,z)
def slerp(qa, qb, t):
    qm = np.zeros(4)

    qa = qa / np.linalg.norm(qa)
    qb = qb / np.linalg.norm(qb)

    cosHalfTheta = qa[0] * qb[0] + qa[1] * qa[1] + qa[2] * qb[2] + qa[3] * qb[3]

    if abs(cosHalfTheta) >= 1.0:
        qm = qa
        return qm

    halfThetaRad = np.acos(cosHalfTheta)
    sinHalfTheta = np.sqrt(1.0 - cosHalfTheta ** 2)

    if abs(sinHalfTheta) < 0.001:
        qm[0] = qa[0] * (1-t) + qb[0] * t
        qm[1] = qa[1] * (1-t) + qb[1] * t
        qm[2] = qa[2] * (1-t) + qb[2] * t
        qm[3] = qa[3] * (1-t) + qb[3] * t

    ratioA = np.sin((1 - t) * halfThetaRad) / sinHalfTheta
    ratioB = np.sin(t * halfThetaRad) / sinHalfTheta

    qm[0] = qa[0] * ratioA + qb[0] * ratioB
    qm[1] = qa[1] * ratioA + qb[1] * ratioB
    qm[2] = qa[2] * ratioA + qb[2] * ratioB
    qm[3] = qa[3] * ratioA + qb[3] * ratioB
    
    return qm