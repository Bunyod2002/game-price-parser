from abs import ABS, abstractmethod

class Base_Parser(ABS):
    @abstractmethod
    def game_search(self, game_name):
        """Search game by its name from site and return GamePrice object"""
        pass
    
