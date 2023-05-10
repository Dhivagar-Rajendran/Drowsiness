#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os


# In[5]:


import shutil


# In[6]:


import glob


# In[7]:


from tqdm import tqdm


# In[8]:


Raw_DIR=r'C://Users//VE//Desktop//Project//mrlEyes_2018_01'
for dirpath, dirname, filenames in os.walk(Raw_DIR):
    for i in tqdm([f for f in filenames if f.endswith('.png')]):
        if i.split('_')[4]=='0':
            shutil.copy(src=dirpath+'/'+i, dst=r'C://Users//VE//Desktop//Project//prepared_data//closed_eyes')
        
        elif i.split('_')[4]=='1':
            shutil.copy(src=dirpath+'/'+i, dst=r'C://Users//VE//Desktop//Project//prepared_data//open_eyes')


# In[ ]:





# In[ ]:




