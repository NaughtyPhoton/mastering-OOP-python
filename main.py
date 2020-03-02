#!/usr/bin/env python3.7
"""
Testing Suit and Card classes.
"""
from Deck import Deck3 as Deck
from Hand import Hand5 as Hand

if __name__ == '__main__':
    deck = Deck(5)
    hand = Hand(deck.pop(), deck.pop(), deck.pop())
    split_1, split_2 = Hand.split(hand, deck.pop(), deck.pop())
    frozen = Hand.freeze(split_1)

    print(split_1)
    print(split_2)
    print(frozen)
