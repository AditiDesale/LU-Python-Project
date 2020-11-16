#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


import pandas as pd
data = pd.read_csv("a.csv")


# In[15]:


data.dtypes


# In[14]:


data.describe()


# In[11]:


sum(list(data.kills)) / len(list(data.kills)) #avg


# In[17]:


np.percentile(data.kills,99)


# In[12]:


max(list(data.kills)) #max


# In[13]:


data.columns


# In[14]:


import seaborn as sns


# In[15]:


sns.distplot(data.matchDuration)


# In[16]:


sns.distplot(data.walkDistance)


# In[19]:


fig,axs=plt.subplots(2,1)
sns.displot(data.matchDuration,ax=axs[0]);
sns.displot(data.walkDistance,ax=axs[1]);


# In[20]:


fig,axs=plt.subplots(1,2)
sns.displot(data.matchDuration,ax=axs[0]);
sns.displot(data.walkDistance,ax=axs[1]);


# In[21]:


sns.pairplot(data.head(500));


# In[22]:


print("Unique value in matchType is:",pd.unique(data['matchType']))
print()
print("Count of unique value in matchType is:",len(pd.unique(data['matchType'])))


# In[26]:


plt.style.use('fivethirtyeight')
sns.barplot(data['matchType'],data['killPoints']);
plt.xticks(rotation=80);


# In[25]:


sns.barplot(data.matchType, data.weaponsAcquired)


# In[27]:


data.select_dtypes(exclude=["number","bool_"])


# In[28]:


sns.boxplot(data.matchType, data.winPlacePerc)


# In[29]:


sns.boxplot(data.matchType, data.matchDuration)


# In[31]:


sns.boxplot(data.matchDuration,data.matchType);
plt.xticks(rotation=60);


# In[32]:


data["KILL"]=(data.headshotKills+data.roadKills+data.teamKills)
kd=pd.DataFrame(data[['headshotKills','roadKills','teamKills','KILL']])
print(kd)


# In[17]:


sns.barplot(data.matchDuration, data.walkDistance)


# In[20]:


sns.scatterplot(data.kills, data.damageDealt)


# In[23]:


data.matchType.value_counts()


# In[24]:


sns.barplot(data.matchType, data.kills)


# In[25]:


sns.barplot(data.matchType, data.weaponsAcquired)


# In[ ]:




