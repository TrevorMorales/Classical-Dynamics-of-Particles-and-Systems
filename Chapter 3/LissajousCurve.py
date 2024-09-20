import matplotlib.pyplot as plt
import math
import numpy as np
import os

Directory = os.path.dirname(__file__)

dT = 0.01
Steps = int(10/dT)
XPosition = np.zeros((Steps))
YPosition = np.zeros((Steps))
A = 4
B = 6
XFrequency = 7
YFrequency = 6
Alpha = math.pi / 2
Beta = 0
T = 0

for i in range(Steps):
    XPosition[i] = A * math.cos((XFrequency * T) - Alpha)
    YPosition[i] = B * math.cos((YFrequency * T) - Beta)
    T = T + dT

plt.plot(XPosition, YPosition)
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.text(XPosition[0]+0.5,YPosition[0]+0.5,'(0,6) @ t = 0', fontsize = 12)
plt.plot(XPosition[0],YPosition[0],'x')
plt.plot(XPosition[Steps-1],YPosition[Steps-1],'x')
plt.axhline(y=0, linestyle = 'dashed')
plt.axvline(x=0, linestyle = 'dashed')
plt.text(XPosition[Steps-1]-3,YPosition[Steps-1]-1.25,'('+str(round(XPosition[Steps-1],3))+','+str(round(YPosition[Steps-1],3))+') @ t = 10', fontsize = 12)
plt.ylabel("Y Position (m)")
plt.xlabel("X Position (m)")
plt.title("A = 4, B = 6, ωx = 7, ωy = 6, α = π / 2, β = 0")
plt.savefig(os.path.join(Directory, '3-A_Lissajous_Curve.png'))
plt.show()

XPosition = np.zeros((Steps))
YPosition = np.zeros((Steps))
A = 4
B = 4
XFrequency = 6
YFrequency = 24
Alpha = 0
Beta = math.pi / 4
T = 0

for i in range(Steps):
    XPosition[i] = A * math.cos((XFrequency * T) - Alpha)
    YPosition[i] = B * math.cos((YFrequency * T) - Beta)
    T = T + dT

plt.plot(XPosition, YPosition)
plt.xlim(-6,6)
plt.ylim(-6,6)
plt.text(XPosition[0]-2,YPosition[0]+1.25,'('+str(round(XPosition[0],3))+','+str(round(YPosition[0],3))+') @ t = 0', fontsize = 12)
plt.plot(XPosition[0],YPosition[0],'x')
plt.plot(XPosition[Steps-1],YPosition[Steps-1],'x')
plt.axhline(y=0, linestyle = 'dashed')
plt.axvline(x=0, linestyle = 'dashed')
plt.text(XPosition[Steps-1]-1,YPosition[Steps-1]+0.5,'('+str(round(XPosition[Steps-1],3))+','+str(round(YPosition[Steps-1],3))+') @ t = 10', fontsize = 12)
plt.ylabel("Y Position (m)")
plt.xlabel("X Position (m)")
plt.title("A = 4, B = 4, ωx = 6, ωy = 24, α = 0, β = π / 4")
plt.savefig(os.path.join(Directory, '3-B_Lissajous_Curve.png'))
plt.show()