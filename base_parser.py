<<<<<<< HEAD
from abc import ABC, abstractmethod
=======
from abs import ABC, abstractmethod
>>>>>>> 438888eb6198002ea7fda2c3e54e4e0e02c3f483

class Base_Parser(ABC):
    @abstractmethod
    def game_search(self, game_name):
        """Search game by its name from site and return GamePrice object"""
        pass
    
