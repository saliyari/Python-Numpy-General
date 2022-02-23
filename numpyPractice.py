#!/usr/bin/env python
# coding: utf-8

# In[38]:


import numpy as np


# In[39]:


ar1=np.array([1,2,3])
ar1.reshape(1,3)
ar1.shape


# In[40]:


ar2=np.array([3,6,9])
ar2


# In[60]:


np.dot(ar1,ar2)


# In[42]:


A=np.array([[1,2,3],[3,6,9]])
A.shape


# </h4> Note what's happening in the cell below. I have added it after our session.

# In[64]:


np.dot(A,ar2)
#Figure out the details of this. prractice by changing values to make sure you know how it's working.


# In[65]:


A


# In[66]:


B=np.array([1,2,3]) 
B.shape


# In[67]:


A/B  #elementwise division Numpy creates a second copy of B and stacks it over B and then does elementwise division


# In[68]:


print(A/B)


# In[69]:


C=A*B
C.shape


# In[70]:


A/B


# In[71]:


C=np.array([1,0])
C


# In[72]:


x=np.array([1,2,4])
x_norm = np.linalg.norm(x,axis=0,keepdims=True)
x_norm


# In[73]:


def norm(x):
    return np.linalg.norm(x,axis=1,keepdims=True)

def Sigmoid (x):
    return x+1

Sigmoid(C)


# In[74]:


norm(A*B)


# In[75]:


x=np.array([[3,4,5],[0,9,3]])
#x
np.sum(x[0]+x[1])


# In[76]:


x=np.array([[1,2],[3,4]])


# In[77]:


a3darray = np.zeros((2, 2, 2))
a3darray


# In[78]:


a3darray[1][1][1]=5
a3darray[1][1][0]=9
a3darray[0][0][1]=5


# In[79]:


a3darray


# In[80]:


D=np.array([[1],[2],[3]])
D
D.shape


# In[81]:


np.log(5)  

np.log(A)


# In[ ]:





# In[ ]:




