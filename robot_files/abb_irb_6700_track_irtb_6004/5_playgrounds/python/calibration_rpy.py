###############################
#For calculating quaternion
#Jingwen Wang
#jingwen.wang@epfl.ch
###############################

import numpy as np
from compas.geometry import Rotation, Transformation, Translation, Vector, Frame, Point, Quaternion

q1 = 1
q2 = -0.000156286
q3 = -0.000156286
q4 = 0.000221566
Q = Quaternion(q1, q2, q3, q4)
R = Rotation.from_quaternion(Q)

rpy = R.euler_angles(static=True, axes ='xyz')

print([*rpy])
