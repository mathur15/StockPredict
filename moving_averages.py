#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


# In[16]:


#import data
df = pd.read_csv('VTI.csv')
#optimize for N
N_max=20
df.sort_values(by='Date',inplace=True,ascending=True)
df.head(5)


# In[19]:


ax=df.plot(x='Date',y='Adj Close',grid=True)
ax.set_xlabel('Date')
ax.set_ylabel('Adj Price(USD)')
plt.show()


# In[22]:


#split data into train,validation and test
train_size = int(0.6 * len(df))
validation_size = int(0.2 * len(df))
test_size = int(0.2 * len(df))

df_train = df[:train_size]
df_validation = df[train_size:train_size+validation_size]
df_test = df[train_size+validation_size:]


# In[26]:


#plot dataframes
ax = df_train.head(10).plot(x='Date',y='Adj Close',grid=True,style='r-')
ax = df_validation.head(10).plot(x='Date',y='Adj Close',grid=True,style='b-',ax=ax)
ax = df_test.head(10).plot(x='Date',y='Adj Close',grid=True,style='g-', ax=ax)
ax.legend(['train','validation','test'])
ax.set_xlabel('Date')
ax.set_ylabel('Prices(USD)')


# In[ ]:




