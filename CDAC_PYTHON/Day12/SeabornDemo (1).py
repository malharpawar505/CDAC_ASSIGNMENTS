#!/usr/bin/env python
# coding: utf-8

# In[6]:


import seaborn as sns
import numpy as np


# In[ ]:





# In[2]:


ds = sns.get_dataset_names()
ds


# In[3]:


df = sns.load_dataset("iris")
df


# In[4]:


df.describe()


# In[5]:


df.info()


# #
# displot
# lmplot
# lineplot
# relplot
# boxplot
# countplot
# scatterplot
# 

# In[8]:


xdata=np.random.randint(1,30,50)
ydata=np.random.randint(1,30,50)

print(xdata)
print(ydata)
d= sns.displot(x=xdata,y=ydata)
d


# In[14]:


xdata=np.random.randint(1,30,10)
ydata=np.random.randint(1,30,10)
sns.set(style="whitegrid") 
#dark
#white
#darkgrid
#whitegrid

#print(xdata)
#print(ydata)
d= sns.displot(x=xdata,y=ydata)
d


# In[15]:


df= sns.load_dataset("iris")
d= sns.displot(x="sepal_length",y="sepal_width",data=df)
d


# In[16]:


df= sns.load_dataset("iris")
d= sns.lineplot(x="sepal_length",y="sepal_width",data=df)
d


# In[17]:


df= sns.load_dataset("iris")
d= sns.lineplot(x="sepal_length",y="sepal_width",data=df,hue="species")
d


# In[18]:


df= sns.load_dataset("iris")
d= sns.barplot(x="sepal_length",y="sepal_width",data=df,hue="species")
d


# In[19]:


df= sns.load_dataset("iris")
d= sns.barplot(x="sepal_length",y="sepal_width",data=df)
d


# In[20]:


df= sns.load_dataset("iris")
d= sns.lmplot(x="sepal_length",y="sepal_width",data=df)
d


# In[21]:


df= sns.load_dataset("iris")
d= sns.lmplot(x="sepal_length",y="sepal_width",data=df,hue="species")
d


# In[23]:


df= sns.load_dataset("iris")
d= sns.scatterplot(x="sepal_length",y="sepal_width",data=df,hue="species",marker="*")
d


# In[27]:


df= sns.load_dataset("iris")
d= sns.displot(x="sepal_length",data=df,kde=True)
d


# In[31]:


df= sns.load_dataset("car_crashes")
d= sns.scatterplot(x="speeding",y="alcohol",data=df,marker="o")
d


# In[ ]:





# In[ ]:





# In[29]:


df= sns.load_dataset("car_crashes")
df.info()


# In[33]:


df= sns.load_dataset("iris")
d= sns.boxplot(x="sepal_length",y="sepal_width",data=df,hue="species")
d


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




