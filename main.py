#!/usr/bin/env python3.7
"""
Testing Suit and Card classes.
"""

from Suit import Suit
from Card import NumberCard, FaceCard, AceCard, Card


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


if __name__ == '__main__':
    cardFactory = CardFactory()
    cardFactory = [cardFactory.card(rank, suit) for rank in range(1, 14) for suit in Suit]
    print('')
