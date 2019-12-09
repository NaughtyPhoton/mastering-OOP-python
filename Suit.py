from enum import Enum
from typing import Tuple


class Card:

    def __init__(self, rank: str, suit: str) -> None:
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()

    def _points(self) -> Tuple[int, int]:
        return int(self.rank), int(self.rank)


class AceCard(Card):

    def _points(self) -> Tuple[int, int]:
        return 1, 11


class FaceCard(Card):

    def _points(self) -> Tuple[int, int]:
        return 10, 10


class Suit(str, Enum):
    Club = "♣"
    Spade = "♠"
    Heart = "♥"
    Diamond = "♦"


# def card(rank: int, suit: Suit) -> Card:
#     if rank == 1:
#         return AceCard("A", suit)
#     elif 2 <= rank < 11:
#         return Card(str(rank), suit)
#     elif rank == 11:
#         return FaceCard("J", suit)
#     elif rank == 12:
#         return FaceCard("Q", suit)
#     elif rank == 13:
#         return FaceCard("K", suit)
#     else:
#         raise Exception("Design Failure")


def card4(rank: int, suit: Suit) -> Card:
    class_ = {
        1: AceCard,
        11: FaceCard,
        12: FaceCard,
        13: FaceCard
    }.get(rank, Card)
    return class_(str(rank), suit)


if __name__ == '__main__':
    deck = [card4(rank, suit)
            for rank in range(1, 14)
            for suit in list(Suit)]
    print()
