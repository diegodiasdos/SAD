
# coding: utf-8

# ## Aula de Data  Science 

# In[2]:

print ("ola mundo")


# In[33]:

#!/bin/python

n = int(raw_input('Digite  um numero'))
resultado =1 
lista = range(1,n+1)

for x in lista:
    resultado= x*resultado
print'% s!= % s'%(n,resultado)


# In[34]:

import pandas as pd


# In[ ]:




# In[20]:

import numpy as np 


# In[21]:

s=pd.Series(np.random.randn(5), index=['a','b','c','d','e'])


# In[22]:

#Index 
print (s[0])
print("\n")
print (s[:3])


# In[23]:

#Create  a dataframe 
df = pd.DataFrame(s,columns = ['coluna 1'])
df 


# In[26]:

# Easy to add columms 
df['Coluna 2'] = df['coluna 1'] * 4
df 


# In[28]:

df.sort_values(by = 'Coluna 2')


# In[30]:

#boolean indexing 
df[df['Coluna 2'] <= 2]


# In[35]:

df.apply(lambda x: min(x) +max(x))
np.mean(df)


# In[38]:

table = df.describe()
table


# In[39]:

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
plt.style.use('ggplot')


# In[40]:

#read in data into  a dataframe 

df = pd.read_csv('c:/data/GlobalTemperatures.csv')

#Show  the  first 5 rows of the  table 
df.head(10)


# In[ ]:



