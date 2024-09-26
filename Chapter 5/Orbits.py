import matplotlib.pyplot as plt
import numpy as np

SunMass = 1.989 * (10**(30))
EarthMass = 5.9722 * (10**(24))
G = 6.67430 * (10**(-11))
Au = 150007331000
# print(SunMass)
# print(EarthMass)
# print(Au)
# print(G)

GravitationalForce = ( G * EarthMass * SunMass ) / ( Au**2 )

XForce = np.zeros((360))
YForce = np.zeros((360))
Angle = np.zeros((360))

for i in range(len(Angle)):
    Angle[i] = i * ((2 * np.pi) / 360)
    XForce[i] = GravitationalForce * np.cos(Angle[i])
    YForce[i] = GravitationalForce * np.sin(Angle[i])

plt.plot(Angle, XForce)
plt.plot(Angle, YForce)
plt.title("Gravitational Force of the Sun on the Earth")
plt.ylabel("Force (N)")
plt.xlabel("Angle (rads)")
# plt.show()

OrbitalPeriod = 3.153 * (10**(7))
OrbitalSpeed = (2 * np.pi * Au ) / OrbitalPeriod
print("Earth's Orbital Speed:", OrbitalSpeed, "m/s")
print("Earth's Orbital Speed in Natural Units:", str(OrbitalSpeed / Au * OrbitalPeriod), "au / year\n")

NaturalOrbitalSpeed = OrbitalSpeed / Au * 31556952
print("Gravitational Constant:", str(((OrbitalSpeed * OrbitalSpeed * Au )/SunMass)), "N m^2 / kg^2")
print("Gravitational Constant in Natural Units:",str(NaturalOrbitalSpeed * NaturalOrbitalSpeed), "au^3 / (solar mass * year ^ 2)\n")
NaturalG = NaturalOrbitalSpeed * NaturalOrbitalSpeed

print("Orbital Speed (in natural units) can be given as √(GM/R) if G, M and R are in natural units (au).")



# First Simulation

for k in range(3):

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



# Euler-Richardson

for k in range(3):
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
        
        # TotalEnergy = (np.sqrt(XVelocity**2 + YVelocity**2) / 2.0) + (NaturalG / Radius)
        # print(TotalEnergy)
        # Still basically the same
        
        for j in range(Steps - 1):
            Radius = np.sqrt(XPosition[j]**2 + YPosition[j]**2)
            Acceleration = -(NaturalG) / (Radius**2)
            
            XAcceleration = Acceleration * (XPosition[j] / Radius)
            YAcceleration = Acceleration * (YPosition[j] / Radius)

            XVelocity_half = XVelocity + 0.5 * XAcceleration * dT
            YVelocity_half = YVelocity + 0.5 * YAcceleration * dT
            
            XPosition_half = XPosition[j] + XVelocity_half * dT
            YPosition_half = YPosition[j] + YVelocity_half * dT
            
            Radius_half = np.sqrt(XPosition_half**2 + YPosition_half**2)
            Acceleration_half = -(NaturalG) / (Radius_half**2)
            
            XAcceleration_half = Acceleration_half * (XPosition_half / Radius_half)
            YAcceleration_half = Acceleration_half * (YPosition_half / Radius_half)

            XVelocity += XAcceleration_half * dT
            YVelocity += YAcceleration_half * dT
            
            XPosition[j + 1] = XPosition_half
            YPosition[j + 1] = YPosition_half

        # TotalEnergy = (np.sqrt(XVelocity**2 + YVelocity**2) / 2.0) + (NaturalG / Radius)
        # print(TotalEnergy)
        # Still basically the same

        plt.plot(XPosition, YPosition)

    Title = f"Euler-Richardson Orbit Simulation for dT = {dT} years"
    plt.title(Title)
    plt.ylabel("Position (au)")
    plt.xlabel("Position (au)")
    plt.axis('equal')
    plt.grid()
    # plt.show()

    

# Verlet

for k in range(3):
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
        
        # TotalEnergy = (np.sqrt(XVelocity**2 + YVelocity**2) / 2.0) + (NaturalG / Radius)
        # print(TotalEnergy)

        Radius = np.sqrt(XPosition[0]**2 + YPosition[0]**2)
        Acceleration = -(NaturalG) / (Radius**2)
        XAcceleration = Acceleration * (XPosition[0] / Radius)
        YAcceleration = Acceleration * (YPosition[0] / Radius)

        for j in range(1, Steps):
            XPosition[j] = XPosition[j - 1] + XVelocity * dT + 0.5 * XAcceleration * dT**2
            YPosition[j] = YPosition[j - 1] + YVelocity * dT + 0.5 * YAcceleration * dT**2

            Radius = np.sqrt(XPosition[j]**2 + YPosition[j]**2)
            Acceleration = -(NaturalG) / (Radius**2)
            XAcceleration = Acceleration * (XPosition[j] / Radius)
            YAcceleration = Acceleration * (YPosition[j] / Radius)

            XVelocity += 0.5 * (XAcceleration + (-(NaturalG) / (Radius**2) * (XPosition[j] / Radius))) * dT
            YVelocity += 0.5 * (YAcceleration + (-(NaturalG) / (Radius**2) * (YPosition[j] / Radius))) * dT
        
        # TotalEnergy = (np.sqrt(XVelocity**2 + YVelocity**2) / 2.0) + (NaturalG / Radius)

        plt.plot(XPosition, YPosition)

    Title = f"Verlet Orbit Simulation for dT = {dT} years"
    plt.title(Title)
    plt.ylabel("Position (au)")
    plt.xlabel("Position (au)")
    plt.axis('equal')
    plt.grid()
    # plt.show()



# Apocalyptic Earth Sim (Initial Vy slightly decreased)

for k in range(3):
    Steps = 100 * (10**(k+1))
    dT = 1 / (100 * (10**(k+1)))

    Radius = 1
    XPosition = np.zeros(Steps)
    YPosition = np.zeros(Steps)
    XPosition[0] = Radius
    OrbitalSpeed = np.sqrt(NaturalG / Radius)
    XVelocity = 0
    YVelocity = OrbitalSpeed * 0.95
    
    # TotalEnergy = (np.sqrt(XVelocity**2 + YVelocity**2) / 2.0) + (NaturalG / Radius)
    # print(TotalEnergy)

    Radius = np.sqrt(XPosition[0]**2 + YPosition[0]**2)
    Acceleration = -(NaturalG) / (Radius**2)
    XAcceleration = Acceleration * (XPosition[0] / Radius)
    YAcceleration = Acceleration * (YPosition[0] / Radius)

    for j in range(1, Steps):
        XPosition[j] = XPosition[j - 1] + XVelocity * dT + 0.5 * XAcceleration * dT**2
        YPosition[j] = YPosition[j - 1] + YVelocity * dT + 0.5 * YAcceleration * dT**2

        Radius = np.sqrt(XPosition[j]**2 + YPosition[j]**2)
        Acceleration = -(NaturalG) / (Radius**2)
        XAcceleration = Acceleration * (XPosition[j] / Radius)
        YAcceleration = Acceleration * (YPosition[j] / Radius)

        XVelocity += 0.5 * (XAcceleration + (-(NaturalG) / (Radius**2) * (XPosition[j] / Radius))) * dT
        YVelocity += 0.5 * (YAcceleration + (-(NaturalG) / (Radius**2) * (YPosition[j] / Radius))) * dT
        
    # TotalEnergy = (np.sqrt(XVelocity**2 + YVelocity**2) / 2.0) + (NaturalG / Radius)

    plt.plot(XPosition, YPosition)

    Title = f"Earth Orbit Simulation for at 0.95Vy Initial Velocity"
    plt.title(Title)
    plt.ylabel("Position (au)")
    plt.xlabel("Position (au)")
    plt.axis('equal')
    plt.grid()
    plt.show()

print("Done")