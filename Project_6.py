#!/usr/bin/env python
# coding: utf-8

# 

# In[1]:


import tensorflow as tf
assert tf.__version__ >= "2.0"

import numpy as np
import matplotlib.pyplot as plt
import random
import os

get_ipython().run_line_magic('matplotlib', 'qt')


# In[2]:


NUM_DIMS = 3

# set up number of points that will be on unit sphere
NUM_PTS = 8


# In[3]:


OPT = "Nadam_mid_learn"
ITERS = 10**6
IMG_PATH=os.path.join("./Project_6", str(NUM_PTS) +"verts_"+ str(ITERS) + "_iters_" + OPT)
if not os.path.exists(IMG_PATH):
    os.makedirs(IMG_PATH)


# In[4]:


def sphere_term(tf_pts):
    zr = np.zeros([NUM_DIMS])
    a = 0
    for n in range(NUM_PTS):
        a += tf.abs(tf.norm(tf_pts[n,:]-zr)-1)
#     print(a)
    return a


# In[1]:


def repel_term(tf_pts):
    a = 0
    for n in range(NUM_PTS):
        for m in range(n):
            a += 1.0/(tf.norm(tf_pts[n,:]-tf_pts[m,:])+1e-20)
#     print(a)
    return a


# 

# In[2]:


def first_pt_boost(tf_pts):
    epsilon = .1
    a=0
    for n in range(NUM_PTS):
        a += 1/((tf_pts[n,2]+1-1e200)**10)
    return a


# In[3]:


def same_zs(tf_pts):
    a=0
    for n in range(NUM_PTS):
        for m in range(n+1, NUM_PTS):
            a+= tf_pts[n,2]-tf_pts[m,2]
    return a


# In[4]:


alpha = 100
beta = 10
gamma = 100
delta = 10

loss = lambda: alpha*sphere_term(tf_pts) + beta*repel_term(tf_pts) #+ delta*same_zs(tf_pts)#+ max(gamma*first_pt_boost(tf_pts), 50)


# In[5]:


two_opt = False
if OPT == 'SGD':
    opt = tf.keras.optimizers.SGD(learning_rate=0.00001)
elif OPT == 'Nadam':
    opt = tf.keras.optimizers.Nadam()
elif OPT == 'Nadam_high_learn':
    opt = tf.keras.optimizers.Nadam(learning_rate=.01)
elif OPT == 'Nadam_low_learn':
    opt = tf.keras.optimizers.Nadam(learning_rate=.0001, beta_1=0.4)
elif OPT == 'Adagrad':
    opt = tf.keras.optimizers.Adagrad()
elif OPT == 'Nadam_and_SGD':
    opt = tf.keras.optimizers.Nadam()
    opt2 = tf.keras.optimizers.SGD()
    two_opt = True
elif OPT == 'SGD_and_Nadam':
    opt = tf.keras.optimizers.SGD()
    opt2 = tf.keras.optimizers.Nadam()
    two_opt = True
elif OPT == 'Nadam_mid_learn':
    opt = tf.keras.optimizers.Nadam(learning_rate=.005)
elif OPT == 'Nadam_super_high_learn':
    opt = tf.keras.optimizers.Nadam(learning_rate=.1)


# In[10]:


#create random points in range 0-1.0 as numpy array and cast to TF variable
template = np.random.rand(NUM_PTS,NUM_DIMS)
print(template)
tf_pts = tf.Variable(np.random.rand(NUM_PTS,NUM_DIMS))


# In[11]:


# calling optimization in tensorflow
# set up number of iterations that the optimization will run
NUM_ITERS = ITERS
sphere_terms = []
repel_terms = []
for n in range(NUM_ITERS):
    sphere_terms.append(alpha*sphere_term(tf_pts))
    repel_terms.append(beta*repel_term(tf_pts))
    if n%100 == 0:
        print('iteration #: ',n)
        print(alpha*sphere_term(tf_pts))
        print(beta*repel_term(tf_pts))
    opt.minimize(loss, var_list=[tf_pts])


# In[12]:


# calling optimization in tensorflow
# set up number of iterations that the optimization will run
if two_opt == True:
    NUM_ITERS = ITERS
    sphere_terms = []
    repel_terms = []
    for n in range(NUM_ITERS):
        sphere_terms.append(alpha*sphere_term(tf_pts))
        repel_terms.append(beta*repel_term(tf_pts))
        if n%100 == 0:
            print('iteration #: ',n)
            print(alpha*sphere_term(tf_pts))
            print(beta*repel_term(tf_pts))
        opt2.minimize(loss, var_list=[tf_pts])


# In[14]:


# plotting loss curves
get_ipython().run_line_magic('matplotlib', 'qt')
plt.figure()
s_line, = plt.plot(sphere_terms,'r')
r_line, = plt.plot(repel_terms,'b')
plt.xlabel('# iterations')
plt.ylabel('loss function(s)')
plt.grid()
plt.legend((s_line,r_line),('sphere term','repel term'))
plt.show()
plt.savefig(os.path.join(IMG_PATH, "Loss_Curves"), format='png')


# In[15]:


tf_array = tf_pts.numpy()
print(type(tf_array))
print(tf_array)

# check if distance of pts from origin is 1
print(np.linalg.norm(tf_array,axis = 1))


# In[16]:


# 2-D Plotting with unit circle
if NUM_DIMS == 2:
    # 2-D Plotting
    fig, axs = plt.subplots(1,1)
    axs.plot(tf_pts[:,0],tf_pts[:,1],'bs')
    axs.axis('equal')
    angles = np.linspace(0, 2 * np.pi, 100)
    axs.plot(np.cos(angles),np.sin(angles))


# In[6]:


# 3-D Plotting with unit sphere
get_ipython().run_line_magic('matplotlib', 'qt')
if NUM_DIMS == 3:
    a = tf_pts
    import matplotlib as mpl
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    xp = a[:,0]
    yp = a[:,1]
    zp = a[:,2]
    ax.plot(xp, yp, zp, 'bs')
    
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    import numpy as np


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Make data
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))

    # Plot the surface
    ax.plot_surface(x, y, z, color='b',alpha = 0.2)
    ax.scatter(xp, yp, zp, 'bs')
    plt.savefig(os.path.join(IMG_PATH, "In_Sphere"), format='png')
    plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




