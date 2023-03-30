#!/usr/bin/env python
# coding: utf-8

# In[90]:


#IMPORTING MODULES
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
get_ipython().run_line_magic('matplotlib', 'inline')


# In[91]:


#LOADING DATASET
df=pd.read_csv('Vaccination.csv')


# In[92]:


df.head()


# In[93]:


#Check how many NaNs for each column
df.isnull().sum()


# In[94]:


#Fill NaNs with 0 and then drop all areas with areaid = 0. 
df.fillna(0, inplace = True)
df.drop(df.index[df['areaid'] == 0], inplace = True)


# In[95]:


#Check how many nulls we have. SHould be none. 
df.isnull().sum()


# In[96]:


df.info()


# In[97]:


df['referencedate'] =  pd.to_datetime(df['referencedate'], format='%Y-%m-%d')


# In[98]:


#Print column names and drop the ones we don't intend to use. 
df.columns


# In[100]:


#We select to examine Thessaloniki
df_thess = df[df["area"] == 'ΘΕΣΣΑΛΟΝΙΚΗΣ'].copy()
df_thess


# In[15]:


df_thess.drop(df_thess.index[df_thess['totalvaccinations'] == 0], inplace = True)


# In[103]:


#Plot total vaccinations as a function of reference date
plt.figure(figsize=(18,6))
sns.lineplot(data=df_thess, x="referencedate", y="totalvaccinations")
plt.title("Total vaccinations in Thessaloniki May 2021 - May 2022")
plt.xticks(rotation=45)
plt.show()


# In[18]:


df_thess.drop(df_thess.index[df_thess['dailydose1'] == 0], inplace = True)


# In[104]:


#Plot daily dose of the first vaccine as a function of date
plt.figure(figsize=(18,6))
sns.lineplot(data=df_thess, x="referencedate", y="dailydose1")
plt.xticks(rotation=90)
plt.title("Daily vaccinations of the first vaccine dose in Thessaloniky")


# In[105]:


#Plot daily dose of the second vaccine as a function of date
plt.figure(figsize=(18,6))
sns.lineplot(data=df_thess, x="referencedate", y="dailydose2")
plt.xticks(rotation=90)
plt.title("Daily vaccinations of the second vaccine dose in Thessaloniky")


# In[106]:


#Plot daily dose of the third vaccine as a function of date
plt.figure(figsize=(18,6))
sns.lineplot(data=df_thess, x="referencedate", y="dailydose3")
plt.xticks(rotation=90)
plt.title("Daily vaccinations of the third vaccine dose in Thessaloniky")


# In[102]:


#We select to examine Athens
df_ath = df[df["area"] == 'ΚΕΝΤΡΙΚΟΥ ΤΟΜΕΑ ΑΘΗΝΩΝ'].copy()
df_ath


# In[26]:


df_ath.drop(df_ath.index[df_ath['totalvaccinations'] == 0], inplace = True)


# In[110]:


#Plot total vaccinations as a function of reference date
plt.figure(figsize=(18,6))
sns.lineplot(data=df_ath, x="referencedate", y="totalvaccinations")
plt.title("Total vaccinations in Athens May 2021 - May 2022")
plt.xticks(rotation=45)
plt.show()


# In[111]:


#Plot daily dose of the first vaccine as a function of date
plt.figure(figsize=(18,6))
sns.lineplot(data=df_ath, x="referencedate", y="dailydose1")
plt.xticks(rotation=90)
plt.title("Daily vaccinations for the first vaccine dose in Athens")


# In[112]:


#Plot daily dose of the second vaccine as a function of date
plt.figure(figsize=(18,6))
sns.lineplot(data=df_ath, x="referencedate", y="dailydose2")
plt.xticks(rotation=90)
plt.title("Daily vaccinations for second vaccine dose in Athens")


# In[113]:


#Plot daily dose of the third vaccine as a function of date
plt.figure(figsize=(18,6))
sns.lineplot(data=df_ath, x="referencedate", y="dailydose3")
plt.xticks(rotation=90)
plt.title("Daily vaccinations for third vaccine dose in Athens")


# In[114]:


#Printing the top 10 areas in Greece with vaccination analysis
vacc_by_area = df.groupby('area').max().sort_values('totalvaccinations', ascending=False)
vacc_by_area = vacc_by_area.iloc[:10]
vacc_by_area


# In[115]:


#The plot  of the first dose as a function of the area
plt.figure(figsize=(16, 7))
plt.bar(vacc_by_area.index, vacc_by_area.totaldose1)
plt.xticks(rotation = 90)
plt.ylabel('Total dose 1')
plt.xlabel('Area')
plt.show()


# In[116]:


#The plot  of the second dose as a function of the area
plt.figure(figsize=(16, 7))
plt.bar(vacc_by_area.index, vacc_by_area.totaldose2)
plt.xticks(rotation = 90)
plt.ylabel('Total dose 2')
plt.xlabel('Area')
plt.show()


# In[117]:


#The plot  of the third dose as a function of the area
plt.figure(figsize=(16, 7))
plt.bar(vacc_by_area.index, vacc_by_area.totaldose3)
plt.xticks(rotation = 90)
plt.ylabel('Total dose 3')
plt.xlabel('Area')
plt.show()


# In[39]:


total_vacc_by_area = df.groupby('area').max().sort_values('totalvaccinations', ascending=False)
total_vacc_by_area = total_vacc_by_area.iloc[:10]
total_vacc_by_area


# In[118]:


#The plot of total vaccinations as a function of the area
plt.figure(figsize=(16, 7))
plt.bar(total_vacc_by_area.index, total_vacc_by_area.totalvaccinations)
plt.title('Total vaccinations per area')
plt.xticks(rotation = 90)
plt.ylabel('Total vaccinations')
plt.xlabel('Area')
plt.show()


# In[ ]:





# In[ ]:




