###############################
#For calculating quaternion
#Jingwen Wang
#jingwen.wang@epfl.ch
###############################

import numpy as np
from compas.geometry import Rotation, Transformation, Translation, Vector, Frame, Point, Quaternion

q1 = 1
q2 = 0.000334521
q3 = 0.000334521
q4 = 0.0000178281
Q = Quaternion(q1, q2, q3, q4)
R = Rotation.from_quaternion(Q)

rpy = R.euler_angles(static=True, axes ='xyz')

print([*rpy])
