#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
# Need to print even numbers till 20 by using numpy functions
x=np.arange(2,20,2)
x


# In[4]:


#Stepfunction with decimal values

array_of_float=np.arange(0,2,0.3)
array_of_float


# In[9]:


array_2d=np.array([[2,4,6],[3,5,7]])
array_2d
array_2d.shape


# In[11]:


a=np.arange(6)
a


# In[13]:


array_nd=np.arange(100).reshape(10,10)
array_nd
#reshape should be multiple of given range number if we dont give multiples of values then we get error as
#cannot reshape array size


# In[15]:


array_nd=np.arange(100).reshape(3,25)
array_nd


# In[ ]:




