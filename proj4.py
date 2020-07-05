#!/usr/bin/env python
# coding: utf-8

# # Project 4 - Polynomial Regression from Scratch
# 
# In this notebook, you will write code that will:
# -  generate a dataset, 
# -  model it using a polynomial regression, 
# -  and find the optimal model parameters for it (writing your own optimization routine).
# 
# All of the parts of this are meant to be done "from scratch", so do not use sklearn. (numpy's ok)  
# Note: this is a continuation of the exercise we started in class previously.  

# In[55]:


import numpy as np
import matplotlib.pyplot as plt


# ## Dataset
# Create a dataset with 1,000 1-D X and corresponding y values, each w/ a small amount of added uniform random noise (max val = 0.1).  (So unlike example in class which had a surface and 2 features, this is like the book example with a curve with 1 feature.)
# 
# -  make X go from -5 to 5 (plus noise)
# -  make $y = 5 + 7x + 2x^2 - 0.5x^3$   (plus noise)

# In[46]:


x = np.random.uniform(-5,5,(1000,1)) + np.random.uniform(-0.1,0.1,(1000,1))
y = 5 + 7*x + 2*(x**2) - 0.5*(x**3) + np.random.uniform(-0.1,0.1,(1000,1))


# ## Augment X
# Write a function that adds new columns to the dataset of powers of X, up to and including $X^5$ (and don't forget the ones for the $\theta_0$ term).

# In[47]:


x0_ones = np.ones((X.shape[0],X.shape[1]))
x2 = x**2
x3 = x**3
x4 = x**4
x5 = x**5
x_augmented = np.concatenate((x0_ones, x, x2, x3, x4, x5), axis = 1)


# ## Fit a Polynomial Regression model to the training data
# Assume that we have a polynomial regression model
# \begin{equation*}
# y(X;\theta) = \theta_0 + \theta_1 x + \theta_2 x^2 +\theta_3 x^3 +\theta_4 x^4 +\theta_5 x^5 
# \end{equation*}
# 
# Assume that we're using a mean squared error function.
# 
# -  Find the optimal value of theta (ie $\theta_0$ through $\theta_5$). Note: Refer to Ch. 4, Eqn's 4.6 and 4.7.
# 
# -  Try this for a variety of different values of alpha.  Note how long it takes for the optimization to converge (or if it doesn't).
# 

# In[48]:


eta = 0.0000000000001
n_iterations = 10000000
m = 1000
theta = np.random.randn(6,1)
for i in range(n_iterations):
    gradient = 2/m * x_augmented.T.dot(x_augmented.dot(theta)-y)
    theta = theta - eta*gradient
    
    
print(theta)


# ## Plot the Final Model
# Make a plot showing the (X,y) data points of the training set, and superimpose the line for the model on the same plot.

# In[57]:


y_predicted = x_augmented.dot(theta)
plt.scatter(x,y_predicted, c = 'r')
plt.scatter(x, y, c = 'g' )


# ## Different Model Degrees
# Try the model for different degrees of n, specifically n = (2, 5, 10).  Plot the resulting models.

# In[63]:


x_aug_n2 = np.concatenate((x0_ones, x, x2), axis  = 1 )
x6 = x**6 
x7 = x**7 
x8 = x**8 
x9 = x**9 
x10 = x**10 
x_aug_n10 = np.concatenate((x0_ones, x_augmented, x6,x7,x8,x9,x10), axis = 1)
#x_aug_n3 = np.concatenate(x0_ones, x, x2, x3, x4, x5)
#x_aug_n4 = np.concatenate(x0_ones, x, x2, x3, x4, x5)


# In[ ]:




