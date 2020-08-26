


# Import everything needed
import numpy as np
import matplotlib.pyplot as plt
from gurobipy import *
import time

def plot_locations_and_edges(Edges):
    for (i,j) in Edges:
        plt.plot([location[i,0], location[j,0]], [location[i,1], location[j,1]], color = "blue", linestyle = "dashed", linewidth= 0.5)
    x,y = np.transpose(location);

    plt.scatter(x,y, color = "red");
    plt.xlabel("x-coordinate")
    plt.ylabel("y-coordinate")
    plt.title("Matchings of Rival Teams")
    plt.show()

# Previously computed runtimes
times = [7.50100000e-02, 1.86590000e-02, 3.76530000e-02, 6.55640000e-02,
       9.24220000e-02, 1.31711000e-01, 1.79213000e-01, 2.29969000e-01,
       7.13742000e-01, 3.89647000e-01, 4.98939000e-01, 5.94722000e-01,
       6.87888000e-01, 7.57945000e-01, 8.96916000e-01, 1.03419300e+00,
       1.22052400e+00, 1.70963900e+00, 1.57993900e+00, 1.71035200e+00,
       2.00378200e+00, 2.38150600e+00, 2.29569300e+00, 2.45584700e+00,
       2.97761100e+00, 2.90555300e+00, 3.56060900e+00, 3.51006500e+00,
       3.78492300e+00, 4.37639300e+00, 1.74059483e+02]

sizes = [  10,   20,   30,   40,   50,   60,   70,   80,   90,  100,  110,
        120,  130,  140,  150,  160,  170,  180,  190,  200,  210,  220,
        230,  240,  250,  260,  270,  280,  290,  300, 1000]

plot1 = plt.figure(1)
plt.scatter(sizes,times)
plt.xlabel("Size of instance")
plt.ylabel("Time to solve instance")
plt.title("Solution times of Matching Problem");

# create 1000 equally spaced points between -10 and 10
x = np.linspace(0, n, 1000)

# calculate the y value for each element of the x vector
y = 0.00004*x**2


plt.plot(x, y, color = "green")
plt.legend(["y = 0.00004*x**2","solve times"])








plot2 = plt.figure(2)
plt.scatter(sizes[:-1],times[:-1])
plt.xlabel("Size of instance")
plt.ylabel("Time to solve instance")
plt.title("Solution times of Matching Problem");

# create 1000 equally spaced points between -10 and 10
x = np.linspace(0, sizes[-2], 1000)

# calculate the y value for each element of the x vector
y = 0.00004*x**2


plt.plot(x, y, color = "green")
plt.legend(["y = 0.00004*x**2","solve times"])



plt.scatter(sizes,times)
plt.xlabel("Size of instance")
plt.ylabel("Time to solve instance")
plt.title("Solution times of Matching Problem");

# create 1000 equally spaced points between -10 and 10
x = np.linspace(0, n, 1000)

# calculate the y value for each element of the x vector
y = 0.00004*x**2


plt.plot(x, y, color = "green")
plt.legend(["y = 0.00004*x**2","solve times"])
