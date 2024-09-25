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
plt.show()

OrbitalPeriod = 3.153 * (10**(7))
OrbitalSpeed = (2 * np.pi * Au ) / OrbitalPeriod
print("Earth's Orbital Speed:", OrbitalSpeed, "m/s")
print("Earth's Orbital Speed in Natural Units:", str(OrbitalSpeed / Au * OrbitalPeriod), "au / year\n")

NaturalOrbitalSpeed = OrbitalSpeed / Au * 31556952
print("Gravitational Constant:", str(((OrbitalSpeed * OrbitalSpeed * Au )/SunMass)), "N m^2 / kg^2")
print("Gravitational Constant in Natural Units:",str(NaturalOrbitalSpeed * NaturalOrbitalSpeed), "au^3 / (solar mass * year ^ 2)\n")
NaturalG = NaturalOrbitalSpeed * NaturalOrbitalSpeed

print("Orbital Speed (in natural units) can be given as √(G/R) if R is in natural units (au).")