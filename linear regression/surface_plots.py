#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import matplotlib.pyplot as plt


# In[22]:


a = np.arange(-1,1,0.01)
b = a


# In[23]:


a,b = np.meshgrid(a,b)
print(a)
print(b)


# In[27]:


fig = plt.figure()
axes = fig.gca(projection = "3d")
axes.plot_surface(a,b,b**2+a**2,cmap ="rainbow")
plt.show()


# In[28]:


fig = plt.figure()
axes = fig.gca(projection = "3d")
axes.contour(a,b,b**2+a**2,cmap ="rainbow")
plt.show()


# In[ ]:




