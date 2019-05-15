import os
import numpy as np
import math as m
import matplotlib.pyplot as plt
# %matplotlib inline --> plt.show()

from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import tensorflow as tf

#utility function
def reset_graph(seed = 42):
    tf.reset_default_graph()
    tf.set_random_seed(seed)
    np.random.rand(seed)


#below defines linear regression model that we fit. 3 predictors x1,x2, x3 that are all uniformly distributed in [-1,1]
#we weight them with weights b1 to b3.
#add to this an intercept A and Gaussian noise with the volatility sigma that equal 10%.
#we use artificial data for the following regression
#y(x) = a+b1*x1+b2*x2+b3*x3+oe
#where e~N(0,1) is a Gaussian noise and o is its volatility, with the following choice of parameters:
# a = 1.0
# b1,b2,b3 = (0.5, 0.2, 0.1)
# o = 0.1
# x1, x2, x3 will be uniformally distributed in [-1,1]



#generate data
n_points = 5000
n_features = 3

bias = np.ones(n_points).reshape((-1,1))
low = -np.ones((n_points, n_features), 'float')
high = np.ones((n_points, n_features), 'float')

# s
X = np.random.uniform(low=low, high=high)
noise = np.random.normal(size=(n_points, 1))