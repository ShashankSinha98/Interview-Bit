#!/usr/bin/env python
# coding: utf-8

# In[86]:


arr = [1, 2, 5, -7, 2, 3]


# In[87]:


def maxset(A):
    
    A.append(-1)
    
    max_sum = 0
    curr_sum = 0
    result_arr = []
    curr_arr = []
    
    for i in A:
        
        if i>=0:
            curr_sum += i
            curr_arr.append(i)
        else:
            if curr_sum > max_sum:
                max_sum = curr_sum
                result_arr = curr_arr[:]
                
            elif curr_sum == max_sum:
                if len(curr_arr) > len(result_arr):
                    result_arr = curr_arr[:]
                    
            curr_arr.clear()
            curr_sum = 0
                    
                    
    return result_arr
                    


# In[88]:


maxset(arr)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




