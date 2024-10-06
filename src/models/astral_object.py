from abc import ABC, abstractmethod


class AstralObject(ABC):
    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column

    @abstractmethod
    def create(self, service):
        pass

    @abstractmethod
    def delete(self, service):
        pass
