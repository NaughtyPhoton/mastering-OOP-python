#!/usr/bin/env python3.7
"""
Deck Collection Class.
"""
import random

from Card import Card
from CardFactory import CardFactory
from Suit import Suit


class Deck:
    def __init__(self) -> None:
        self._cardFactory = CardFactory()
        self._cards = [self._cardFactory.makeCard(r + 1, s) for r in range(13) for s in iter(Suit)]
        random.shuffle(self._cards)

    def pop(self) -> Card:
        return self._cards.pop()
