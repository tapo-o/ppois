from turing.Tape import Tape
from turing.Rule import Rule

class Turing:
    def __init__(self, tape: Tape, rules: Rule, start_state: str):
        self._tape = tape
        self._rules = rules
        self._state = start_state

    def step(self) -> bool:
        symbol = self._tape.read_symbol()
        action = self._rules.get_action(self._state, symbol)

        if action is None:
            return False
        
        new_state, new_symbol, direction = action
        self._tape.write_symbol(new_symbol)
        self._tape.move(direction)
        self._state = new_state
        return True
