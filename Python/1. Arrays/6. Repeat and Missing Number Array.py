#!/usr/bin/env python
# coding: utf-8

# In[1]:


arr = [3, 1, 2, 5, 3] 


# In[27]:


def repeatedNumbers(arr):
    
    n = len(arr)
    
    #sum(arr) - sum(range(1,n+1)) = A - B
    #sum([i**2 for i in arr])  -  sum([i**2 for i in range(1,n+1)]) =  (A+B) (A-B)
    
    a_minus_b = sum(arr) - sum(range(1,n+1))
    a_plus_b = int((sum([i**2 for i in arr])  -  sum([i**2 for i in range(1,n+1)])) / a_minus_b)
    
    A = (a_plus_b+a_minus_b)/2
    B = a_plus_b - A
    
    return int(A),int(B)


# In[28]:


A,B = repeatedNumbers(arr)


# In[29]:


print(A,B)


# In[ ]:





# In[ ]:




