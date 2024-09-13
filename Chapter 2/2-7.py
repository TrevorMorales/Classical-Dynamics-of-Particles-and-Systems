# Imports
import matplotlib.pyplot as plt
import numpy as np
import math

# Initialization

PlaneVelocity =    160.0 # km/h
PlaneVelocity = ( PlaneVelocity * 1000.0 ) / 60.0 / 60.0
PlaneHeight =       80.0 # m
Gravity =            9.8 # m/s^2
HayBaleMass =       30.0 # kg
HayBaleSurfaceArea = 0.2 # m^2
DragCoefficient =    0.8 # a.u.

# Graph Array Initialization
Steps = int(20)
YWithoutAirResistance = np.zeros((Steps))
XWithoutAirResistance = np.zeros((Steps))

# Without Air Resistance
TimeToFall = math.sqrt(80/4.9)
TimeSteps = np.linspace(0.0, TimeToFall, num = Steps)
XStartPosition = -(PlaneVelocity * TimeToFall) - 30
for i in range (Steps):
    YWithoutAirResistance[i] = PlaneHeight - 0.5 * Gravity * (TimeSteps[i] * TimeSteps[i])
    XWithoutAirResistance[i] = XStartPosition + PlaneVelocity * TimeSteps[i]
plt.plot(XWithoutAirResistance,YWithoutAirResistance)
plt.axis((XWithoutAirResistance[0],0,YWithoutAirResistance[Steps-1],YWithoutAirResistance[0]))
plt.show()