#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[16]:


#List comprehension 
myList=[(i+1)*random.randint(-40,40) for i in range(15)]

## Old way

myList=[]
for i in range(15):
    myList.append((i+1)*random.randint(-40,40))


# In[17]:


myList


# Slicing operations in Python

# In[18]:


myList[0:3] #Including the start excluding the end 


# In[19]:


myList[-1]  # instead myList[len(myList)-1]


# In[28]:


myList[0:-1]


# The first number is the starting index <br>
# <br>
# The second number is the last index (not inclusive) <br>
# <br>
# The third number is the size of the steps (directed i.e. it has positive or negative direction)<br>
# <br>
# -1 is the index of the last element (think of the list wrapped so the last element is placed right before the first element. Now, if you go "forward" you could get from the first element to the last. If you go backwards (negative sign) you go in the direction that starts from the last element and ends with the first.

# In[29]:


myList[-1:0:-1] #


# In[37]:


myList[-1:-1:-1] # Could mistakingly think it reverses the list

#Because if you start at x and before you reach x you stop, you traverse nothing, 
#regardless of the direction


# In[38]:


myList[:]


# In[39]:


myList[::]


# In[40]:


myList[::-1]


# In[42]:


myList[::2]


# In[43]:


myList[::-2]


# In[ ]:




