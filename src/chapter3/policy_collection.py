from abc import ABC
from dataclasses import dataclass
from typing import Set


@dataclass(frozen=True)
class Value:
    number: int


@dataclass(frozen=True)
class Rule(ABC):
    def ok(self, value: Value) -> bool:
        pass

    def ng(self, value: Value) -> bool:
        pass


@dataclass(frozen=True)
class PositiveNumberRule(Rule):
    def ok(self, value: Value) -> bool:
        return value.number % 2 == 0

    def ng(self, value: Value) -> bool:
        return value.number % 2 == 1


class Policy:
    def __init__(self):
        self.rules: Set[Rule] = set()

    def comply_with_all(self, value: Value) -> bool:
        for each in self.rules:
            if each.ng(value):
                return False
        return True

    def comply_with_some(self, value: Value) -> bool:
        for each in self.rules:
            if each.ok(value):
                return True

    def add_rule(self, rule: Rule) -> None:
        self.rules.add(rule)


if __name__ == "__main__":
    policy = Policy()
    policy.add_rule(PositiveNumberRule())
    print(policy.comply_with_some(Value(4)))
