import requests as req
from bs4 import BeautifulSoup
from base_parser import Base_Parser

class Steam_Parser(Base_Parser):
    def game_search(self, game_name):
        pass
    
    def get_appid(self, game_name):
        url = f"https://store.steampowered.com/search/?term={game_name}" # Это url для поиска игр по имени, он возвращает страницу с результатами поиска, где можно найти appid игры
        response = req.get(url) # Получаем HTML-код страницы
        soup = BeautifulSoup(response.text, 'html.parser') # Парсим HTML-код с помощью BeautifulSoup
        search_results = soup.select("a.search_result_row")
        for result in search_results: # Проходим по всем результатам поиска
            title = result.select_one('span', class_='title').text.strip() # Получаем название игры
            if title.lower() == game_name.lower(): # Если название игры совпадает с искомым, то возвращаем appid
                appid = result['data-ds-appid'] # Получаем appid из атрибута data-ds-appid
                return appid
            
