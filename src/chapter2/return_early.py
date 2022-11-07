from dataclasses import dataclass


@dataclass(frozen=True)
class Yen(object):
    value: float


class Customer:
    base_fee: Yen = Yen(100)

    def __init__(self, customer_type: str):
        self.customer_type = customer_type

    def fee(self) -> Yen:
        if self._is_child():
            return self._child_fee
        if self._is_senior():
            return self._senior_fee

        return self.base_fee

    @property
    def _child_fee(self) -> Yen:
        return Yen(self.base_fee.value * 0.5)

    @property
    def _senior_fee(self) -> Yen:
        return Yen(self.base_fee.value * 0.8)

    def _is_child(self) -> bool:
        return self.customer_type == "child"

    def _is_adult(self) -> bool:
        return self.customer_type == "adult"

    def _is_senior(self) -> bool:
        return self.customer_type == "senior"


if __name__ == "__main__":
    customer = Customer(customer_type="adult")
    print(customer.fee())
