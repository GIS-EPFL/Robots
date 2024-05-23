###############################
#For calculating aurora quaternion to iris
#Consider the transformation of axis based on three point calibration
#Jingwen Wang
#jingwen.wang@epfl.ch
###############################

import numpy as np
from compas.geometry import Rotation, Transformation, Translation, Vector, Frame, Point, Quaternion

w = 1
ix = 0.000334521
iy = 0.000334521
iz = 0.0000178281
iQ = Quaternion(w, ix, iy,iz)
iR = Rotation.from_quaternion(iQ)

i_rpy = iR.euler_angles(static=True, axes ='xyz')

# print([*rpy])

ax = -0.000156286
ay = -0.000156286
az = 0.000221566
aQ = Quaternion(w, ax, ay,az)
aR = Rotation.from_quaternion(aQ)

a_rpy = aR.euler_angles(static=True, axes ='xyz')

[x, y, z, row, pitch ,yaw] = [6314.5407114902, 3605.5713818138, 1.9451920794, -0.0068641574, -0.0049381994,-3.1408819908]

T= Translation.from_vector(Vector(x,y,z)) * Rotation.from_euler_angles([row, pitch ,yaw],static = True, axes = "xyz")

i_frame = Frame.from_euler_angles(i_rpy,static=True, axes ='xyz')
a_frame = Frame.from_euler_angles(a_rpy,static=True, axes ='xyz')
print(a_frame)
aini = a_frame.transformed(T)
T_new = Transformation.from_frame_to_frame(Frame.worldXY(), aini)

Scale, Shear, Rotation, Translation, Projection = T_new.decomposed()
rpy = Rotation.euler_angles(static=True, axes ='xyz')
xyz = Translation.translation_vector[0],Translation.translation_vector[1],Translation.translation_vector[2]
print([*xyz,*rpy])