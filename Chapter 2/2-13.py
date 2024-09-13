import matplotlib.pyplot as plt
import numpy as np
import math

ConstantA = 0.5
ConstantK = 0.3
InitialVelocity = 400
Steps = 1000
TimeSteps = np.linspace(0, Steps-1, Steps)
Distance = np.zeros((Steps))
dT = 0.001

Velocity = InitialVelocity
Distance[0] = 0

for i in range(1, Steps):
    Time = TimeSteps[i] * dT
    Distance[i] = (1 / ( ConstantA * ConstantK * 2)) * -math.asin( ( ConstantA * ConstantA - Velocity * Velocity ) / ( ConstantA * ConstantA + Velocity * Velocity ) )

print(Distance)

plt.plot(TimeSteps*dT, Distance)
plt.axvline(x=math.pi/(2 * ConstantA * ConstantK))
plt.show()

# m, k, a constants
# RetardingForce = m * k * (v * v * v + a * a * v)