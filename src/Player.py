#!/usr/bin/env python3.7
"""
Blackjack Player class.
"""
from BettingStrategy import BettingStrategy
from GameStrategy import GameStrategy
from Table import Table


class Player():

    def __init__(
            self,
            table: Table,
            bet_strategy: BettingStrategy,
            game_strategy: GameStrategy,
            **extras,
    ) -> None:
        self.table = table
        self.bet_strategy = bet_strategy
        self.game_strategy = game_strategy
        self.log_name: str = extras.pop("log_name", self.__class__.__name__)
        if extras:
            raise TypeError(f"Extra arguments: {extras!r}")
