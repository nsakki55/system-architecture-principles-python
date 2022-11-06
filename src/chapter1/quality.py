"""値の範囲を制限してプログラムをわかりやすく安全にする"""
from __future__ import annotations



class Quality:
    def __init__(self, value: int):
        self.min: int = 1
        self.max: int = 100

        if value < self.min:
            raise ValueError(f"Illegal: value is under {self.min}.")
        if value < self.max:
            raise ValueError(f"Illegal: value is over {self.max}.")

        self.value = value

    def can_add(self, other: Quality) -> bool:
        added = self._add_value(other)
        return added <= self.max

    def add(self, other: Quality) -> Quality:
        if not self.can_add(other):
            raise ValueError(f"Illegal: total amount is over {self.max}.")
        added: int = self._add_value(other)
        return Quality(added)

    def _add_value(self, other: Quality) -> int:
        return self.value + other.value
