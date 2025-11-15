class Rule:
    def __init__(self):
        self._rules = {}

    def set_action(self, state: str, symbol: str, new_state: str, new_symbol: str, direction: str):
        self._rules[(state, symbol)] = (new_state, new_symbol, direction)

    def get_action(self, state: str, symbol: str):
        return self._rules.get((state, symbol), None)