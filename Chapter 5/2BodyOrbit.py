import numpy as np
import matplotlib.pyplot as plt

NaturalG = 39.54593914429025
MassJ = 0.001
MassA = 1e-8
RadiusJ = 5.2
RadiusA = 3.0

Steps = 10000000
dT = 1.0/1000.0

for i in range(1):
    RadiusA = (3.0) + (i * 0.1)

    JXPosition, JYPosition, AXPosition, AYPosition = np.zeros(Steps), np.zeros(Steps), np.zeros(Steps), np.zeros(Steps)
    JXPosition[0] = RadiusJ
    AXPosition[0] = RadiusA

    JOrbitalSpeed = np.sqrt(NaturalG / RadiusJ)
    AOrbitalSpeed = np.sqrt(NaturalG / RadiusA)
    JXVelocity = 0
    JYVelocity = JOrbitalSpeed
    AXVelocity = 0
    AYVelocity = AOrbitalSpeed

    for j in range(Steps - 1):
        RadiusJ = np.sqrt(JXPosition[j]**2 + JYPosition[j]**2)
        RadiusA = np.sqrt(AXPosition[j]**2 + AYPosition[j]**2)
        Distance = np.sqrt((JXPosition[j] - AXPosition[j])**2 + (JYPosition[j] - AYPosition[j])**2)

        JSunAcceleration = -(NaturalG) / (RadiusJ**2)
        JAAcceleration = -(NaturalG * MassA) / (Distance)

        ASunAcceleration = -(NaturalG) / (RadiusA**2)
        AJAcceleration = -(NaturalG * MassJ) / (Distance)

        JXAcceleration = JSunAcceleration * (JXPosition[j] / RadiusJ) + JAAcceleration * ((JXPosition[j] - AXPosition[j]) / Distance)
        JYAcceleration = JSunAcceleration * (JYPosition[j] / RadiusJ) + JAAcceleration * ((JYPosition[j] - AYPosition[j]) / Distance)

        AXAcceleration = ASunAcceleration * (AXPosition[j] / RadiusA) + AJAcceleration * ((AXPosition[j] - JXPosition[j]) / Distance)
        AYAcceleration = ASunAcceleration * (AYPosition[j] / RadiusA) + AJAcceleration * ((AYPosition[j] - JYPosition[j]) / Distance)

        JXVelocity += JXAcceleration * dT
        JYVelocity += JYAcceleration * dT

        AXVelocity += AXAcceleration * dT
        AYVelocity += AYAcceleration * dT

        JXPosition[j+1] = JXPosition[j] + JXVelocity * dT
        JYPosition[j+1] = JYPosition[j] + JYVelocity * dT
        AXPosition[j+1] = AXPosition[j] + AXVelocity * dT
        AYPosition[j+1] = AYPosition[j] + AYVelocity * dT

    plt.plot(JXPosition, JYPosition)
    plt.plot(AXPosition, AYPosition)
    plt.show()

print("Done")