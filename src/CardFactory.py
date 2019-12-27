#!/usr/bin/env python3.7
"""
Deck Collection Class.
"""
from Card import AceCard, Card, NumberCard, FaceCard
from Suit import Suit


class CardFactory:

    def makeCard(self, rank: int, suit: Suit) -> Card:
        if rank == 1:
            return AceCard(rank, suit)
        elif 2 <= rank < 11:
            return NumberCard(rank, suit)
        elif 11 <= rank < 14:
            return FaceCard(rank, suit)
        else:
            raise Exception("Rank out of range.")
