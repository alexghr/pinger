# This is a state management store similar to a Redux store

class Store:
    def __init__(self):
        self._state = State()

    def state(self):
        return self._state
    
    def update(self, ping_response: bool):
        if ping_response:
            self._state.count_recent_fail = 0 # reset current failures
            self._state.count_ok += 1
        else:
            self._state.count_recent_fail += 1
            self._state.count_fail += 1

class State:
    def __init__(self):
        self.count_ok = 0
        self.count_fail = 0
        self.count_recent_fail = 0
    
    def total_pings(self):
        return self.count_fail + self.count_ok