#!/usr/bin/env python
# coding: utf-8

# In[64]:


arr = [0,1,0,9]


# In[67]:


def plusOne(A):
        
    str_num = ""

    for i in A:
        str_num += str(i)
            
    int_num = int(str_num)
        
    modified_int_num = int_num + 1
        
    result = [i for i in str(modified_int_num)]
        
    return result


# In[68]:


ans = plusOne(arr)


# In[69]:


print(ans)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




