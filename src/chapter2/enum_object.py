from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


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


class SeniorFee(Fee):
    _yen: Yen = Yen(80)
    _label: str = "senior"

    @property
    def yen(self) -> Yen:
        return self._yen

    @property
    def label(self):
        return self._label


class FeeType(Enum):
    adult = AdultFee()
    child = ChildFee()
    senior = SeniorFee()

    @property
    def yen(self) -> Yen:
        return self.value.yen

    @property
    def label(self) -> str:
        return self.value.label


def fee_for(fee_type_name: str) -> Yen:
    return FeeType[fee_type_name].yen


if __name__ == "__main__":
    fee_adult = fee_for("adult")
    fee_child = fee_for("child")
    fee_senior = fee_for("senior")

    print(fee_senior)
    print(fee_adult)
    print(fee_child)
