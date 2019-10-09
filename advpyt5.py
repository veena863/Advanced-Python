#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd#constants or scalars: The fixed value
x=pd.Series(5,index=[0,1,2])
print(x)


# In[9]:


#how to access the data from the series?
y=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(y[0])
#first 3 elements
print (y[:3])


# In[11]:


#customized index position
print(y['b'])


# In[12]:


#last 3 elements 
print(y[-3:])


# In[ ]:


#DATAFRAMES
#It is a 2D data structure data arranged in tabular fashion,in rows and cols
#Basic syntax

#pandas.DataFrames(data,index,dtype,copy)



#By which of all the things a dataframe can be created?
#list,dictionary,series,Numpy ndarrays,Another dataframe


# In[13]:


import numpy as np
import pandas as pd
df=pd.DataFrame()
print(df)


# In[14]:


#Creating dataframe from a list
data=[1,2,3,4,5]
df=pd.DataFrame(data)
print(df)


# In[16]:


data=[['anith','10'],['veena',15],['anil',20]]
df=pd.DataFrame(data,columns=['studentname','Marks'])
print(df)


# In[18]:


#Nan(not a number)
#creating a dataframe from a lsit of dictionaries
data=[{'a':1,'b':2},{'a':5,'b':10,'c':20}]
df=pd.DataFrame(data)
print(df)


# In[21]:


d={'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df=pd.DataFrame(d)
print(df)


# In[22]:


#how to select the coloumns manually?
print(df['two'])


# In[ ]:




