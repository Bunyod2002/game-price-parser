import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from base_parser import Base_Parser
from game_price import Game_Price
import requests as req

class Kupikod_Parser(Base_Parser):
    def game_search(self,game_name, site_name=None, price=None, currency=None, type=None, url=None):               
        params = {
            "q": game_name
            }
        url = "https://search-v2.kupikod.com/search?"
        response = req.get(url, params=params)
        res = response.json()
        name_game = res['items'][0]['name']
        return Game_Price(name_game, site_name, price, currency, type, url)
        
print(Kupikod_Parser().game_search("The Witcher 3"))