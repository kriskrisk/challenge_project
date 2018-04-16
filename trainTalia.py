
# coding: utf-8

# In[121]:


import numpy as np
from numpy import genfromtxt
import pandas as pd
data = pd.read_json('C:/Users/User/Downloads/trainingDecks.json',lines=True)
cards =set()
#zbiorek wszytskich kart z training setu
for i in range(0,400):
    w = pd.DataFrame.from_dict(data.iloc[i,0])
    cards= set().union(cards,w.columns.tolist())
karty = dict.fromkeys(cards,0)
zero_data = np.zeros(shape=(400,len(cards)))
dane = pd.DataFrame(zero_data,columns = karty.keys())
for i in range(0,400):
    for key in data.iloc[i,0]:
        ww = dane[key]
        ww[i] = data.iloc[i,0][key][0]
        dane[key] = ww
dane['deckName'] = data['deckName']
dane['Hero'] =data['hero']


# In[122]:


dane.head()

