from abc import ABC, abstractmethod

class Base_Parser(ABC):
    @abstractmethod
    def game_search(self, game_name):
        """Search game by its name from site and return GamePrice object"""
        pass
    
