import matplotlib.pyplot as plt

import numpy as np

import math

#prefined distance poses can be used to tet this out

#decelration is a constant.
#slope in v graph is decel rate
#we know the distance drop down to find time


def distance(x0, x1, y0, y1):
  X = x1 - x0
  Y = y1 - y0
  return math.sqrt(pow(X, 2) + pow(Y, 2))
  #used to calculate the distance between endpoint and car's current distance
def newvel(d, a):

  v_1 = ((10 - a) + a * math.sqrt(1 + (4 * d))) / 2
  v_2 = ((10 - a) - a * math.sqrt(1 + (4 * d))) / 2
  #now need to check if the computed velcoiy values are valid
  #we want to have a velcoity less than 5.
  if 0 < v_1 < 5:
    return v_1

  #return these velcoity values
  elif 0 < v_2 < 5:
    #return these velcoity values
    return v_2


  #velcoity goes to low level
def decel(thresh_d, curr_d, v_max, a_max):
  if thresh_d > curr_d:
    return newvel(curr_d, a_max)
  else:
    return v_max

def plotvel(N, dt, t, V, D, m, v_max, x_v, y_v, y_d, D2):
  for i in range(N):
    t[i] = dt * i
    V[i] = m * t[i] + v_max
    if i < N - 1:
      D[i + 1] = (V[i] * dt) + D[i]
      D2[i + 1] = 6 - ((V[i] * dt) + D[i])

  x1 = [x_v]
  y1 = [y_v]
  y2 = [y_d]

  plt.figure(1)
  plt.plot(t, V, label="Velcoity")
  plt.plot(t, D, label="Distance")
  plt.plot(t, D2, label="Distance")
  plt.plot(x1, y1, marker="o", markersize=5, markerfacecolor="green")
  plt.plot(x1, y2, marker="o", markersize=5, markerfacecolor="red")
  #plt.plot(x1, y2, marker="o", markersize=5, markerfacecolor="blue")

  plt.show()


if __name__ == "__main__":

  v_m = 5  #constant 5mph that won't change (for now)
  endpoint = [7, 7]
  curr_point = [2, 5]  #list but function takes in ints
  decel_dist = 7
  a_max = -2  #passed into new vel #m

  #-------------------------------(plotting)--------------------------------
  N = 2000
  t_f = 2
  dt = (t_f / N)
  t = np.zeros(N)
  V = np.zeros(N)
  D = np.zeros(N)
  Dleft = np.zeros(N)

  dist = distance(curr_point[0], endpoint[0], curr_point[1], endpoint[1])
  v_next = decel(decel_dist, dist, v_m, a_max)

  x_val = ((v_next - v_m) / a_max)
  y_dist = ((12.5) * a_max) + (125 / (a_max * a_max))    #same formulas just written in different ways 
  y_dist2 = (a_max * math.pow(x_val, 2)) + (5 * x_val)
  y_dist3 = (12.5 / a_max) - (25 / a_max)
  distanceleft = 6 - y_dist
  distanceleft2 = 6 - y_dist2
  #not sure if distance eq is correct?

  #--------------(FOR PLOTTING)----------------------
  #y_dist2 = ((v_next -5))
  #y_v = [v_next]
  #x_v = [x_val]  #a specific time
  #y_d = [y_dist3]
  #plotvel(N, dt, t, V, D, a_max, v_m, x_v, y_v, y_d, Dleft)
  #------------------------------------------------------------
  print(v_next)
  print(dist)
  #make a linear line. solve for t using the known velcoity. make a point on both lines
  #same thing for distance??? make plotting functions. Then plot ur pts. See if they are on the line and if the times match up
