#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[2]:


get_ipython().run_line_magic('pinfo', 're')


# In[3]:


s="The quick brown fox jumps over the lazy dog"
re.match("^The",s)


# In[5]:


re.search("^The",s)


# In[6]:


re.findall("^The",s)


# In[8]:


s="The quick brown fox jumps over the lazy crazy busy lazy dog"
re.findall("l..y",s)


# In[9]:


s="The quick brown fox jumps over the lazy crazy busy lazy dog"
re.search("l..y",s)


# In[11]:


s="The quick brown fox jumps over the lazy crazy busy lazy dog"
lst =list(re.finditer("l..y",s))
lst


# In[15]:


s="The quick brown fox jumps over the lazy crazy busy lazy dog"
s1=re.sub("o","oo",s)
s1


# In[36]:


re.findall("[a-z]+[oo]+[a-z]*",s1)



# In[38]:


s="The quick brown_fox jumps over_the lazy crazy busy lazy dog"
re.findall("[a-z]*_+[a-z]*",s)


# In[39]:


s="The quick brown_fox 345 jumps over_the lazy crazy 1234 busy lazy dog"
re.findall("[0-9]+",s)


# In[41]:


s="The quick brown_fox 3455 3456 9090 9090 jumps over_the lazy crazy 1234 1234 1234 9090 busy lazy dog"
re.findall("\d{4}\s+\d{4}\s+\d{4}\s+\d{4}\s+",s)


# In[42]:


s="The quick brown_fox 3455 3456 9090 9090 jumps over_the lazy crazy 1234 1234 1234 9090 busy lazy dog"
re.findall("\d{4}\s+",s)


# In[49]:


s="In this HTML tutorial, you will find more than 200 examples. With our online Try it Yourself editor, ravi@gmail.com you can edit sudha@yahoo.com and test each example yourself!"
re.findall("\s+[a-zA-Z0-9.]+@+[a-zA-Z.]+",s)

re.search("\s+[a-zA-Z0-9.]+@+[a-zA-Z.]+",s)


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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




