from abc import ABC, abstractmethod


class IMovable(ABC):

    @abstractmethod
    def move(self):
        raise NotImplementedError()
