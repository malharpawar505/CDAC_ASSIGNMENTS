#!/usr/bin/env python
# coding: utf-8

# In[5]:


import plotly.graph_objects as plty
import numpy as np


# In[ ]:





# In[9]:


xdata=np.random.randint(1,30,30)
ydata=np.random.randint(1,30,30)

fig= plty.Figure(data=plty.Scatter(x=xdata,y=ydata,mode="markers"))
fig


# In[12]:


county=["India","China","England","USA"]
population=[140,155,120,60]


fig= plty.Figure(data=plty.Pie(labels=county,values=population))
fig


# In[14]:


county=["India","China","England","USA"]
population=[140,155,120,60]


fig= plty.Figure(data=plty.Bar(x=county,y=population))
fig


# In[16]:


county=["India","China","England","USA"]
population=[140,155,120,60]


fig= plty.Figure(data=plty.Scatter(x=county,y=population))
fig


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




