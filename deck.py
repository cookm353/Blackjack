# !/usr/bin/env python3

# Deck.py
# M. Cook
# Class representing a deck of cards

from card import Card
from random import randint, seed


class Deck:

    def __init__(self):
        self.__deck = self.build_deck()

    # Getters
    @property
    def deck(self):
        return self.__deck

    # Utility functions

    def build_deck(self):
        '''Create a new deck of cards'''
        ranks = list(range(2, 11))
        ranks = list(map(lambda x: str(x), ranks))
        ranks.extend(['jack', 'queen', 'king'])
        ranks.insert(0, 'ace')
        suits = ('spades', 'diamond', 'hearts', 'clubs')

        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append(Card(rank, suit))
        return deck

    def deal_card(self):
        '''Deal a card and remove it from the deck'''
        # Count remaining cards and pick one at random
        num_cards = len(self.deck)
        for i in range(10):
            seed = randint(0, 10)
            index = randint(0, num_cards - 1)
        dealt_card = self.deck[index]

        # Remove card from deck and present it
        self.deck.pop(index)
        return dealt_card


def main():
    pass


if __name__ == "__main__":
    main()
    # pass
