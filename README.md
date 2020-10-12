# Blackjack <a name="top">
Object oriented blackjack program with classes for cards, hands, and decks each in individual files.  It's nothing fancy, mostly just practice using OOP in Python.

* Card <a href=#card>
* Hand <a href=#hand>
* Deck <a href=#deck>

## Card <a name="card">
Class representing a playing card

## Deck <a name="deck">
Class representing a deck of playing cards.  It's only property is a list of all 52 playing cards.  It has two utility methods:</br>

  shuffle(self): Creates a new deck at the start of each game.  This method is called when a new deck object is created, so you can either create a new deck object each time or call this method.</br>  
  deal_card(self): Removes a random card from the deck and returns it.  This method is called by the Hand.take_card() method, so there's no need to call it.
  

## Hand <a name="hand">
Class representing a hand.  It has two main properties: the hand's value and a list containing the cards in it.  It has two utility methods:</br>
  
  show_hand(self): Display the cards currently in the hand and the value of the cards</br>  
  take_card(self, deck): Remove a card from the deck, add it to the hand, and update the hand's value.  A deck object must be initialized and passed to this method as an argument.  

## TO-DO
Finish building the main game file, edit this readme to include other details about program and make the intenral links actually work right.
