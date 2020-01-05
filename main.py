#!/usr/bin/env python3.7
"""
Testing Suit and Card classes.
"""
from Deck import Deck3 as Deck
from GameStrategy import GameStrategy
from Hand import Hand4 as Hand

if __name__ == '__main__':
    deck = Deck(5)
    hand = Hand(deck.pop(), deck.pop(), deck.pop())
    frozen_hand = Hand(hand)
    split_1 = Hand(hand, deck.pop(), split=0)
    split_2 = Hand(hand, deck.pop(), split=1)

    print(split_1)
    print(split_2)

    dumb = GameStrategy()

    print('c')
