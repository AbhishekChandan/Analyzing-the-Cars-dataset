#!/usr/bin/env python
# coding: utf-8

# # The data of different cars are given with different specification.We are going to analyze using the pandas framework
# 

# In[2]:


import pandas as pd


# In[6]:


car=pd.read_csv("Cars Data1.csv")


# In[ ]:





# In[5]:


car


# In[7]:


car.head()


# In[8]:


car.index


# In[9]:


car.shape


# In[10]:


car.columns


# In[14]:


car.nunique()


# In[15]:


car['Make'].value_counts()


# **Find the null value in dataset.If there are any null value in the column, then fill with the mean value of that column.**

# In[28]:


car.isnull().sum()


# In[30]:


car.index


# In[32]:


for x in range(0,433):
    print(x)


# In[35]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[31]:


car[x for x in range(0,433)].fillna(car['Cylinders'].mean(),inplace=True)


# In[ ]:





# In[26]:





# In[41]:


car.dtypes


# In[ ]:





# In[39]:


car['Cylinders'].fillna(car['Cylinders'].mean())


# In[45]:


car['Weight'].fillna(car['Weight'].mean(),inplace=True)


# In[ ]:





# In[ ]:





# In[46]:


car.isnull().sum()


# #

# In[ ]:





# In[ ]:





# In[37]:


car.isnull().sum()


# In[48]:


car['Weight'].fillna(car['Weight'].mean(),inplace=True)


# In[52]:


car.isnull().sum()


# **check what are the different tpes of amke are there in our dataset and what is the count(occurrence)of each make in the data.**

# In[51]:


car['Make'].value_counts()


# In[54]:


car.head(2)


# In[63]:


car[(car["Origin"]=='Asia')|(car["Origin"]=='Europe')]


# In[ ]:





# **show all the records where origin is Asia or Europe**

# In[68]:


car[car['Origin'].isin(['Asia','Europe'])]


# Remove all the records(rows) where weight is above 4000

# In[67]:


car[~(car['Weight']>4000)]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[23]:


car.isnull().sum()


# **Increase all the values of 'MPG_City' column by 3**

# In[69]:


car.head()


# In[71]:


car['MPG_City']=car['MPG_City'].apply(lambda x:x+3)


# In[72]:


car['MPG_City']


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




