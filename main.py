#!/usr/bin/env python3.7
"""
Testing Suit and Card classes.
"""
from Deck import Deck3 as Deck
from GameStrategy import GameStrategy
from Hand import Hand

if __name__ == '__main__':
    deck = Deck(5)
    hand = Hand(deck.pop(), deck.pop(), deck.pop())
    dumb = GameStrategy()
    print('')
