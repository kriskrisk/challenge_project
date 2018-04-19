import numpy as np
import pandas as pd

TRAINING_DECKS_PATH = '../trainingDecks.json'
TRAINING_GAMES_PATH = '../training_games.csv'

data = pd.read_json(TRAINING_DECKS_PATH, lines=True)
cards = set()       # Set of all cards

for i in range(0, 400):
    w = pd.DataFrame.from_dict(data.iloc[i, 0])
    cards = set().union(cards, w.columns.tolist())

cards_names = dict.fromkeys(cards, 0)
zero_data = np.zeros(shape=(400, len(cards)))
decks_data = pd.DataFrame(zero_data, columns=sorted(list(cards_names.keys())))

for i in range(0, 400):
    for key in data.iloc[i, 0]:
        ww = decks_data[key]
        ww[i] = data.iloc[i, 0][key][0]
        decks_data[key] = ww

decks_data['deckName'] = data['deckName']
decks_data['Hero'] = data['hero']
games = pd.read_csv(TRAINING_GAMES_PATH, delimiter=';')


def list_to_string(list):
    return list[0]


decks_data['deckName'] = decks_data['deckName'].apply(list_to_string)
decks_data['Hero'] = decks_data['Hero'].apply(list_to_string)
decks_data = decks_data.set_index('deckName', drop=False)

set_size = 299680

ta = np.zeros(shape=(set_size, len(cards)))
training_set = pd.DataFrame(zero_data, columns=sorted(list(cards_names.keys())))

for i in range(0, set_size):
    training_set.loc[i] = decks_data.loc[games.loc[i]['Deck1']][0:330] - decks_data.loc[games.loc[i]['Deck2']][0:330]

print(training_set.loc[0])
