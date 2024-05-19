from strategy import *
from state import *


class Package:
    def __new__(cls, weight, strategy=Standard(), state=Transit()):
        it = cls.__dict__.get("__it__")
        if it is not None:
            return it
        cls.__it__ = it = object.__new__(cls)
        it.__init__(weight, strategy, state)
        return it

    def __init__(self, weight, strategy=Standard(), state=Transit()):
        self.weight = weight
        self.strategy = strategy
        self.state = state

    def update_strategy(self, new_strategy):
        if not isinstance(new_strategy, Strategy):
            raise 'Not a strategy'
        self.strategy = new_strategy
        self.get_cost()

    def update_state(self, new_state):
        if not isinstance(new_state, State):
            raise 'Not a state'
        self.state = new_state
        self.state.handle()

    def get_cost(self):
        return self.strategy.get_cost(self.weight)

    def has_been_delivered(self):
        return isinstance(self.state, Delivered)
