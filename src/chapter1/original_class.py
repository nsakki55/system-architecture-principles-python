from __future__ import annotations


class Quantity:
    MIN: int = 1
    MAX: int = 100

    def __init__(self, value: int):
        if value < self.MIN:
            raise ValueError(f"Illegal: value is under {self.MIN}.")
        if value > self.MAX:
            raise ValueError(f"Illegal: value is over {self.MAX}.")

        self.value = value

    def can_add(self, other: Quantity) -> bool:
        added = self._add_value(other)
        return added <= self.MAX

    def add(self, other: Quantity) -> Quantity:
        if not self.can_add(other):
            raise ValueError(f"Illegal: total amount is over {self.MAX}.")
        added: int = self._add_value(other)
        return Quantity(added)

    def _add_value(self, other: Quantity) -> int:
        return self.value + other.value


if __name__ == "__main__":
    quality = Quantity(10)
    added_quality = quality.add(Quantity(20))
    print(added_quality.value)
