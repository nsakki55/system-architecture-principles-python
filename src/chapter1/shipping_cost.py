"""異なるクラスの重複したコードをなくす"""
class ShippingCost:
    def __init__(self, base_price: int):
        self.minimum_for_free: int = 3000
        self.cost: int = 500
        self.base_price = base_price

    @property
    def amount(self) -> int:
        if self.base_price < self.minimum_for_free:
            return self.cost

        return 0


def shipping_cost(base_price: int) -> int:
    cost = ShippingCost(base_price)
    return cost.amount
