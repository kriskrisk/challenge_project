
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np

dane = pd.read_csv("C:/Users/User/decks.csv")
dane= dane.set_index("deckName",drop = True)
games= pd.read_csv("C:/users/user/Downloads/training_games.csv",delimiter=';')
# do training_games.csv dodałem nagłowki

#klasy na inty zamieniam
dict = {'PLAYER_0 WON':0,'PLAYER_1 WON':1}
games["Wynik"] = games["Wynik"].map(dict)

# bohaterow mozna na inty bez szczegolnego porzadku
#di = dane["Hero"].value_counts()
#for i in range(0,9):
#    di[i] = i
#dane["Hero"]=dane["Hero"].map(di)
#ale wiecej ma sensu zamiana na dummy :

d_hero= pd.get_dummies(dane['Hero'])
dane = pd.concat([dane, d_hero], axis=1)

#wyrzucam kolumne Hero ale nei wyrzucam kolumny Druid - teoretycznei to zle bo 
#macierz d_hero nei ma pelnego rzedu, ale to przeszkadza tylko (chyba) w regresji liniowej
dane = dane.drop('Hero',axis =1)

# deckName juz jes tw indeksie wiec wyrzucam z kolumny
dane=dane.drop("deckName.1",axis=1)


# In[2]:


#pomocnicze 
x = dane.iloc[0].append(dane.iloc[1])


# In[ ]:


# no i tworze ostateczny data_set

zero_data = np.zeros(shape=(0,2*dane.shape[1]))
training_set = pd.DataFrame(zero_data,columns = x.index)
training_set = pd.concat( [dane.loc[games.loc[i]["Talia1"]].append(dane.loc[games.loc[i]["Talia2"]]) for i in range(0,games.shape[0])],axis=1,ignore_index = True)


# In[ ]:


training_set = training_set.transpose()
training_set.head()


# In[ ]:


from sklearn.model_selection import train_test_split as t
y = games['Wynik']
X_train,X_test,y_train,y_test = t(training_set,y,test_size = 0.10)


# In[ ]:


from sklearn.ensemble import RandomForestClassifier as RF
from sklearn.model_selection import GridSearchCV as Grid

forest_parameters = {'criterion':['gini','entropy'],'max_depth': [10,20,5]}
rf = RF()
grid = Grid(estimator =rf,param_grid = forest_parameters)
# to uzywa 3 krotne jwaldiacji krzyzowej do prownania wszytkich kombinacji parametrow
grid.fit(X_train,y_train)


# In[ ]:


from sklearn.ensemble import GradientBoostingClassifier as XGB
from sklearn.naive_bayes import MultinomialNB as NB
from sklearn.manifold import TSNE
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier as M
model_list = [SVC(),SVC(kernel = 'poly'),SVC(kernel = 'sigmoid'),M(activation = 'logistic',hidden_layer_sizes=[100,80] ),M(activation = 'logistic',hidden_layer_sizes=[50,20] ),TSNE(),NB()]


for model in model_list:
    model.fit(X_train,y_train)
    print(model.score(X_test,y_test))


# In[ ]:


X_d_2 = model_list[4].transform(X_train)
# TSNE sluzy do radykalnej redukcji wymiaru - w tym przypadk ud odwoch

