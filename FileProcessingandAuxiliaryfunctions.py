#!/usr/bin/env python
# coding: utf-8

# In[78]:


# Generators. We talked about iterables and iterators.

g=(x for x in range(10))  
l=[i for i in range(10)]

print(l)
    
print(next(g))

#print(g) 

x=next(g)


# In[79]:


print(next(g))


# In[80]:


#Cast to list. Note that only the last call is saved. Since next was called twice we are at 2
l=list(g)
l


# Generators are used when you would like to aovid cowrding the memory with a huge list or other data structure. If you can access the elements one at a time, you might want to use that. <br><br>
# 
# The general way of writing a generator is like defining a function only instead of return, you would yield 

# In[81]:


def halves(alist):
    for item in alist:
        yield(item/2)


# In[82]:


next(halves(l))


# In[83]:


for i in halves(l):
    print(i)


# In[84]:


#Python file processing could also allow you to read CSV files as if they are text files and
# process them.

#Reading CSV f
from csv import reader

def load_csv(filename):
    file = open(filename, "r")
    lines = reader(file)
    dataset = list(lines)
    #file.close()
    return dataset

datase=load_csv("mydata.csv")


# In[85]:


for line in load_csv('mydata.csv'): 
    print(line)


# In[64]:


#Could have printed the whole thing

print(load_csv('mydata.csv'))


# In[54]:


#Defining variables to allow multiple use and getting a summary gives a neater report.
filename='mydata.csv'
dataset=load_csv(filename)
print('Loaded data file {0} with {1} rows and {2} columns'.format(filename, len(dataset),
len(dataset[0])))


# We don't like to use lists though. This kind of file reading and writing does not 
# use the capabilities that numpy provides us with. However, simple file processing is something you should know.

# In[55]:


#To do everything you need you can import the entire library. To keep things lighter you can
# always just import ONLY what you need. We don't have to be that efficient here.
import csv


# In[ ]:


#dataset[0]=-8 
dataset


# In[73]:


def write_csv(filename,mylist):
    file = open(filename, "w") 
    write = csv.writer(file)    
    write.writerows(mylist)
    file.close()
    
write_csv('second.csv',dataset)


# In[ ]:


test=load_csv('second.csv')

for line in load_csv('second.csv'): 
    print(line)

#dataset


# In[88]:


f=open('third.csv', 'w')
write = csv.writer(f)     
write.writerows(dataset) 
#f.close()
    
for line in load_csv('third.csv'): 
    print(line)    


# <h6> Pandas for reading files

# In[77]:


from pandas import read_csv
filename = 'mydata.csv'
columns = ['first','second','third','fourth']
data = read_csv(filename, names=columns)


# In[ ]:




