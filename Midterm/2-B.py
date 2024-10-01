# Imports
import matplotlib.pyplot as plt
import numpy as np
import math
import os

# Initialization

Directory = os.path.dirname(__file__)
SoundVelocity = 331
K = 0.2
dT = 0.00001
Steps = int(5/dT)
ElapsedTime = 0
Velocity = np.zeros((Steps))
Position = np.zeros((Steps))
SoundPosition = np.zeros((Steps))
SoundPosition[0] = 5 * SoundVelocity

for i in range(1, Steps):
    ElapsedTime += dT
    Acceleration = 9.81 - (K * Velocity[i-1])
    Velocity[i] = Velocity[i-1] + (Acceleration * dT)
    Position[i] = Position[i-1] + (Velocity[i] * dT)
    SoundPosition[i] = (5 - ElapsedTime) * SoundVelocity

Min = 9999999999
for i in range(Steps):
    if(np.abs(SoundPosition[i] - Position[i]) < Min):
        Min = np.abs(SoundPosition[i] - Position[i])
        Closest = i

print((SoundVelocity*(5 - Closest * dT)))
plt.plot(Position)
plt.plot(SoundPosition)
plt.show()