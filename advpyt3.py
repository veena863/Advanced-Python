#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
#rows and col operations:
#in a given 2d array----->axis=0----->cols
#                   ----->axis=1----->rows


# In[3]:


import numpy as np
numbers=np.arange(12).reshape(3,4)
#we need to calculate sum of cols
numbers.sum(axis=0)


# In[4]:


#to calculate sum of rows
numbers.sum(axis=1)


# In[5]:


numbers.min(axis=0)


# In[6]:


numbers.max(axis=1)


# In[10]:


#Statistical functions
test_scores=np.array([32.32,56.98,21.52,44.32,55.63,13.25,43.47,43.34])
print(np.mean(test_scores))

#Mean=(sum of test_scores)(N)
print(np.median(test_scores))


# In[ ]:




