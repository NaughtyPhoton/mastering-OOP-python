#!/usr/bin/env python3.7
"""
Testing Suit and Card classes.
"""
from Deck import Deck

if __name__ == '__main__':
    deck = Deck()
    hand = [deck.pop(), deck.pop()]
    print('')
