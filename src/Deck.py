#!/usr/bin/env python3.7
"""
Deck Collection Class.
"""
import random

from CardFactory import CardFactory
from Suit import Suit


# class Deck:
#     """
#     Deck implementation which wraps a list class.
#     """
#
#     def __init__(self) -> None:
#         self._cardFactory = CardFactory()
#         self._cards = [self._cardFactory.makeCard(r + 1, s) for r in range(13) for s in iter(Suit)]
#         random.shuffle(self._cards)
#
#     def pop(self) -> Card:
#         return self._cards.pop()
#
#
# class Deck2(list):
#     """
#     Deck implementation which extends the list class.
#     This example has the disadvantage that it exposes all the method's of list class.
#     """
#
#     def __init__(self) -> None:
#         self._cardFactory = CardFactory()
#         super().__init__(self._cardFactory.makeCard(r + 1, s) for r in range(1, 13) for s in iter(Suit))
#         random.shuffle(self)


class Deck3(list):
    """
    Deck implementation which extends the list class and contains multiple sets of 52 card decks.
    Still has the disadvantage that it exposes all the method's of list class.
    """

    def __init__(self, decks: int = 1) -> None:
        super().__init__()
        self._cardFactory = CardFactory()
        for _ in range(decks):
            self.extend(self._cardFactory.make_card(r + 1, s) for r in range(13) for s in iter(Suit))
        random.shuffle(self)
        burn = random.randint(1, 52)
        for _ in range(burn):
            self.pop()
