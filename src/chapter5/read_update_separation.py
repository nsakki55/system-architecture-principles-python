from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict


class Amount:
    MAX: int = 100

    def __init__(self, value: int):
        self.value = value

    def __sub__(self, other):
        return self.value - other.value

    def has(self, amount: Amount) -> bool:
        return self.value + amount.value < self.MAX


class IBankAccountRepository(ABC):
    @abstractmethod
    def balance(self) -> Amount:
        pass

    @abstractmethod
    def withdraw(self, amount: Amount) -> bool:
        pass


class BankAccountRepositoryImpl(IBankAccountRepository):
    def __init__(self, amount: Amount):
        self.total_amount = amount

    def balance(self) -> Amount:
        return self.total_amount

    def withdraw(self, amount: Amount):
        self.total_amount - amount


class BankAccountService:
    def __init__(self, repository: IBankAccountRepository) -> None:
        self.repository = repository

    def balance(self) -> Amount:
        return self.repository.balance()

    def can_withdraw(self, amount: Amount) -> bool:
        balance: Amount = self.balance()
        return balance.has(amount)


class BankAccountUpdateService:
    def __init__(self, repository: IBankAccountRepository):
        self.repository = repository

    def withdraw(self, amount: Amount) -> None:
        self.repository.withdraw(amount)


class Model:
    def __init__(self) -> None:
        self.attribute: Dict[str, Any] = {}

    def add_attribute(self, name: str, attribute: Any):
        self.attribute[name] = attribute


class BankAccountController:
    query_service = BankAccountService(BankAccountRepositoryImpl(amount=Amount(50)))
    update_service = BankAccountUpdateService(BankAccountRepositoryImpl(amount=Amount(50)))

    def withdraw(self, amount: Amount, model: Model):
        if not self.query_service.can_withdraw(amount):
            return "insufficient funds page"
        self.update_service.withdraw(amount)
        balance: Amount = self.query_service.balance()
        model.add_attribute("balance", balance)
        return "withdrawal completed page"


class BankAccountScenario:
    query_service = BankAccountService(BankAccountRepositoryImpl(amount=Amount(50)))
    update_service = BankAccountUpdateService(BankAccountRepositoryImpl(amount=Amount(50)))

    def withdraw(self, amount: Amount):
        if not self.query_service.can_withdraw(amount):
            raise ValueError("insufficient funds")
        self.update_service.withdraw(amount)
        return self.query_service.balance()


if __name__ == "__main__":
    bank_account_service = BankAccountController()
    print(bank_account_service.withdraw(amount=Amount(10), model=Model()))
