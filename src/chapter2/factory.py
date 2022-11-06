from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict


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


class FeeFactory:
    types: Dict[str, Fee] = {"adult": AdultFee(), "child": ChildFee()}

    @classmethod
    def fee_by_name(cls, name: str) -> Fee:
        return cls.types.get(name)


if __name__ == "__main__":
    fee_adult = FeeFactory.fee_by_name("adult")
    print(fee_adult.yen)
    fee_child = FeeFactory.fee_by_name("child")
    print(fee_child.yen)
