#!/usr/bin/env python3.7

import abc
from abc import abstractmethod


class BettingStrategy(metaclass=abc.ABCMeta):
    """
    Superclass for BettingStrategy family of classes.
    bet() method must be implemented.
    """

    @abstractmethod
    def bet(self) -> int:
        raise NotImplementedError("No bet method")

    def record_win(self) -> None:
        pass

    def record_loss(self) -> None:
        pass


class Flat(BettingStrategy):
    """
    Test class that always bets.
    """

    def bet(self) -> int:
        return 1
