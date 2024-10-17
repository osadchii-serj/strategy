from dataclasses import dataclass
from interface import IMovable


@dataclass
class Car:

    model: str
    movable_strategy: IMovable

    def set_strategy(self, movable_strategy: IMovable):
        self.movable_strategy = movable_strategy

    def move(self):
        self.movable_strategy.move()
