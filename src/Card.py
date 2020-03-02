#!/usr/bin/env python3.7
"""
Card model.
"""
import sys
from typing import cast

from Suit import Suit


class Card:
    insure = False

    def __init__(self, rank: str, suit: "Suit", hard: int, soft: int) -> None:
        self.rank = rank
        self.suit = suit
        self.hard = hard
        self.soft = soft

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(suit={self.suit!r}, rank={self.rank!r})"

    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"

    def __format__(self, format_spec) -> str:
        if not format_spec:
            return str(self)

        rs = format_spec.replace("%r", str(self.rank)).replace("%s", self.suit).replace("%%", "%")
        return rs

    def __eq__(self, other) -> bool:
        return (
                self.suit == cast(Card, other).suit
                and self.rank == cast(Card, other).rank
        )

    def __hash__(self) -> int:
        return (hash(self.suit) + 4 * hash(self.rank)) % sys.hash_info.modulus


class NumberCard(Card):

    def __init__(self, rank: int, suit: "Suit") -> None:
        super().__init__(str(rank), suit, rank, rank)


class AceCard(Card):
    insure = True

    def __init__(self, rank: int, suit: "Suit") -> None:
        super().__init__("A", suit, 1, 11)


class FaceCard(Card):

    def __init__(self, rank: int, suit: "Suit") -> None:
        rank_str = {11: "J", 12: "Q", 13: "K"}[rank]
        super().__init__(rank_str, suit, 10, 10)


if __name__ == '__main__':
    c1 = AceCard(1, Suit.Diamond)
    c2 = AceCard(1, Suit.Diamond)

    print(id(c1) // 16)
    print(id(c2) // 16)

    print(hash(c1))
    print(hash(c2))

    print(c1 == c2)
