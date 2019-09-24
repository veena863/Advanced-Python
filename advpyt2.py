#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Arthematic operations on numpy array
import numpy as np
a=np.array([10,10,10])
b=np.array([5,5,5,])
a+b


# In[2]:


a-b


# In[3]:


a*b


# In[4]:


a/b
#whenever we are applying a division,output will be in float dtype


# In[5]:


a%b


# In[6]:


a%3


# In[7]:


a<5


# In[9]:


#modifying array without creating a new one
a+=3
a


# In[11]:


b+=a
b


# In[12]:


#unary operators
ages=np.array([12,15,18,20])
ages.sum()


# In[13]:


ages.min()


# In[14]:


ages.max()

