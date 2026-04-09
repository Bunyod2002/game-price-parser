import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))#временный костыль для импорта из родительской папки
from base_parser import Base_Parser
from game_price import Game_Price
import requests as req
from bs4 import BeautifulSoup

class Kupikod_Parser(Base_Parser):
    def __init__(self, game_name):# при инициализации класса сразу выполняем поиск игры на сайте и сохраняем ее название и url для дальнейшего использования
        params = {"q": game_name}
        url = "https://search-v2.kupikod.com/search?"
        
        response = req.get(url, params=params)
        res = response.json()
        
        self.name_game = res['items'][0]['name']
        self.url = url
    
    def game_search(self, site_name=None, price=None, currency=None, type=None):
        return Game_Price(
            self.name_game,
            site_name,
            price,
            currency,
            type,
            self.url
        )

class GGsel_Parser(Base_Parser):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def get_ggsel_title(self, query):
        url = f"https://ggsel.net/catalog?search={query}"
        response = req.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title_element = soup.find('h3', class_='card-title') # название в карточке товара
        
        if not title_element:
            title_element = soup.find('div', class_='product-title')
        
        if not title_element:
            return query
        
        return title_element.text.strip()

    def game_search(self, game_name, site_name=None, price=None, currency=None, type=None, url=None):
        return self.get_ggsel_title(game_name)


# пример
if __name__ == "__main__":
    ggsel_parser = GGsel_Parser()
    
    raw_title = ggsel_parser.game_search("витчер")  # ← теперь используем game_search
    print(f"Найдено на GGsel: {raw_title}")# получаем название игры с GGsel
    
    kupikod_parser = Kupikod_Parser(raw_title)
    game_data = kupikod_parser.game_search(site_name="GGsel")
    
    print(f"Результат: {game_data}")