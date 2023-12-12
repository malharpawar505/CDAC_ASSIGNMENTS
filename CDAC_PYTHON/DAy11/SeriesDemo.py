#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


pd.__version__


# #Create Series Objects

# In[3]:


#Empty Series
s=pd.Series()
s


# In[4]:


lst =[10,20,30,40,50,60,70,80]
s= pd.Series(lst)
s


# In[6]:


lst =[10,20,30,40,50,60,70,80]
s= pd.Series(lst,index=['a','b','c','d','e','f','g','h'])
s


# In[7]:


tup =(10,20,30,40,50,60,70,80)
s= pd.Series(data=tup,index=['a','b','c','d','e','f','g','h'])
s


# In[8]:


arr =np.arange(11,19)
s= pd.Series(data=arr,index=['a','b','c','d','e','f','g','h'])
s


# In[9]:


s= pd.Series(12,index=['a','b','c','d','e','f','g','h'])
s


# #Accessing Series Values

# In[61]:


arr =np.arange(11,19)
s= pd.Series(data=arr,index=['a','b','c','d','e','f','g','h'])
s


# In[62]:


d={'a':10,'b':20,'c':30}
s= pd.Series(d)
s


# In[11]:


s[1]


# In[12]:


s[3:7]


# In[13]:


s['a']


# In[14]:


s['a':'f']


# In[15]:


s.loc['b']


# In[16]:


s.loc['b':'g']


# In[18]:


s.iloc[2]


# In[19]:


s.iloc[2:5]


# 
# #Mathamatical Operations on Single Series
# 

# In[20]:


arr =np.arange(11,19)
s= pd.Series(data=arr,index=['a','b','c','d','e','f','g','h'])
s


# In[21]:


s+1


# In[22]:


s*3


# In[23]:


s//2


# In[24]:


s/2


# In[25]:


s**2


# #Mathamatical Operations on 2 Series object

# In[26]:


arr =np.arange(1,5)
s= pd.Series(data=arr,index=['a','b','c','d'])
arr =np.arange(10,50,10)
s1= pd.Series(data=arr,index=['a','b','c','d'])
print(s)
print(s1)


# In[27]:


s+s1


# In[28]:


s1-s


# In[29]:


s1*s


# In[30]:


s1**s


# In[31]:


s1//s


# In[32]:


s1/s


# In[33]:


s1.add(s)


# In[34]:


s1.multiply(s)


# In[35]:


s1.pow(s)


# In[36]:


arr =np.arange(1,5)
s= pd.Series(data=arr,index=['a','b','c','d'])
arr =np.arange(10,50,10)
s1= pd.Series(data=arr,index=['a','b','e','f'])
print(s)
print(s1)


# In[37]:


s+s1


# In[38]:


s1.add(s, fill_value=10)


# #built in functions

# In[39]:


arr =np.arange(11,19)
s= pd.Series(data=arr,index=['a','b','c','d','e','f','g','h'])
s


# In[40]:


s.min()


# In[41]:


s.max()


# In[42]:


s.sum()


# In[43]:


s.all()


# In[44]:


s.any()


# In[45]:


s.head()


# In[46]:


s.head(3)


# In[47]:


s.tail()


# In[48]:


s.tail(2)


# In[50]:


s.describe()


# In[51]:


s.info()


# In[52]:


s.dtype #return data type of Series


# In[53]:


s[s>15] #filter data


# In[54]:


s['h']=100 #update the data


# In[55]:


s


# In[56]:


s['i']=100 #insert Data


# In[57]:


s


# In[58]:


s= pd.Series([1,2,3])
s


# In[59]:


s.index='a','b','c' #modified all index values


# In[60]:


s


# In[ ]:





# In[ ]:




