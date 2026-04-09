from abc import ABC, abstractmethod

class Base_Parser(ABC):
    @abstractmethod
    def game_search(self, game_name, site_name=None, price=None, currency=None, type=None, url=None):
        pass
