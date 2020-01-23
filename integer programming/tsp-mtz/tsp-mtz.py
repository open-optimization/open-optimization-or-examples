#!/usr/bin/env python
# coding: utf-8

# In[14]:


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


# In[21]:


# Load Instance

#instance = "sp11"
instance = "uscap"
#instance = "sgb128"

# Load Names
f=open("data/" + instance + "_name.txt", "r")
names = f.readlines()
names = [name.rstrip("\n") for name in names]

#Load Locations
location = np.loadtxt("data/" + instance + "_xy.txt")

#Load Distances
distance = np.loadtxt("data/" + instance + "_dist.txt")

n = len(names)


# In[22]:


################
# Start the timer
start = time.clock()
################

### Input your model here

# Create a new model
m = Model("NFL-Rivals Model")

# Create set
I = range(n)

# Create variables
x = m.addVars(I,I, vtype=GRB.BINARY, name="x")

# Set objective
m.setObjective(0.5*sum(distance[i,j]*x[i,j] for i in I for j in I), GRB.MINIMIZE)

# Add constraint:
m.addConstr(sum(x[i,j] for i in I for j in I) >= n-1, "at least (n-1)/2 pairs")

#Add constraint: no city connected to itself
m.addConstrs((x[i,i]==0 for i in I), "No city connected to itself")

#Add constraint: At most 1 rival for each city
m.addConstrs((sum(x[i,j] for j in I) <=1 for i in I), "Rivals")

# Optimize model
m.optimize()

#End the timer
end = time.clock()
print("Time to run code: ", end - start)
################

#Extract the solution and plot it
x_sol = [ [ x[(i,j)].x for i in I] for j in I]
edges = [(i,j) for i in I for j in I if x_sol[i][j] ==1]
plot_locations_and_edges(edges)
