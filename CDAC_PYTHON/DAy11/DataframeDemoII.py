#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


dt={'id': {0: 1,1: 2,2: 3,3: 4,4: 5,5: 6,6: 7,7: 8,8: 9,9: 10,10: 11,11: 12,
  12: 13,13: 14,14: 15,15: 16,16: 17,17: 18,18: 19,19: 20,20: 21,21: 22,
  22: 23,23: 24,24: 25,25: 26,26: 27,27: 28,28: 29,29: 30,30: 31,31: 32,32: 33,
  33: 34,34: 35},
 'name': {0: 'John Deo',1: 'Max Ruin',2: 'Arnold',3: 'Krish Star',4: 'John Mike',
  5: 'Alex John',6: 'My John Rob',7: 'Asruid',8: 'Tes Qry',9: 'Big John',
  10: 'Ronald',11: 'Recky',12: 'Kty',13: 'Bigy',14: 'Tade Row',15: 'Gimmy',
  16: 'Tumyu',17: 'Honny',18: 'Tinny',19: 'Jackly',20: 'Babby John',21: 'Reggid',
  22: 'Herod',23: 'Tiddy Now',24: 'Giff Tow',25: 'Crelea',26: 'Big Nose',
  27: 'Rojj Base',28: 'Tess Played',29: 'Reppy Red',30: 'Marry Toeey',
  31: 'Binn Rott',32: 'Kenn Rein',33: 'Gain Toe',34: 'Rows Noump'},
  'class': {0: 'Four', 1: 'Three',2: 'Three',3: 'Four',4: 'Four', 5: 'Four',
  6: 'Five',7: 'Five',8: 'Six',9: 'Four',10: 'Six',11: 'Six',12: 'Seven',
  13: 'Seven',14: 'Four',15: 'Four',16: 'Six',17: 'Five',18: 'Nine',19: 'Nine',
  20: 'Four',21: 'Seven',22: 'Eight',23: 'Seven',24: 'Seven',25: 'Seven',
  26: 'Three',27: 'Seven',28: 'Seven',29: 'Six',30: 'Four',31: 'Seven',32: 'Six',
  33: 'Seven',34: 'Six'},'mark': {0: 75,1: 85,2: 55,3: 60,4: 60,5: 55,6: 78,
  7: 85,8: 78,9: 55,10: 89,11: 94,12: 88,13: 88,14: 88,15: 88,16: 54,17: 75,
  18: 18,19: 65,20: 69,21: 55,22: 79,23: 78,24: 88,25: 79,26: 81,27: 86,28: 55,
  29: 79,30: 88,31: 90,32: 96,33: 69,34: 88},
 'gender': {0: 'female',1: 'male',2: 'male',3: 'female',4: 'female',5: 'male',
  6: 'male',7: 'male',8: 'male',9: 'female',10: 'female',11: 'female',12: 'female',
  13: 'female',14: 'male',15: 'male',16: 'male',17: 'male',18: 'male',19: 'female',
  20: 'female',21: 'female',22: 'male',23: 'male',24: 'male',25: 'male',26: 'female',
  27: 'female',28: 'male',29: 'female',30: 'male',31: 'female',32: 'female',
  33: 'male',34: 'female'}}
df = pd.DataFrame(dt)
df


# In[3]:


df.drop(34,axis=0,inplace=True) #delete row at index 34


# In[4]:


df


# In[5]:


df.loc[34]=[99,"Riya","Six",76,"female"] #add new row in df


# In[6]:


df


# In[7]:


df.loc[34]=[99,"Rahul","Six",76,"male"] #Update new row in df


# In[8]:


df


# In[9]:


def grade(marks):
    if marks >=70:
        return "Distinction"
    elif marks>= 60:
        return "First class"
    elif marks>= 50:
        return "Second class"
    else:
        return "pass"
    
df["grade"]=list(map(grade,df["mark"]))
df


# In[11]:


df1=df.replace({'female':'F',"male":'M'})
df1


# In[16]:


df.replace({'female':'F',"male":'M'},inplace=True)  #on Entire df
df


# In[17]:


df["gender"].replace({'female':'F',"male":'M'},inplace=True)  #on Series/Single column
df


# In[ ]:





# In[15]:


df["gender"]=df["gender"].map({'F':'female',"M":'male'})
df


# #data Cleaning
# 
# 

# In[18]:


d={'a':[1,2,3,4,None],'b':[10,20,None,4,6],'c':[100,None,200,300,500],'d':[110,120,20,30,50]}
df=pd.DataFrame(d)
df


# In[20]:


df1=df.dropna()# delete rows having na values
df1


# In[21]:


df1=df.dropna(axis=0) # delete rows having na values
df1


# In[22]:


df


# In[23]:


df1=df.dropna(axis=1) # delete cols having na values
df1


# In[24]:


df1=df.fillna(0)
df1


# In[25]:


df1=df.fillna(10)
df1


# In[27]:


df["a"].mean()


# In[26]:


df1=df.fillna(df["a"].mean()) #fill na values with columns mean value
df1


# In[28]:


df.loc[0].mean() #Mean value of 1st row


# In[ ]:





# In[29]:


df1=df.fillna(df.loc[0].mean()) #fill na values with 1st rows mean value
df1


# In[30]:


df


# In[31]:


df["c"].isnull() #on entire column


# In[32]:


df.isnull() #on entire df


# In[33]:


pd.isnull(df.loc[1,"c"]) # check for single value


# In[34]:


d={'a':[1,2,3],'b':[10,20,30]}
d1={'a':[11,21,31],'b':[110,210,310]}
df1=pd.DataFrame(d)
df2=pd.DataFrame(d1,index=[4,5,6])
print(df1)
print(df2)


# In[36]:


print(pd.concat([df1,df2])) #concating Two DataFrame


# In[37]:


d={'id':[1,2,3],'name':['kirti','rashmi','rakesh']}
d1={'id':[1,2,4],'age':[12,34,57]}
df=pd.DataFrame(d)
df1=pd.DataFrame(d1)
print(df)
print(df1)


# In[38]:


df3=pd.merge(df,df1,on="id",how="inner")
df3


# In[39]:


df3=pd.merge(df,df1,on="id",how="left")
df3


# In[40]:


df3=pd.merge(df,df1,on="id",how="right")
df3


# In[41]:


df3=pd.merge(df,df1,on="id",how="outer")
df3


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




