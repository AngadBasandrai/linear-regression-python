import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

data = np.loadtxt('data.csv', delimiter=',')
for d in data:
    x.append(d[0])
    y.append(d[1])

xbar = np.mean(x)
sx = np.std(x)
ybar = np.mean(y)
sy = np.std(y)

linex = [np.min(x), np.max(x)]
liney = []
revLiney = [np.min(y), np.max(y)]
revLinex = []

r_ = []
for i in range(len(x)):
    r_.append(((x[i]-xbar)/sx)*((y[i]-ybar)/sy))

r = 0
for i in r_:
    r += i
r/=len(x)

b = r * (sy / sx)
a = ybar - (b * xbar)

for x_ in linex:
    liney.append(a + (b * x_))

# plt.scatter(x, y)
# plt.plot()

predX = float(input("X: "))
predY = a + (b * predX)

print("Predicted y is: " + str(predY))

linePredXX = [np.min(x), predX]
linePredXY = [predY, predY]

linePredYY = [np.min(y), predY]
linePredYX = [predX, predX]


plt.scatter(x, y)
plt.scatter(predX, predY, c="green")
plt.plot(linex, liney)
plt.plot(linePredXX, linePredXY, 'g--')
plt.plot(linePredYX, linePredYY, 'g--')
plt.show()
