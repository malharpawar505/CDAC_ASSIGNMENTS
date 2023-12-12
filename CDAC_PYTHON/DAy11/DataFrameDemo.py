#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


df = pd.DataFrame()
df


# In[4]:


d={'id':[10,20,30],'Name':['Radha','Rama','Keshav'],'marks':[56.89,45.8,90.9]}
df = pd.DataFrame(d)
df


# In[5]:


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


# In[6]:


df.info() # return info about DF


# In[7]:


df.describe() # Statistical analysis of numeric columns


# In[8]:


df.max()


# In[9]:


df.min()


# In[10]:


df.head()


# In[11]:


df.head(3)


# In[12]:


df.head(10)


# In[13]:


df.tail(10)


# In[14]:


df.tail()


# In[15]:


df.tail(2)


# In[23]:


df["name"] #Return COlumn


# In[17]:


df[["name",'mark']]


# In[18]:


df[['id',"name",'mark']]


# In[20]:


df['mark']


# In[21]:


df['mark'].value_counts() # Count of values


# In[22]:


df['gender'].value_counts() # Count of values


# In[24]:


df.shape


# In[25]:


df.shape[0] # no of rows


# In[26]:


df.shape[1] # no of columns


# In[27]:


df.index #return all index values


# In[28]:


df.columns #return all columns


# In[29]:


d={'id':[10,20,30],'Name':['Radha','Rama','Keshav'],'marks':[56.89,45.8,90.9]}
df1 = pd.DataFrame(d)
df1


# In[31]:


df1.columns=["no","nm","per"] #rename all the columns


# In[32]:


df1


# In[33]:


df1.rename(columns={"no":"id"}) #rename single column


# In[34]:


df1["total"] = 100 #Add new columns


# In[35]:


df1


# In[36]:


df1["total"] =df1["per"]+200 #if Total column exist then update all values if doesnt exist then insert new column
df1


# In[40]:


df1.drop(columns="total",inplace=True) 
# inplace = true that will modify current df by default it is False so it will return new df
df1


# In[45]:


df


# In[46]:


df[df["mark"]>60]


# In[47]:


df[df["mark"]<60]


# In[49]:


(df[df["mark"]<60]).count()


# In[50]:


(df[df["mark"]>60]).count()


# In[51]:


df[(df["mark"]>60) & (df["gender"] =="male")]


# In[52]:


df[(df["mark"]>60) & (df["gender"] =="male") & (df["class"] =="Five")]


# In[53]:


df[(df["mark"]>60) & (df["gender"] =="male") & ((df["class"] =="Five") | (df["class"] =="Seven"))]


# In[54]:


df[(df["mark"]>60) & (df["gender"] =="male") & (df["class"] =="Five") | (df["class"] =="Seven")]


# In[55]:


df.sort_values("mark") #by default sort in scending order of marks


# In[56]:


df.sort_values("mark",ascending=False) #sort in descending


# In[57]:


df.sort_values(["mark","class"]) #Sort data First Column and second on ascending


# In[58]:


df.sort_values(["mark","class"],ascending=[True,False]) #Sort data First Column on ascending and 2nd on descending


# In[59]:


df["mark"]


# In[60]:


#Call all basic function on Series object
print(df["mark"].count())
print(df["mark"].min())
print(df["mark"].max())
print(df["mark"].sum())
print(df["mark"].all())
print(df["mark"].any())


# In[61]:


df["name"]


# In[63]:


df["name"].str.upper()


# In[65]:


df[df["name"].str.startswith("A")] #return all records starting with A


# In[66]:


g=df.groupby("mark")


# In[68]:


list(g)


# In[69]:


g.groups


# In[71]:


g.first()


# In[72]:


g.last()


# #Accessing DataFrame by Index and Slicing
# 
# 

# In[73]:


df


# In[83]:


print(df.loc[0,"class"])


# In[84]:


print(df.loc[0:5,"class"])


# In[85]:


print(df.loc[0:5,"id":"class"])


# In[86]:


print(df.loc[:,:])


# In[87]:


print(df.loc[::2,"id":"class"])


# In[88]:


print(df.loc[::2,["id","class"]])


# In[89]:


print(df.iloc[:,:])


# In[90]:


print(df.iloc[::2,::2])


# In[91]:


print(df.iloc[2:20,1:3])


# In[92]:


df.iloc[19,1] ="Testing" #update the values


# In[93]:


df


# In[94]:


df


# In[96]:


#Write df in xlsx with index values
df.to_excel("C:\Snehal\CDAC\Sept 23\DBDA\Python\PythonProgs\DAy11\myfile.xlsx")


# In[97]:


#Write df in xlsx without index values
df.to_excel("C:\Snehal\CDAC\Sept 23\DBDA\Python\PythonProgs\DAy11\myfile1.xlsx",index=False)


# In[98]:


#read data from xlsx
df= pd.read_excel(r"C:\Snehal\CDAC\Sept 23\DBDA\Python\PythonProgs\DAy11\data\Order_data.xlsx")
df


# In[104]:


df[["Units","Unit Cost","Total"]].corr() # corelational data 


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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[43]:





# In[44]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




