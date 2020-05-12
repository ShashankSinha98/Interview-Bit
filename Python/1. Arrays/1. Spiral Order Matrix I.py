#!/usr/bin/env python
# coding: utf-8

# In[50]:


arr = [[1],[2],[3]]


# In[60]:


def spiral(arr):
    T = 0
    B = len(arr)-1
    L = 0 
    R = len(arr[0])-1
    
    res = []
    
    while(T<=B and L<=R):
        
        for i in range(L,R+1):
            res.append(arr[T][i])
        T += 1
        
        if T<=B and L<=R:
            for i in range(T,B+1):
                res.append(arr[i][R])
            R -= 1
        
        if T<=B and L<=R:
            for i in range(R,L-1,-1):
                res.append(arr[B][i])
            B -= 1
        
        if T<=B and L<=R:
            for i in range(B,T-1,-1):
                res.append(arr[i][L])
            L += 1
        
    return res


# In[61]:


ans = spiral(arr)


# In[62]:


print(ans)


# In[ ]:




