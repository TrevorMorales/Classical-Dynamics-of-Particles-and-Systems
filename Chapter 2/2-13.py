import matplotlib.pyplot as plt
import numpy as np
import os
import math

Directory = os.path.dirname(__file__)

ConstantA = 0.05
ConstantK = 0.01
InitialVelocity = 10
Iterations = 5

Steps = 10000000
dT = 0.01
Time = np.zeros((Steps))
Force = np.zeros((Iterations, Steps))
Acceleration = np.zeros((Iterations, Steps))
Velocity = np.zeros((Iterations, Steps))
Position = np.zeros((Iterations, Steps))
Mass = 2

for i in range(Iterations):
    Velocity[i][0] = InitialVelocity + (10 * i)

for j in range(Iterations):
    for i in range(1, Steps):
        Time[i] = i * dT
        Force[j][i] = -Mass * ConstantK * ((Velocity[j][i-1]*Velocity[j][i-1]*Velocity[j][i-1]) + ConstantA * ConstantA * Velocity[j][i-1])
        Acceleration[j][i] = Force[j][i] / Mass
        Velocity[j][i] = Velocity[j][i-1] + Acceleration[j][i-1] * dT
        Position[j][i] = Position[j][i-1] + Velocity[j][i-1] * dT
    print('Finished', str(j+1))

for j in range(Iterations):
    plt.plot(Time, Velocity[j], label=f'{InitialVelocity + 10 * j} m/s')

plt.ylabel("Velocity (m/s)")
plt.xlabel("Time (s)")
plt.legend()
plt.savefig(os.path.join(Directory, '2-13_Velocity_v_Time.png'))
plt.show()

for j in range(Iterations):
    plt.plot(Time, Position[j], label=f'{InitialVelocity + 10 * j} m/s')

plt.axhline(y = (math.pi / (2 * ConstantK * ConstantA)), color = 'r', linestyle = '-') 
plt.ylabel("Position (m)")
plt.xlabel("Time (s)")
plt.legend()
plt.savefig(os.path.join(Directory, '2-13_Position_v_Time.png'))
plt.show()
print('Done')