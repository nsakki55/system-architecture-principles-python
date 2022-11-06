from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Quantity:
    value: int
    discount: int

    @property
    def is_discountable(self) -> bool:
        return True


@dataclass(frozen=True)
class Money:
    value: int

    def multiple(self, multiple_value: int) -> Money:
        return Money(self.value * multiple_value)


def amount(unit_price: Money, quantity: Quantity):
    if quantity.is_discountable:
        discount(unit_price, quantity)

    return unit_price.multiple(quantity.value)


def discount(unit_price: Money, quantity: Quantity) -> Money:
    discount_value = unit_price.value - quantity.discount
    return Money(discount_value)


if __name__ == "__main__":
    money = Money(100)
    quantity = Quantity(20, 10)
    amount_money = amount(unit_price=money, quantity=quantity)
    print(amount_money.value)
