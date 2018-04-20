import numpy as np
import pandas as pd
import operator

TRAINING_DECKS_PATH = '../trainingDecks.json'
TRAINING_GAMES_PATH = '../training_games.csv'

data = pd.read_json(TRAINING_DECKS_PATH, lines=True)

data['hero'] = data['hero'].apply(operator.itemgetter(0))
data['deckName'] = data['deckName'].apply(operator.itemgetter(0))