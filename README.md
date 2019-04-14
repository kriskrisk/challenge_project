# Challenge Project

A project for the Machine Learning course @ MIMUW.<br />
Project was made as a solution to machine learning challenge: 
[link](https://knowledgepit.fedcsis.org/contest/view.php?id=123).<br />
In brief, the task is to estimate win rates for decks of 
[Hearthstone](https://en.wikipedia.org/wiki/Hearthstone) cards.

## Data

There are two types of data, first concerning decks and second concerning the course of games played using this decks.
Decks are represented as sets of cards. Each card has its properties:
* mana cost
* rarity (common, rare, legendary)
* type (enchantment, hero, minion)
* class (druid, hunter, mage)
* mechanic - special ability (add to hand, battlecry, bomb)
* race
* and others...

Second part of data set contains all the information about games: every possible action with a card, 
every attack, use of special ability or spell. Of course there is information about winner of a game as well.
Games were played between four bots. 

## Problem

Problem statement is simple: given a deck of Hearthstone cards predict overall win rate of this deck.

## My solution

I've tried two approaches: naive Bayes and neutral networks.
During data analysis I discovered interesting property of this data.
There are few groups of decks. Every deck from data set belongs to one of this groups.
Moreover, every deck from a group is very similar to other decks from the same group and very different from decks
from other groups. Finally, decks belonging to the same group have similar win rates.
This allows to look at this problem as clustering problem (at least to boost results).
As a result I've achieved much better results using CNN than NB.  
