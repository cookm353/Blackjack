# !/usr/bin/env python3

# Hand.py
# M. Cook
# Class representing a hand of cards

from card import Card
from deck import Deck


class Hand:

    def __init__(self):
        self.__value = 0
        self.__cards = []

    # Getters
    @property
    def value(self):
        return self.__value

    @property
    def cards(self):
        return self.__cards

    # Setters
    @value.setter
    def value(self, value):
        self.__value = value

    # Utility methods
    def show_hand(self):
        '''Display cards in hand'''
        for card in self.cards:
            print(card)

    def take_card(self, deck):
        '''Deal a card and place in hand'''
        card = deck.deal_card()
        self.value += card.value
        self.__cards.append(card)


def main():
    hand = Hand()
    deck = Deck()
    # card = deck.deal_card()
    hand.take_card(deck)
    hand.take_card(deck)
    hand.show_hand()
    print(hand.value)


if __name__ == "__main__":
    main()
