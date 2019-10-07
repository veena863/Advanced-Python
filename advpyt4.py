#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#PANDAS


# In[ ]:


#pandas are used for data Analytics or data analysis


# In[2]:


get_ipython().system('pip install pandas')


# In[ ]:


#understanding data structure of Pandas:
#1 Series
#2 Dataframe
#3 Panel------Used in aerospace Engineering


# In[ ]:


#Note: All the above data structures are built on top of NUMPY


# In[3]:


#Series         :1D array(Singular format and homogenous array)
#Dataframes     :2D array(Tabular format)
#Panel          :3D based concepts


# In[ ]:


#What type of dattypes pandas consist of?
#All Panda's data structures are immutable except series datatype which is 


# In[6]:


import pandas as pd
#Pandas Series
#Basic Syntax---pandas.series(data,index,dtype,copy)
s=pd.Series()
print(s)
#float64---->Pandas built on Numpy--->Numpy default datatype is float


# In[9]:


#import Numpy and Pandas then we can have all the functionalities
import numpy as np
import pandas as pd
data=np.array(['a','b','c','d','e'])
s=pd.Series(data)
print(s)


# In[11]:


#how to get customized indexing?(100,101,102,103,104)
data=np.array(['a','b','c','d','e'])
s=pd.Series(data,index=[100,101,102,103,104])
print(s)


# In[ ]:




