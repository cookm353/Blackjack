#!/usr/bin/env python3

cards = ['Ace']
faces = ['jack', 'queen', 'king']
cards.extend(list(range(2, 11)))


class Card:

    def __init__(self, card, suit):
        self.__card = card.title()
        self.__suit = suit.title()

        # Set card's value
        if card.lower() == "ace":
            self.__value = self.set_ace_value()
        elif card.lower() in faces:
            self.__value = 10
        else:
            self.__value = int(card)

    def __str__(self):
        return "{self.card} of {self.suit}".format(self=self)
        # display_card()

    # Getters
    @property
    def card(self):
        return self.__card

    @property
    def suit(self):
        return self.__suit

    @property
    def value(self):
        return self.__value

    # Setters
    @value.setter
    def value(self, value):
        self.__value = value

    # Utility methods
    def set_ace_value(self):
        return 11


def main():
    # Unit testing
    card = Card("jack", "spades")
    print(card)
    print(card.value)


if __name__ == "__main__":
    main()
    # pass
