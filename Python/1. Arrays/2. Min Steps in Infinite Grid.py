#!/usr/bin/env python
# coding: utf-8

# In[83]:


inp_arr = [(0,0),(2,0),(5,0)]


# In[86]:


def minSteps(arr):
    
    steps = 0
    
    for i in range(len(arr)-1):
        A = arr[i]
        B = arr[i+1]
        XA, YA = A
        XB, YB = B
        
        diag_diff = min(abs(XB-XA),abs(YB-YA))
        
        
        if XB>XA and YB>YA:
            # 1st Quad
            XC = XA + diag_diff
            YC = YA + diag_diff
        
        elif  XA>XB and YB>YA:
            # 2nd Quad
            XC = XA - diag_diff
            YC = YA + diag_diff
        
        elif XB>XA and YB<YA:
            # 4th Quad
            XC = XA + diag_diff
            YC = YA - diag_diff
        
        else:
            # 3rd Quad
            XC = XA - diag_diff
            YC = YA - diag_diff
            
        remm_step = max(abs(XC-XB),abs(YC-YB))
        
        steps+= (diag_diff + remm_step)
    
    return steps
    


# In[87]:


ans = minSteps(inp_arr)


# In[88]:


print(ans)


# In[ ]:





# In[ ]:




