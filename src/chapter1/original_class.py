from __future__ import annotations


class Quantity:
    min: int = 1
    max: int = 100

    def __init__(self, value: int):
        if value < self.min:
            raise ValueError(f"Illegal: value is under {self.min}.")
        if value > self.max:
            raise ValueError(f"Illegal: value is over {self.max}.")

        self.value = value

    def can_add(self, other: Quantity) -> bool:
        added = self._add_value(other)
        return added <= self.max

    def add(self, other: Quantity) -> Quantity:
        if not self.can_add(other):
            raise ValueError(f"Illegal: total amount is over {self.max}.")
        added: int = self._add_value(other)
        return Quantity(added)

    def _add_value(self, other: Quantity) -> int:
        return self.value + other.value


if __name__ == "__main__":
    quality = Quantity(10)
    added_quality = quality.add(Quantity(20))
    print(added_quality.value)
