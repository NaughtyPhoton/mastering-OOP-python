#!/usr/bin/env python3.7
"""
GameStrategy is an object which is attached to an 'owner' to implement decisions.
"""
from Hand import Hand


class GameStrategy:
    """
    A pretty dumb strategy.
    """

    def insurance(self, hand: Hand) -> bool:
        return False

    def split(self, hand: Hand) -> bool:
        return False

    def double(self, hand: Hand) -> bool:
        return False

    def hit(self, hand: Hand) -> bool:
        return sum(c.hard for c in hand.cards) <= 17
