## rotmat_2_euler
## Rotation Matrix to Euler Angles (3-2-1 & 3-1-3)
## Author: Luka Bjellos
## Useful sources:
##  https://academicflight.com/articles/kinematics/rotation-formalisms/euler-angles/

import numpy as np

def rotmat_2_euler(R,sequence):
    theta = np.empty(3)

    if sequence == "3-2-1": # roll, pitch, yaw
        
        theta[0] = np.atan2(R[2,1],R[2,2])
        theta[1] = -np.arcsin(R[2,0])
        theta[2] = np.atan2(R[1,0],R[0,0])

        if np.abs(theta[1] - np.pi/2) < 0.01:
            theta[0] = 0
            theta[1] = np.pi/2
            theta[2] = np.atan2(R[0,1],R[1,1])

        elif np.abs(theta[1] + np.pi/2) < 0.01:
            theta[0] = 0
            theta[1] = -np.pi/2
            theta[2] = -np.atan2(R[0,1],R[1,1])

    elif sequence == "3-1-3": # alpha, beta, gamma / RAAN, i, argp

        theta[0] = np.atan2(R[0,2],-R[1,2])
        theta[1] = np.arccos(R[2,2])
        theta[2] = np.atan2(R[2,0],R[2,1])

        if np.abs(theta[1]) < 0.01:
            theta[0] = np.atan2(-R[0,1],R[0,0])
            theta[1] = 0
            theta[2] = 0

        elif np.abs(theta[1] - np.pi) < 0.01:
            theta[0] = np.atan2(R[0,1],-R[0,0])
            theta[1] = np.pi
            theta[2] = 0

    else:
        print("Invalid sequence, input \"3-2-1\" or \"3-1-3\" as a string.")
        return

    return theta