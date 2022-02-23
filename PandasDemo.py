#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd


# In[62]:


df=pd.read_csv('mydata.csv')
#df = pd.read_csv('winequality-red.csv',delimiter=';') #kaggle
#df=pd.read_csv('survey_results_public.csv')


# In[63]:


df.head(8)


# In[64]:


df.shape


# In[65]:


pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows',6)


# In[66]:


df


# In[59]:


schema_df = pd.read_csv('survey_results_schema.csv') 


# In[67]:


schema_df


# In[61]:


pd


# In[ ]:





# In[ ]:




