import matplotlib.pyplot as plt
import numpy as np
import math
import os

# Constants

Directory = os.path.dirname(__file__)

Mass = 1
K = 1
Alpha = 0.5

Steps = 1000
dT = 0.01
Time = np.zeros((Steps))
Force = np.zeros((Steps))
Acceleration = np.zeros((Steps))
Velocity = np.zeros((Steps))
Position = np.zeros((Steps))

for i in range(1,Steps):
    Time[i] = i * dT
    Force[i] = K * Time[i] * math.e**(-Alpha * Time[i])
    Acceleration[i] = Force[i] / Mass
    Velocity[i] = Velocity[i-1] + Acceleration[i-1] * dT
    Position[i] = Position[i-1] + Velocity[i-1] * dT

plt.plot(Time, Acceleration)
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s/s)")
plt.title("Acceleration vs. Time")
plt.savefig(Directory + '/2-23_Acceleration')
plt.show()
plt.plot(Time, Velocity)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity vs. Time")
plt.savefig(Directory + '/2-23_Velocity')
plt.show()
plt.plot(Time, Position)
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Position vs. Time")
plt.savefig(Directory + '/2-23_Position')
plt.show()