class Agregattor:
    """Этот класс будет поочередно будет запускать все парсеры для конкретной игры"""
    def __init__(self, parsers):
        self.parsers = parsers # Список всех парсеров
        
    def get_prices(self, game_name):
        results = []
        for parser in self.parsers:
            result = parser.game_search(game_name)
            results.append(result)
        return results
    
    def sort_prices(self):
        pass