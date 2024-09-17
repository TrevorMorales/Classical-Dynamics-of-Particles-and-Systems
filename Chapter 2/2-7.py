# Imports
import matplotlib.pyplot as plt
import numpy as np
import math
import os

# Initialization

Directory = os.path.dirname(__file__)
PlaneVelocity =    160.0    # km/h
PlaneVelocity = ( PlaneVelocity * 1000.0 ) / 60.0 / 60.0
PlaneHeight =       80.0    # m
Gravity =            9.8    # m/s^2
HayBaleMass =       30.0    # kg
AirDensity =          1.204 # kg/m^3
HayBaleSurfaceArea = 0.2    # m^2
DragCoefficient =    0.8    # a.u.

# Graph Array Initialization
Steps = int(500)
YWithoutAirResistance = np.zeros((Steps))
XWithoutAirResistance = np.zeros((Steps))

# Without Air Resistance
TimeToFall = math.sqrt(80/4.9)
TimeSteps = np.linspace(0.0, TimeToFall, num = Steps)
XStartPosition = -(PlaneVelocity * TimeToFall) - 30
for i in range (Steps):
    YWithoutAirResistance[i] = PlaneHeight - 0.5 * Gravity * (TimeSteps[i] * TimeSteps[i])
    XWithoutAirResistance[i] = XStartPosition + PlaneVelocity * TimeSteps[i]


# With Air Resistance
XPosition = np.zeros((Steps))
YPosition = np.zeros((Steps))
Time = 0
TimeStep = 0.01
XVelocity = PlaneVelocity
YVelocity = 0.0
XPosition[0], YPosition[0] = XStartPosition,PlaneHeight

for i in range(Steps):
    if (not i == 0):
        XAcceleration = - ( DragCoefficient / HayBaleMass ) * XVelocity * XVelocity
        YAcceleration = -Gravity - ( DragCoefficient / HayBaleMass ) * YVelocity * YVelocity
        XVelocity = XVelocity + XAcceleration * TimeStep
        YVelocity = YVelocity + YAcceleration * TimeStep
        XPosition[i] = XPosition[i-1] + XVelocity * TimeStep
        YPosition[i] = YPosition[i-1] + YVelocity * TimeStep
    
    Time += TimeStep

plt.plot(XPosition, YPosition, label = 'Air Resistance')
plt.plot(XWithoutAirResistance,YWithoutAirResistance, label = 'Without Air Resistance')
plt.axis((XWithoutAirResistance[0],0,YWithoutAirResistance[Steps-1],YWithoutAirResistance[0]))
plt.xlabel("Position (m)")
plt.ylabel("Position (m)")
plt.title("Hay Bales Released Simultaneously")
plt.legend()
plt.savefig(Directory + '/2-7_Simultaneous_Release')
plt.show()

Offset = 0
Min = YPosition[0]
for i in range(Steps):
    if(YPosition[i] < Min and YPosition[i] > 0):
        Offset = XPosition[i]

for i in range(Steps):
    XPosition[i] = XPosition[i] - Offset - 30


plt.plot(XPosition, YPosition, label = 'Air Resistance')
plt.plot(XWithoutAirResistance,YWithoutAirResistance, label = 'Without Air Resistance')
plt.axis((XWithoutAirResistance[0],0,YWithoutAirResistance[Steps-1],YWithoutAirResistance[0]))
plt.xlabel("Position (m)")
plt.ylabel("Position (m)")
plt.title("Hay Bales Landing Simultaneously")
plt.legend()
plt.figtext(0.15,0.25,"Distance Between Release/Landing\n Positions of Bales = " + str(round(Offset+30,4)))
plt.savefig(Directory + '/2-7_Simultaneous_Landing')
plt.show()