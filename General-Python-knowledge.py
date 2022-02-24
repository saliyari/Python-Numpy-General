#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=4
y=6
print(x,y)


# In[2]:


print(4)
print(3)
#contrast to Javva


# In[3]:


print(3,end='')
print(4)
#To achieve same line printing


# In[42]:


list=[1,2,3,4,5]
list.sort(reverse=True)


# In[43]:


list[:3]


# In[5]:


list[2:]


# In[6]:


list[:]


# In[7]:


list[:-1]#Cyclic indexing 


# In[8]:


list[-2:-1] #This should make it clear once you can answer this you understand the slicing


# In[9]:


list[:2:-1]#The last one is the number of steps default is 1, could be negative.


# In[10]:


list[0:4:2]


# In[11]:


list[0:4:-2] # Can't go between those two indices with negative steps unless you "leave" the list (sequence for that matter)


# In[12]:


#Finally forgiving for index out of bound whenever possible
list[:30]


# In[13]:


5 in list


# In[14]:


6 in list 


# Exercise: Write a slicing of a list the reverses the list

# In[15]:


# Write your code here


# Some Strings and file exerrcises

# In[16]:




val='something'
val


# In[ ]:





# In[17]:


l1=[ i+1 for i in range(9)]
l1


# In[18]:


l2=[i-1 for i in range(2,11)]
l2


# In[19]:


l=l1+l2
l


# In[20]:


l1


# In[21]:


l1=l


# In[22]:


l1


# Remember Strings are immutable in Python just like they are in Java
# 
# If you try to assign a value to a character in a String you get a traceback, exception
# 
# You can reassign a value to a string variable

# In[23]:


string=('test')
string=string.upper()

print(string)

string='what?'

string


# In[24]:


print(string.find('ST')) #Not found is -1
print(string.find('at')) #Returns the index of the first occurence
count=0
0.7507185185185187==0.7507185185185187


# In[25]:


l3=[6,8,7,4,3,-1]
l3.sort()
l3
#What happens if you try print(l3.sort()) and why? This is a common mistake.
#Note that in Jupyter we don't have to write print() to print out the value of a variable. Makes us lazy, maybe, but again
#in a piece of Python code we hardly ever just print a variable except for debugging and when we use Jupyter we are drafting 
#code. If absolutely necessary we can add a print and turn 'l3' into 'print(l3)'. 


# You can use sum, min, max functions on a list. Not as a method of a list but as a built in function
# 

# In[26]:


sum(l3)
sum(l3)/len(l3) 


# Check "continue" and "break" in the context of conditionals and loops
# 

# In[27]:


#Do your own experiment here


# String to list via split. Sensitive to white space
# 

# In[28]:


l4=string.split()
l4


# In[29]:


l5='w h a t ?'.split()
l5
#You can see that this list has 5 elements in it versus 1 in the previous one


# In[ ]:


s2='this is another example'


# In[30]:


s2.split()
#Test a while space at the end, say \n


# ###### Something trickier: split ignores multiple white spaces. One blank or 10 are the same.
# 
# We can split based on a a character. Like "myname@mydomain.com".split('@') to get the email and domain separately

# In[31]:


"myname@mydomain.com".split('@')


# ###### Also multiple instances of a character to split
# 

# In[32]:


'alumni.iu.edu'.split('.')


# In[33]:


l='test'.split()
l


# In[34]:


test='This is a test string for \n checking the list'


# In[37]:


lst=test.split()
lst


# In[38]:


lst[0]


# In[39]:


if not lst[0]=='from': print('yes')


# In[40]:


len('\n')


# In[44]:


days=('test','tested','testing')


# In[45]:


days[2]


# In[47]:


days.index('test')


# In[48]:


lst.index('is')


# In[49]:


import re


# In[50]:


x='My 2 favorite numbers are 18 and 5'


# In[52]:


y=re.findall('[0-9]+',x)
y


# In[ ]:




