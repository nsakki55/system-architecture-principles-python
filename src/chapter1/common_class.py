class ShippingCost:
    minimum_for_free: int = 3000
    cost: int = 500

    def __init__(self, base_price: int):
        self.base_price = base_price

    @property
    def amount(self) -> int:
        if self.base_price < self.minimum_for_free:
            return self.cost

        return 0


def shipping_cost(base_price: int) -> int:
    cost = ShippingCost(base_price)
    return cost.amount


if __name__ == "__main__":
    print(shipping_cost((200)))
