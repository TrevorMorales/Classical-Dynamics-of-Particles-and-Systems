import numpy as np
import matplotlib.pyplot as plt

NaturalG = 39.54593914429025
MassJ = 0.001
MassA = 1e-8
RadiusJ = 5.2
RadiusA = 3.0

Steps = 10000
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
        print("Keep Going From Here")

for k in range(1):

    Steps = 1000 * (10**(k+1))
    dT = 1 / (100 * (10**(k+1)))

    for i in range(3):
        Radius = 1.5 * (i + 1)
        XPosition = np.zeros(Steps)
        YPosition = np.zeros(Steps)
        XPosition[0] = Radius
        OrbitalSpeed = np.sqrt(NaturalG / Radius)
        XVelocity = 0
        YVelocity = OrbitalSpeed
        
        TotalEnergy = ( np.sqrt(XVelocity**2 + YVelocity**2) / 2.0 ) + ( NaturalG / Radius ) # Natural Units, per unit mass
        # print("Total Energy Before Sim:", str(TotalEnergy))
        # Same as the end, pretty much

        for j in range(Steps - 1):
            Radius = np.sqrt(XPosition[j]**2 + YPosition[j]**2)
            Acceleration = -(NaturalG) / (Radius**2)
            
            XAcceleration = Acceleration * (XPosition[j] / Radius)
            YAcceleration = Acceleration * (YPosition[j] / Radius)
            
            XVelocity += XAcceleration * dT
            YVelocity += YAcceleration * dT
            
            XPosition[j+1] = XPosition[j] + XVelocity * dT
            YPosition[j+1] = YPosition[j] + YVelocity * dT
        
        TotalEnergy = ( np.sqrt(XVelocity**2 + YVelocity**2) / 2.0 ) + ( NaturalG / Radius ) # Natural Units, per unit mass
        # print("Total Energy After Sim:", str(TotalEnergy))
        # They're basically identical

        plt.plot(XPosition, YPosition)

    Title = f"Orbit Simulation for dT = {dT} years"
    plt.title(Title)
    plt.ylabel("Position (au)")
    plt.xlabel("Position (au)")
    plt.axis('equal')
    plt.grid()
    # plt.show()