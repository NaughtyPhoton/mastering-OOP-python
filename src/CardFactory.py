#!/usr/bin/env python3.7
"""
Deck Collection Class.
"""
from Card import AceCard, Card, FaceCard, NumberCard
from Suit import Suit


class CardFactory:

    def make_card(self, rank: int, suit: Suit) -> Card:
        if rank == 1:
            return AceCard(rank, suit)
        elif 2 <= int(rank) < 11:
            return NumberCard(rank, suit)
        elif 11 <= int(rank) < 14:
            return FaceCard(rank, suit)
        else:
            raise Exception("Rank out of range.")
