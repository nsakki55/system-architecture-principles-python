from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


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


class Reservation:
    def __init__(self, fees: List[Fee]):
        self.fees = fees

    def add_fee(self, fee: Fee) -> None:
        return self.fees.append(fee)

    @property
    def fee_total(self) -> Yen:
        total: Yen = Yen(0)
        for each in self.fees:
            total += each.yen
        return total


if __name__ == "__main__":
    fees = [AdultFee(), AdultFee(), ChildFee()]

    reservation = Reservation(fees)
    print(reservation.fee_total)

    reservation.add_fee(AdultFee())
    print(reservation.fee_total)
