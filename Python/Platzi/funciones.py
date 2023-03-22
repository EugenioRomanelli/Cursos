# -*- coding: utf-8 -*-
"""Funciones.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qgBWorXFeTesrv1n9ZC8UC2X8HJco8eN
"""

import numpy as np
import matplotlib.pyplot as plt

def relu(x):
  return np.maximum(0,x)

x = np.linspace(10,-10,100)

plt.plot(x, relu(x))

def mse(y,y_hat, derivate=False):
  if derivate:
      return (y_hat-y)
  else:
      return np.mean((y_hat - y)**2)

real = np.array([0,0,1,1])
prediction = np.array([0.9,0.5,0.2,0.0])

mse(real, prediction)