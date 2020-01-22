import random


"""
This is a template that I am using to write my deck of cards. I am importing the
classes and contents of this python file and sharing all of class functionality
with the python blackjack game.

In the future I plan to reuse this deck of card template to create more card games
that have to do with a deck of cards.

I found out how to make this through a Youtube Channel called Executed Binary.

He goes through the steps of designing a deck of cards using classes which I feel
havent gotten much practice with.

Link for video: https://www.youtube.com/watch?v=t8YkjDH86Y4&t=114s

In the future I plan to use this template to maybe try and figure out how to make
a different variation to this deck of cards.

All credit to the original creator: https://github.com/eli-byers
"""

# Class to hold card information
class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    # A function to show each card in a formatted template.
    def show(self):
        if(self.value == 11):
            print("{} of {}".format("Jack", self.suit))
        elif(self.value == 12):
            print("{} of {}".format("Queen", self.suit))
        elif(self.value == 13):
            print("{} of {}".format("King", self.suit))
        elif(self.value == 14):
            print("{} of {}".format("Ace", self.suit))
        else:
            print("{} of {}".format(self.value, self.suit))


# This is a deck builder for the names
class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    # Where the building of the deck list takes place
    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]*6:
            for v in range (2, 15):
                self.cards.append(Card(s, v))

    # Where this shows each card inside of the deck
    def show(self):
        for c in self.cards:
            c.show()

    # This shuffles the deck
    def shuffle (self):
        for i in range(len(self.cards)-1, 0, -1):
            r =  random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    # This allows a card to be taken drawn from the deck using the pop method
    def drawCard(self):
        return self.cards.pop()

# This holds the information for the player
class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    # draw a card into player hand list
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    # easy call method that shows each card in the players hand
    def showHand(self):
        for card in self.hand:
            card.show()
