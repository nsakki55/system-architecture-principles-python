from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Yen(object):
    value: int

    def __add__(self, other: Yen) -> Yen:
        return Yen(self.value + other.value)


class Fee(ABC):
    @property
    @abstractmethod
    def yen(self) -> Yen:
        pass

    @property
    @abstractmethod
    def label(self) -> str:
        pass


class AdultFee(Fee):
    _yen: Yen = Yen(100)
    _label: str = "adult"

    @property
    def yen(self) -> Yen:
        return self._yen

    @property
    def label(self):
        return self._label


class ChildFee(Fee):
    _yen: Yen = Yen(50)
    _label: str = "child"

    @property
    def yen(self) -> Yen:
        return self._yen

    @property
    def label(self):
        return self._label


class Charge:
    def __init__(self, fee: Fee):
        self.fee = fee

    @property
    def yen(self):
        return self.fee.yen


if __name__ == "__main__":
    adult = AdultFee()
    child = ChildFee()
    print(adult.yen)
    print(child.yen)

    charge = Charge(adult)
    print(charge.yen)
