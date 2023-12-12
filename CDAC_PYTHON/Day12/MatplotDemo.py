#!/usr/bin/env python
# coding: utf-8

# #Step 1: Install All Libraries
# 
# pip install matplotlib
# 
# pip install seaborn
# 
# pip install plotly
# 

# In[1]:


import matplotlib.pyplot as plt


# In[8]:


students=[10, 3,5,8,12]
marks=[36,30,23,33,14]

plt.plot(students,marks)
plt.title("Student Data")
plt.xlabel("no of Students")
plt.ylabel("Marks")
plt.show()


# In[ ]:





# In[9]:


students=[10, 3,5,8,12]
marks=[36,30,23,33,14]

plt.bar(students,marks)
plt.title("Student Data")
plt.xlabel("no of Students")
plt.ylabel("Marks")
plt.show()


# In[5]:


students=[10, 3,5,8,12]
marks=[36,30,23,33,14]

plt.bar(students,marks,color="r")
plt.show()


# In[14]:


students=[10, 3,5,8,12]
marks=[36,30,23,33,14]

plt.scatter(students,marks,color="r")
plt.show()


# In[15]:


students=[10, 3,5,8,12]
marks=[36,30,23,33,14]

plt.scatter(students,marks,color="r",marker="*")
plt.show()


# In[10]:


students=[10, 3,5,8,12]
marks=[36,30,23,33,14]

plt.plot(students,marks,color="r",marker=">",linestyle="--")
plt.show()


# In[13]:


students=[10, 3,5,8,12]
marks=[36,30,23,33,14]

plt.hist(students)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




