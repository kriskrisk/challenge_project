# challenge_project

SUS assignment 2.<br />
[Project description here](https://knowledgepit.fedcsis.org/contest/view.php?id=123)

## Content of repo:

### Data:

h - data set contains dummes for heros<br />
b2- data set contains dummies for two bots<br />

* X_test.csv - 200 rows - h
* X_train.csv - 1000 rows in each representation of two decks - h, b2
* y_dummies_train.csv - 1000 rows in each dummie representation of result of games from X_train, each result is a pair (1, 0) or (0, 1)
* y_train.csv - same as above, result is not a pair but a number
* prob.csv - win rate for all 400 training decks
* decks.csv - vactorized representation of all 400 training decks with mean win rate for every deck and win rate for every deck played by every bot - h

### Files:

* requirements.txt - set of all libraries that need to be installed to run programs from repo
* simple_approach.ipynb - first algorythms and a lot of trash
* neutral_networks.ipynb

## Results:

* Naive bayes, decision trees < -25
* Knn - to long to compute
* Nets and Conv Nets on two decks < -23 or to long to comput

### Nets:
First traind on 100 epochs to pisck best configuration, then trined longer.

* Conv Net on one deck (128 conv, 1000 dense, relu activation, sigmoid output, SGD) = -8.4
* Conv Net on one deck (128 conv, 1000 dense, relu softsign, sigmoid output, SGD) = -8.3
* Conv Net on one deck (128 conv, 1000 dense, relu softplus, sigmoid output, SGD) = -52
* Conv Net on one deck (128 conv, 1000 dense, relu softsign, sigmoid output, SGD, with classes for y) = -43
