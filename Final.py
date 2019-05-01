#!/usr/bin/env python
# coding: utf-8

# In[18]:


#importing packages
import glob
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt
import time
import numpy as np
import seaborn as sb
import re


# In[19]:


Fitness_data = pd.read_csv("D:\Studies\MACHINE  LEARNING\python\Sleep Analysis\Workout.csv")
Fitness_data.head()


# In[22]:


Fitness_data.dtypes


# In[21]:


Fitness_data['end_time'] = pd.to_datetime(Fitness_data['end_time'])
Fitness_data['start_time'] = pd.to_datetime(Fitness_data['start_time'])
#Fitness_data['start_time'] = pd.to_datetime(Fitness_data['start_time'])
Fitness_data.dtypes
#Fitness_data['Time_Difference'] = Fitness_data['End_time'] -  Fitness_data['Start_time']
#Fitness_data.Time_Difference.head()


# In[51]:


index = Fitness_data.index
columns = Fitness_data.columns
values = Fitness_data.values
ypos = np.arange(len(Fitness_data.deviceuuid))


# In[24]:


#Assigning it to a dataframe for analysis 
Workout_Sample1 = Fitness_data[['deviceuuid','Start_time' , 'End_time' , 'Time_Difference', 'calorie']]


# In[28]:


#Graph 1 shows the average workout time per user
plt.title("Total Workout time")
plt.xlabel("Users")
plt.ylabel("time(hrs)")
plt.rcParams['figure.figsize'] = (10,10)
plt.bar(Fitness_data['deviceuuid'],Fitness_data['Time_Difference'])


# In[29]:


#Graph 2 shows the Calories burnt per user

plt.title("Calorie burnt per User")
plt.xlabel("Users")
plt.ylabel("Calories")
plt.rcParams['figure.figsize'] = (5,4)
plt.style.use('grayscale')
plt.bar(Workout_Sample1.deviceuuid,Workout_Sample1.calorie, color = 'blue')


# In[30]:


#Combining files for further analysis

path = "D:\Studies\MACHINE  LEARNING\python\Sleep Analysis"
file_identifier = "*.csv"
Merged_data = pd.DataFrame()
for f in glob.glob(path + "/*" + file_identifier):
    df = pd.read_csv(f)
    Merged_data = Merged_data.append(df,ignore_index=True)
    writer = pd.ExcelWriter('D:\Studies\MACHINE  LEARNING\python\Sleep Analysis\Merged_File.xlsx', engine='xlsxwriter') 
    Merged_data.to_excel(writer, sheet_name='Merged_data') 
    writer.save()


# In[31]:


Merged_data


# In[32]:


# Assigning the combined data into a dataframe for analysis

Workout_data2 = Merged_data[['deviceuuid','start_time' , 'end_time' , 'calorie', 'distance']]


# In[33]:


#Converting objects to datetime

Workout_data2['start_time'] = Workout_data2['start_time'].astype('datetime64[ns]')
Workout_data2['end_time'] = Workout_data2['end_time'].astype('datetime64[ns]')


# In[34]:


Workout_data2.dtypes


# In[35]:


#Graph3 Workout and Calorie Burnt

plt.title("Total Workout")
plt.xlabel("Workout Month")
plt.ylabel("Calorie Burnt")
plt.plot_date(Workout_data2.start_time,Workout_data2.calorie)


# In[36]:


#Graph4 Distance covered to burnt calorie

plt.plot(Workout_data2.calorie,Workout_data2.distance, color = 'green')


# In[37]:


#Reading the Steps file

Workout_data3=pd.read_csv("D:\\Studies\\MACHINE  LEARNING\\python\\Sleep Analysis\\step_count.csv")
Workout_data3.head()


# In[38]:


#Graph5 Calories burnt with distance based on steps covered

cols = ['#EE7550', '#F19463', '#F6B176']
plt.scatter(Workout_data3.distance, Workout_data3.calorie, facecolors='white', edgecolors='0', s = 5, lw = 0.7, marker='o')
plt.axvline(Workout_data3.distance.mean(), color='k', linestyle='dashed', linewidth=1)
plt.axhline(Workout_data3.calorie.mean(), color='k', linestyle='dashed', linewidth=1)
plt.text(42,1,'mean',rotation=90)
plt.text(10,8,'distance',rotation=0)


# In[39]:


Workout_data4 = pd.read_csv("D:\Studies\MACHINE  LEARNING\python\Sleep Analysis\sleepdata.csv", sep = ';')
Workout_data4.head()


# In[40]:


#Finding time differnce for sleep

Workout_data4['Sleep_start'] = pd.to_datetime(Workout_data4['Start'].values.astype('<M8[m]'))
Workout_data4['Sleep_End'] = pd.to_datetime(Workout_data4['End'].values.astype('<M8[m]'))
Workout_data4['Time_Slept'] = Workout_data4['Sleep_start'] -  Workout_data4['Sleep_End']


# In[41]:


Workout_data4_df = Workout_data4[['Sleep_start' , 'Sleep_End' , 'Time_Slept', 'Activity (steps)', 'Sleep quality']]
Workout_data4_df.head()


# In[42]:


Workout_data4_df['Hours_Slept'] = Workout_data4_df['Time_Slept'].dt.components['hours']
Workout_data4_df['Minutes_slept'] = ((Workout_data4_df['Time_Slept'].dt.components['hours'])*60) + (Workout_data4_df['Time_Slept'].dt.components['minutes'])
Workout_data4_df.head()


# In[43]:


plt.xlabel('Hours of Sleep')
plt.ylabel('No of Days')
plt.axhline(Workout_data4_df.Hours_Slept.mean(), color='k', linestyle='dashed', linewidth=1)
plt.text(12,20,'Avg hrs of sleep' ,rotation=0)
plt.hist(Workout_data4_df['Hours_Slept'], bins= 10, label = "SleepingTime", rwidth = 0.95)


# In[44]:


plt.xlabel('Minutes of Sleep')
plt.ylabel('No of Days')
plt.hist(Workout_data4_df['Minutes_slept'], bins= 12, label = "SleepingTime", rwidth = 0.95, color = 'orange')


# In[45]:


sb.scatterplot(Workout_data4_df['Minutes_slept'],Workout_data4_df['Activity (steps)'], color = 'red')

