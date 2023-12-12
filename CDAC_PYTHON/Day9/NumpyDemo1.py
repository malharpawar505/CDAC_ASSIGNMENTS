#!/usr/bin/env python
# coding: utf-8

# In[40]:


print("Hello World")


# In[41]:


"hello world"


# In[42]:


import numpy as np


# In[43]:


print(np.__version__)


# In[44]:


lst=[1,2,3]
arr=np.array(lst)
print(arr)
print(arr.dtype)
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.itemsize)
print(arr.data)
print(list(arr.data))




# In[45]:


lst=[[1,2,3],[10,20,30]]
arr=np.array(lst)
print(arr)
print(arr.dtype)
print(arr.ndim)
print("------------------"*2)
print(arr.shape)
print("------------------"*2)
print(arr.size)
print("------------------"*2)
print(arr.itemsize)
print("------------------"*2)
print(arr.data)
#print(list(arr.data))


# In[46]:


lst=[[[11,22,33],[10,20,30]],
     [[12,32,33],[100,200,300]],
     [[15,25,35],[110,120,130]],
     [[115,125,35],[1110,1120,1130]]
    ]
arr=np.array(lst)
print(arr)
print("------------------"*2)
print(arr.dtype)
print("------------------"*2)
print(arr.ndim)
print("------------------"*2)
print(arr.shape)
print("------------------"*2)
print(arr.size)
print("------------------"*2)
print(arr.itemsize)
print("------------------"*2)
print(arr.data)


# In[47]:


lst=[1,2.6,3]
arr=np.array(lst)
print(arr)
print(arr.dtype)
print("------------------"*2)
print(arr.ndim)
print("------------------"*2)
print(arr.shape)
print("------------------"*2)
print(arr.size)
print("------------------"*2)
print(arr.itemsize)
print("------------------"*2)
print(arr.data)
print(list(arr.data))


# In[58]:


lst=[1,2.6,'3']
arr=np.array(lst)
print(arr)
print("------------------"*2)
print(arr.dtype)
print("------------------"*2)
print(arr.ndim)
print("------------------"*2)
print(arr.shape)
print("------------------"*2)
print(arr.size)
#print(arr.itemsize)
print(arr.data)
#print(list(arr.data))


# #Differernt ways to create numpy arrays

# In[49]:


#1. array
lst=[1,2,3,4,5]
arr= np.array(lst)
print(arr)


# In[50]:


#2. Ones
arr= np.ones(6)
print(arr)

arr= np.ones(6,dtype=int)
print(arr)
print("------------------"*2)

arr= np.ones((3,2),dtype=int)
print(arr)
print("------------------"*2)

arr= np.ones((2,3,4),dtype=int)
print(arr)


# In[51]:


#3. Zeros
arr= np.zeros(6)
print(arr)

arr= np.zeros(6,dtype=int)
print(arr)
print("------------------"*2)

arr= np.zeros((3,2),dtype=int)
print(arr)
print("------------------"*2)

arr= np.zeros((2,3,4),dtype=int)
print(arr)


# In[52]:


#4. Empty
arr= np.empty(6)
print(arr)

arr= np.empty(6,dtype=int)
print(arr)
print("------------------"*2)

arr= np.empty((3,2),dtype=int)
print(arr)
print("------------------"*2)

arr= np.empty((2,3,4),dtype=int)
print(arr)


# In[53]:


#5. Full
arr= np.full(6,8.5)
print(arr)

arr= np.full(6,5,dtype=int)
print(arr)
print("------------------"*2)

arr= np.full((3,2),10,dtype=int)
print(arr)
print("------------------"*2)

arr= np.full((2,3,4),34,dtype=int)
print(arr)


# In[54]:


#6. Identity
#it will by default create 2d array 

arr= np.identity(6)
print(arr)
print("------------------"*2)
arr= np.identity(6,dtype=int)
print(arr)


# In[55]:


#7. eye

arr= np.eye(3,3,k=0,dtype=int)
print(arr)
print("------------------")
arr= np.eye(3,3,k=-1,dtype=int)
print(arr)
print("------------------")
arr= np.eye(3,3,k=1,dtype=int)
print(arr)


# In[56]:


#8. random.random

arr= np.random.random(3)
print(arr)
print("------------------"*2)
arr= np.random.random((3,3))
print(arr)
print("------------------"*2)
arr= np.random.random((3,2,4))
print(arr)


# In[57]:


#9. random.randint

arr= np.random.randint(1,10,3)
print(arr)
print("------------------"*2)
arr= np.random.randint(10,50,(3,3))
print(arr)
print("------------------"*2)
arr= np.random.randint(100,150,(3,2,4))
print(arr)


# In[61]:


#10. arange

arr= np.arange(12)
print(arr)
print("------------------"*2)


arr= np.arange(5,12)
print(arr)
print("------------------"*2)


arr= np.arange(1,12,2)
print(arr)
print("------------------"*2)


# In[64]:


#10. arange with reshape

arr= np.arange(12).reshape(4,3)
print(arr)
print("------------------"*2)


arr= np.arange(12).reshape(2,2,3)
print(arr)
print("------------------"*2)


# In[76]:


#Converting Multi dimentional array into Single Dimention
#1 flatten
arr= np.arange(12).reshape(2,2,3)
print(arr)
print("------------------"*2)
print(arr.flatten())
print("------------------"*2)

#2 reshape
arr1= np.array([[1,2,3],[1,2,3]])
print(arr1)
print("------------------"*2)

print(arr1.reshape(-1))
print("------------------"*2)



# In[78]:


#2 reshape Used to change the Shape of array 
#No of elements should be same
arr1= np.array([[1,2,3],[1,2,3]])
print(arr1)
print("------------------"*2)
print(arr1.reshape(3,2))


# In[81]:


#Resize() Used to change the Size of array
#resultant elements may not be same
arr= np.random.randint(1,10,(3,4))
print(arr)
print("------------------"*2)
arr.resize(2,2)
print(arr)


# #Mathamatical operations

# In[85]:


arr= np.random.randint(1,10,(3,4))
print(arr)
print("------add 1------------"*2)
print(arr+1)
print("-----multiply by 2-------------"*2)
print(arr*2)

print("-----cube of each ------------"*2)
print(arr**3)

print("-----Devide  floor devision ------------"*2)
print(arr//2)

print("-----Devide  float devision ------------"*2)
print(arr/2)

print("-----Modulus  each ------------"*2)
print(arr%2)




# In[87]:


#Transpose of Matrix
arr= np.random.randint(1,10,(3,4))
print(arr)
print("---"*10)
print(arr.T)


# #Max,min,sum function

# In[93]:


arr= np.random.randint(1,10,(3,4))
print(arr)
print("---"*10)

print(arr.max())
print(arr.min())
print(arr.sum())

print("---"*10)
print("---Rowise-------------")
print(arr)
print("max: ",arr.max(axis=0))
print("min: ",arr.min(axis=0))
print("sum: ",arr.sum(axis=0))

print("---"*10)
print("---Colwise-------------")
print(arr)
print("max: ",arr.max(axis=1))
print("min: ",arr.min(axis=1))
print("sum: ",arr.sum(axis=1))


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




