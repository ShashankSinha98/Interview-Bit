#!/usr/bin/env python
# coding: utf-8

# In[30]:


A=[2,2,2]


# In[31]:


import sys


# In[35]:



def maxArr(arr):
    max_val = -sys.maxsize
    
    arr1 = [] # A[i]+i
    arr2 = [] # A[i]-i
    
    for i in range(len(arr)):
        arr1.append(arr[i]+i)
        
    for i in range(len(arr)):
        arr2.append(arr[i]-i)
        
    maxArr1 = max(arr1)
    minArr1 = min(arr1)
    
    maxArr2 = max(arr2)
    minArr2 = min(arr2)
    
    if abs(maxArr1-minArr1) > max_val:
        max_val = abs(maxArr1-minArr1)
        
    if abs(maxArr2-minArr2) > max_val:
        max_val = abs(maxArr2-minArr2)
        
    return max_val
        
    


# In[36]:


ans = maxArr(A)


# In[37]:


ans


# In[ ]:




