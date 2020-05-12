#!/usr/bin/env python
# coding: utf-8

# In[79]:


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


# In[80]:


import sys


# In[86]:


# Kadane's Algo
max_so_far = -sys.maxsize
max_end_here = -sys.maxsize

for i in range(len(arr)):
    max_end_here += arr[i]
    
    if max_end_here > max_so_far:
        max_so_far = max_end_here
        
    if max_end_here < 0:
        max_end_here = 0


# In[87]:


print(max_so_far)


# In[ ]:





# In[ ]:





# In[ ]:




