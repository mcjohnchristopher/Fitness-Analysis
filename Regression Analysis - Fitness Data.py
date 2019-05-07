#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf


# In[8]:


#importing the data from csv and assigning it to the data frame
Fitness_data = pd.read_csv("D:\Studies\MACHINE  LEARNING\python\Sleep Analysis\Workout.csv")
df = pd.DataFrame(Fitness_data, columns=["distance"])
target = pd.DataFrame(Fitness_data,columns=["duration"])
Fitness_data.head()


# In[9]:


#Linear Regression Using Statsmodels
model = sm.OLS(df.astype(float),target.astype(float)).fit()
predictions = model.predict(df)
model.summary()


# In[ ]:




