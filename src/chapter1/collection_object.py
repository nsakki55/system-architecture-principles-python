from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass(frozen=True)
class Customer:
    id: int


@dataclass(frozen=True)
class Customers:
    customers: List[Customer]

    def add(self, customer: Customer) -> Customers:
        return Customers(self.customers.append(customer))

    def as_list(self) -> Tuple[Customer]:
        return tuple(self.customers)


if __name__ == "__main__":
    customers_list = [Customer(1), Customer(2), Customer(3), Customer(4)]
    customers_class = Customers(customers_list)

    print(customers_class.as_list())
