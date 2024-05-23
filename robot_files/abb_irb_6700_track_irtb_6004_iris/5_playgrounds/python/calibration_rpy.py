###############################
#For calculating quaternion
#Jingwen Wang
#jingwen.wang@epfl.ch
###############################

import numpy as np
from compas.geometry import Rotation, Transformation, Translation, Vector, Frame, Point, Quaternion

w = 1
x = 0.000334521
y = 0.000334521
z = 0.0000178281
Q = Quaternion(w, x, y,z)
R = Rotation.from_quaternion(Q)

rpy = R.euler_angles(static=True, axes ='xyz')

print([*rpy])