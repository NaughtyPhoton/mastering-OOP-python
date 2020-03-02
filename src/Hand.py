#!/usr/bin/env python3.7
"""
Blackjack Hand class.
"""
from typing import Tuple

from Card import Card


class Hand:

    def __init__(self, dealer_card: Card, *cards: Card) -> None:
        self.dealer_card = dealer_card
        self.cards = cards

    @staticmethod
    def freeze(other) -> "Hand":
        hand = Hand(other.dealer_card, *other.cards)
        return hand

    @staticmethod
    def split(other, card0, card1) -> Tuple["Hand", "Hand"]:
        hand0 = Hand(other.dealer_card, other.cards[0], card0)
        hand1 = Hand(other.dealer_card, other.cards[1], card1)
        return hand0, hand1

    def __str__(self) -> str:
        return ", ".join(map(str, self.cards))

    def __repr__(self) -> str:
        cards_text = ', '.join(map(repr, self.cards))
        return f"{self.__class__.__name__} ({self.dealer_card!r}, {cards_text})"

    def __format__(self, format_spec) -> str:
        if not format_spec:
            return str(self)
        return ", ".join(f"{card:{format_spec}}" for card in self.cards)
