#!/usr/bin/env python3.7
from Deck import Deck
from Hand import Hand


class Table:
    """
    Table class handles dealing Hands, receiving bets, offering splits, resolves each hand, and pays off the bets.
    """

    def __init__(self) -> None:
        self.deck = Deck()

    def place_bet(self, amount: int) -> None:
        print("Bet", amount)

    def get_hand(self) -> Hand:
        try:
            self.hand = Hand(self.deck.pop(), self.deck.pop(), self.deck.pop())
            self.hole_card = self.deck.pop()
        except IndexError:
            # Out of cards: need to shuffle and try again
            self.deck = Deck()
            return self.get_hand()

    def can_insure(self, hand: Hand) -> bool:
        return hand.dealer_card.insure
