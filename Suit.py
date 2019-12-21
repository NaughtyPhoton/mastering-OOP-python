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


# def card4(rank: int, suit: Suit) -> Card:
#     class_ = {
#         1: AceCard,
#         11: FaceCard,
#         12: FaceCard,
#         13: FaceCard
#     }.get(rank, Card)
#     return class_(str(rank), suit)

def card7(rank: int, suit: Suit) -> Card:
    class_rank = {
        1: lambda suit: AceCard("A", suit),
        11: lambda suit: FaceCard("J", suit),
        12: lambda suit: FaceCard("Q", suit),
        13: lambda suit: FaceCard("K", suit),
    }.get(rank, lambda suit: Card(str(rank), suit))
    return class_rank(suit)


class CardFactory:

    def rank(self, rank: str) -> "CardFactory":
        self.class_, self.rank_str = {
            1: (AceCard, "A"),
            11: (FaceCard, "J"),
            12: (FaceCard, "Q"),
            13: (FaceCard, "K")
        }.get(rank, (Card, str(rank)))
        return self

    def suit(self, suit: Suit) -> Card:
        return self.class_(self.rank_str, suit)


if __name__ == '__main__':
    deck = [card7(rank, suit)
            for rank in range(1, 14)
            for suit in list(Suit)]

    cardFactory = CardFactory()
    cardFactory = [cardFactory.rank(r + 1).suit(s) for r in range(13) for s in Suit]
    print()
