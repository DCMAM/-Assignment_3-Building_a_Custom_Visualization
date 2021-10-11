
# coding: utf-8

# # Assignment 3 - Building a Custom Visualization

# Use the following data for this assignment:

import pandas as pd
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])
df


# In[2]:

df = df.transpose()
df


# In[3]:

import math

mean = list(df.mean())

std = list(df.std())

confidence = []

for i in range (4) :
    confidence.append(1.96*(std[i]/math.sqrt(len(df))))
    
confidence  


# In[4]:

Y = 39500

def compute_prob(Y):
    nearest = 150
    df_p = pd.DataFrame()
    df_p['diff'] = nearest*((Y - df.mean())//nearest)
    df_p['sign'] = df_p['diff'].abs()/df_p['diff']
    old_range = abs(df_p['diff']).min(), df_p['diff'].abs().max()
    new_range = .5,1
    df_p['shade'] = df_p['sign']*np.interp(df_p['diff'].abs(), old_range, new_range)
    return df_p['shade']


# In[5]:

from matplotlib import cm

shade = list(compute_prob(Y))
colors = ['White' if  x == 0 else cm.Reds(abs(x))
         if x<0 else cm.Blues(abs(x)) for x in shade]


# In[6]:

import matplotlib.pyplot as plt

get_ipython().magic('matplotlib inline')

plt.figure(figsize=(8, 8))

title = plt.title('Easy Option - Bar Coloring')
plt.xticks(range(len(df.columns)), df.columns)
plt.bar(range(len(df.columns)), 
        height = df.values.mean(axis = 0), 
        yerr=confidence, 
        error_kw={'capsize': 10, 'elinewidth': 2, 'alpha':0.7}, 
        color = colors)
h_line = plt.axhline(y=Y, color = 'black', label = 'Y')
h_text = plt.text(3.5, 40000, Y)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.show()


# In[ ]:




# In[ ]:




# In[ ]:



