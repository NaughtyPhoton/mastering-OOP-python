#!/usr/bin/env python3.7
"""
Suit model.
"""

from enum import Enum


class Suit(str, Enum):
    Club = "♣"
    Spade = "♠"
    Heart = "♥"
    Diamond = "♦"
