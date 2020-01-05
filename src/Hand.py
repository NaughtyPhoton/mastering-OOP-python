#!/usr/bin/env python3.7
"""
Blackjack Hand class.
"""
from typing import List, Union, Optional, cast, overload

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


class Hand4:
    """
    Uses a complex __init__() method with multiple strategies for initialization.
    """

    @overload
    def __init__(self, arg1: "Hand4") -> None:
        ...

    @overload
    def __init__(self, arg1: "Hand4", arg2: Card, *, split: int) -> None:
        ...

    @overload
    def __init__(self, arg1: Card, arg2: Card, arg3: Card) -> None:
        ...

    def __init__(
            self,
            arg1: Union["Hand4", Card],
            arg2: Optional[Card] = None,
            arg3: Optional[Card] = None,
            split: Optional[int] = None,
    ) -> None:
        self.dealer_card: Card
        self.cards: List[Card]

        if isinstance(arg1, Hand4):
            # Clone an existing hand
            self.dealer_card = arg1.dealer_card
            self.cards = arg1.cards

        elif isinstance(arg1, Hand4) and isinstance(arg2, Card) and split is not None:
            # Split an existing hand
            self.dealer_card = arg1.dealer_card
            self.cards = [arg1.cards[split], arg2]

        elif isinstance(arg1, Card) and isinstance(arg2, Card) and isinstance(arg3, Card):
            # Build a fresh, new hand from three cards
            self.dealer_card = arg1
            self.cards = [arg2, arg3]

        else:
            raise TypeError("Invalid constructor {arg1!r} {arg2!r} {arg3!r}")

    def __str__(self) -> str:
        return ", ".join(map(str, self.cards))

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.dealer_card!r}, *{self.cards})"
