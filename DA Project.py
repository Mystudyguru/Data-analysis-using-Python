#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


data = pd.read_csv(r"E:\Python DA/data.csv")


# In[4]:


data


# In[5]:


data.head()


# In[6]:


data.columns


# In[7]:


data.tail()


# In[8]:


data.describe()


# # relating the variables with scatterplot 

# In[10]:


sns.relplot(y="FirstDose", x="Population", data=data)


# In[11]:


sns.relplot(y="SecondDose", x="Population",data=data)


# In[ ]:


sns.pairplot(data)


# In[ ]:


sns.relplot(x='Population', y='UnknownDose', kind='line', data=data)


# In[ ]:




