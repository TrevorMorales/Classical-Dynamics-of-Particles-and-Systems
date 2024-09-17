import matplotlib.pyplot as plt
import numpy as np
import math
import os

Directory = os.path.dirname(__file__)

ConstantA = 0.0005
ConstantK = 0.001
InitialVelocity = 40

Steps = 10000
dT = 0.01
Time = np.zeros((Steps))
Force = np.zeros((Steps))
Acceleration = np.zeros((Steps))
Velocity = np.zeros((Steps))
Position = np.zeros((Steps))
Mass = 2
Velocity[0] = InitialVelocity

for i in range(1,Steps):
    Time[i] = i * dT
    Force[i] = -Mass * ConstantK * (Velocity[i-1] * Velocity[i-1] * Velocity[i-1] + ConstantA * ConstantA * Velocity[i-1])
    Acceleration[i] = Force[i] / Mass
    Velocity[i] = Velocity[i-1] + Acceleration[i-1] * dT
    Position[i] = Position[i-1] + Velocity[i-1] * dT

plt.plot(Velocity, Time)
plt.ylabel("Velocity (m/s)")
plt.xlabel("Time (s)")
plt.savefig(Directory + '/2-13_Velocity_v_Time')
plt.show()
plt.plot(Time, Position)
plt.ylabel("Position (m)")
plt.xlabel("Time (s)")
plt.savefig(Directory + '/2-13_Position_v_Time')
plt.show()
# m, k, a constants
# RetardingForce = m * k * (v * v * v + a * a * v)