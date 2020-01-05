#!/usr/bin/env python3.7
"""
Blackjack Hand class.
"""
from typing import List

from Card import Card


class Hand:
    """Hand with methods for playing Blackjack."""

    def __init__(self, dealer_card: Card, *cards: Card) -> None:
        self.dealer_card: Card = dealer_card
        self.cards = list(cards)

    def card_append(self, card: Card) -> None:
        self.cards.append(card)

    def hard_total(self) -> int:
        return sum(c.hard for c in self.cards)

    def soft_total(self) -> int:
        return sum(c.soft for c in self.cards)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} {self.dealer_card} {self.cards}"
