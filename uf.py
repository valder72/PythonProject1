from abc import ABC, abstractmethod


class UF(ABC):

    @abstractmethod
    def union(self, p, q):
        pass

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    @abstractmethod
    def find(self, p):
        pass

    @abstractmethod
    def count(self):
        pass
