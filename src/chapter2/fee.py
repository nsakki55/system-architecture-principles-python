from dataclasses import dataclass


@dataclass(frozen=True)
class Yen(object):
    value: int

class Customer:
    child_fee: Yen = Yen(100)
    adult_fee: Yen = Yen(200)
    senior_fee: Yen = Yen(150)

    def __init__(self, customer_type: str):
        self.customer_type = customer_type

    def fee(self) -> Yen:
        if self._is_child():
            return self.child_fee
        if self._is_adult():
            return self.adult_fee
        if self._is_senior():
            return self.senior_fee

    def _is_child(self) -> bool:
        return self.customer_type == "child"

    def _is_adult(self) -> bool:
        return self.customer_type == "adult"

    def _is_senior(self) -> bool:
        return self.customer_type == "senior"


if __name__ == "__main__":
    customer = Customer(customer_type="adult")
    print(customer.fee())
