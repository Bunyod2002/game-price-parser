import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # временный костыль для импорта из родительской папки
from base_parser import Base_Parser
from game_price import Game_Price
from selenium import webdriver #запускаем браузер
from selenium.webdriver.common.by import By #способы поиска элементов
from selenium.webdriver.support.ui import WebDriverWait #для ожидания прогрузки элементов
from selenium.webdriver.support import expected_conditions as EC #при быстрой загрузки элемента позволяет сразу же взаимодействовать с ним несмотря на то что еще есть время ожидения
from bs4 import BeautifulSoup  # после получение html будем его парсить через beautifulsoup

class Ggsel_Parser(Base_Parser):

    def driver_settings(self):
        options = webdriver.ChromeOptions()#настройки под открытие
        options.add_argument('--headless') #открытие по дефолту в фоновом режиме 
            #доп настройки чтоб казалось что мы человек
        options.add_argument('--disable-blink-features=AutomationControlled')  
        options.add_experimental_option("excludeSwitches", ["enable-automation"])  
        options.add_experimental_option('useAutomationExtension', False)

        driver = webdriver.Chrome(options=options)#запуск браузера

        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") #ласт стадия проверки на работа в js сайта

        return driver
        
    def game_search(self, game_name):
            self.driver = self.driver_settings()
            url = f'https://ggsel.net/search?q={game_name}'
            self.driver.get(url)
            
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'product-card')))#ждем загрузки карточек ттоваров она макс 10 сек
         
            html = self.driver.page_source
            soup = BeautifulSoup(html, 'lxml')#получили html и передали в beautifulsoup
            product_cards = soup.find_all('div', class_='product-card')#(мне лень счас искать но короч потом название класса нужно где тру инфа храниться) сохраняю все карточки товаров в переменную items 
            if not product_cards:
               return None#потом мб прописать как исключенье
            
            goods=[]#создаем список товаров
            for product_card in product_cards:

                title_elem = product_card.find('div', class_='product-title')#парсим данные через bs надо будет потом на тру класс заменить
                title = title_elem.text.strip()#убираем лишние пробелы из названия

                price_elem = product_card.find('div', class_='product-price')
                price_text = price_elem.text.strip()

                link_elem = product_card.find('a', href=True)
                link = link_elem['href']
                if link and not link.startswith('http'):
                   link = f"https://ggsel.net{link}"
            goods.append({"game_name": title,"price": price_text,"url": link})
            goods.sort(key=lambda x: x["price"]) #сортируем по цене
            top_goods = goods[:3]#берем первые три
            result = []
            for item in top_goods:
                result.append(Game_Price(
                game_name=item["game_name"],
                site_name="ggsel.net",
                price=item["price"],
                url=item["url"]
                ))
            return result
    def close(self):
        if self.driver:
            self.driver.quit()#закрываем браузер
''''''
