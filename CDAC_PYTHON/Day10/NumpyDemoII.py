#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


arr= np.random.randint(1,10,(3,3))
arr1= np.random.randint(1,10,(3,3))
print(arr)
print(arr1)


# In[3]:


#Addition
print(arr+arr1)


# In[5]:


#Sub
print(arr)
print(arr1)
print(arr-arr1)


# In[6]:


print(arr)
print(arr1)
print(arr*arr1)
print("--"*10)
print(arr/arr1)
print("--"*10)
print(arr%arr1)
print("--"*10)
print(arr//arr1)
print("--"*10)


# In[7]:


print(arr)
print(arr1)
print(arr.dot(arr1))


# In[10]:


#Accessing Array Element using index and Slicing
arr= np.arange(1,31).reshape(6,5)
print(arr)


# In[ ]:





# In[11]:


print(arr[0 ,0])
print(arr[4 ,2])


# In[12]:


print(arr[::2 ,:])


# In[13]:


print(arr)
print("---"*10)
print(arr[:,::2])


# In[14]:


print(arr)
print("---"*10)
print(arr[::2,::2])


# In[15]:


print(arr)
print("---"*10)
print(arr[:,(2,4)])


# In[16]:


print(arr)
print("---"*10)
print(arr[:,(1,4)])


# In[21]:


print(arr)
print("---"*10)
print(arr[(0,5),:])
print(arr[:,(0,4)])
print(arr[(0,5),0:5:4])


# In[43]:


arr=np.random.randint(1,10,10)
print(arr)
print("---"*10)
arr.sort() #sort array colwise
print(arr)


# In[ ]:





# In[ ]:





# In[27]:


arr=np.random.randint(1,10,(3,3))
print(arr)
print("---"*10)
arr.sort(axis=1) #sort array colwise
print(arr)


# In[26]:


arr=np.random.randint(1,10,(3,3))
print(arr)
print("---"*10)
arr1=np.sort(arr,axis=0) #sort array Rowwise
print(arr1)


# In[30]:


#append
arr=np.random.randint(1,10,(3,3))
arr1=np.random.randint(1,10,(3,3))
print(arr)
print("---"*10)
print(arr1)
print("---"*10)

arr3 = np.append(arr,arr1) #convert into 1d and append all elements
print(arr3)
arr3 = np.append(arr,arr1,axis=0) #appending data row wise
print(arr3)
print("---"*10)
arr3 = np.append(arr,arr1,axis=1) #appending data Column wise
print(arr3)
print("---"*10)


# In[31]:


#Filter Data
arr=np.random.randint(1,10,(3,3))
print(arr)
print("---"*10)
arr1=arr[arr%2==0]
print(arr1)


# In[32]:


#Filter Data
arr=np.random.randint(1,10,(3,3))
print(arr)
print("---"*10)
arr1=arr[arr%2==1]
print(arr1)


# In[34]:


#Filter Data
arr=np.random.randint(1,10,(3,3))
print(arr)
print("---"*10)
arr[arr%2==1]=-1
print(arr)


# In[40]:


arr=np.random.randint(1,10,10)
print(arr)
print("---"*10)
print(arr.argmin())#return 1st index of min value 
print(arr.argmax()) #return 1st index of max value 


# In[41]:


#Unique values
arr=np.random.randint(1,10,10)
print(arr)
print("---"*10)
print(np.unique(arr))


# In[44]:


#Iterate Through Array element
arr=np.random.randint(1,10,10)
print(arr)
for i in arr:
    print(i)


# In[45]:


#reverse
arr=np.random.randint(1,10,10)
print(arr)
print(arr[::-1])


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




