import matplotlib.pyplot as plt
import numpy as np
import math
import os

Mass = 5
Angle = 45
Distance = 142
InitialVelocity = 54
Vxi = InitialVelocity / (math.sqrt(2))
Vyi = Vxi
print(Vxi)

Directory = os.path.dirname(__file__)

Steps = 1000
dT = 0.01
Iterations = 10
Time = np.zeros((Steps))
YPosition = np.zeros((Iterations, Steps))
XPosition = np.zeros((Iterations, Steps))
YAcceleration = np.zeros((Iterations, Steps))
XAcceleration = np.zeros((Iterations, Steps))
YVelocity = np.zeros((Iterations, Steps))
XVelocity = np.zeros((Iterations, Steps))
KConstant = np.zeros((Iterations))
KSteps = 0.00125
Gravity = 10

for i in range(Iterations):
    Time[0] = 0
    KConstant[i] = 0.105 + (KSteps * ( i + 1 ))
    KConstant[i] = round(KConstant[i],5)
    YPosition[i][0] = 0
    XPosition[i][0] = 0
    YVelocity[i][0] = Vyi
    XVelocity[i][0] = Vxi
    XAcceleration[i][0] = -KConstant[i] * XVelocity[i][0]
    YAcceleration[i][0] = -KConstant[i] * YVelocity[i][0] - Gravity
    for j in range(1,Steps):
        Time[j] = j * dT
        YPosition[i][j] = YPosition[i][j-1] + YVelocity[i][j-1] * dT
        YVelocity[i][j] = YVelocity[i][j-1] + YAcceleration[i][j-1] * dT
        YAcceleration[i][j] = -KConstant[i] * YVelocity[i][0] - Gravity
        XPosition[i][j] = XPosition[i][j-1] + XVelocity[i][j-1] * dT
        XVelocity[i][j] = XVelocity[i][j-1] + XAcceleration[i][j-1] * dT
        XAcceleration[i][j] = -KConstant[i] * XVelocity[i][0]
        if(YPosition[i][j] < 0):
            print(KConstant[i], XPosition[i][j])
            break

    plt.plot(XPosition[i], YPosition[i])

plt.axis((0, 200, 0, 100))
plt.legend(KConstant)
plt.title('Projectile Motion')
plt.ylabel('Position (m)')
plt.xlabel('Position (x)')
plt.figtext(0.25, 0.7, 'For d = 142, k = 0.11375')
plt.savefig(Directory + '/2-55_ProjectileMotion')
plt.show()
