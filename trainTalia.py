
# coding: utf-8

# In[14]:


x


# In[54]:


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
dane = pd.DataFrame(zero_data,columns = sorted(list(karty.keys())))
for i in range(0,400):
    for key in data.iloc[i,0]:
        ww = dane[key]
        ww[i] = data.iloc[i,0][key][0]
        dane[key] = ww
dane['deckName'] = data['deckName']
dane['Hero'] =data['hero']
games= pd.read_csv("C:/users/user/Downloads/training_games.csv",delimiter=';')
# dodalem do training_games.csv nagłowki  !

def list_to_string(list):
    return list[0]
# decName sa jednoelemtnowymi listami teraz to naprawiam
dane['deckName']=dane['deckName'].apply(list_to_string)
dane['Hero']=dane['Hero'].apply(list_to_string)
#i ustaiwam deckName na index
dane =dane.set_index('deckName',drop=False)


# In[56]:


set_size =299680


# In[ ]:


zero_data = np.zeros(shape=(set_size,len(cards)))
training_set=pd.DataFrame(zero_data,columns = sorted(list(karty.keys())))
for i in range(0,set_size):
        training_set.loc[i] = dane.loc[games.loc[i]['Talia1']][0:330] - dane.loc[games.loc[i]['Talia2']][0:330]


# In[64]:





# In[67]:


training_set.loc[0]

