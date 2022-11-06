from enum import Enum, auto
from typing import Dict, Set


class State(Enum):
    EXAMINATION = auto()  # 審査中
    APPROVED = auto()  # 承認済
    GOING = auto()  # 実施中
    END = auto()  # 終了
    REMAND = auto()  # 差し戻し中
    TERMINATION = auto()  # 中断中


class StateTransitions:
    allowed: Dict[State, Set[State]] = {
        State.EXAMINATION: {State.APPROVED, State.REMAND},
        State.REMAND: {State.EXAMINATION, State.END},
        State.APPROVED: {State.GOING, State.END},
        State.GOING: {State.TERMINATION, State.END},
        State.TERMINATION: {State.GOING, State.END},
    }

    @classmethod
    def can_transit(cls, from_state: State, to_state: State) -> bool:
        allowed_state = cls.allowed.get(from_state)
        return to_state in allowed_state


if __name__ == "__main__":
    state = StateTransitions.can_transit(State.APPROVED, State.GOING)
    print(state)
