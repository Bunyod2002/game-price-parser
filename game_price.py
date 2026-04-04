class Game_Price:
    def __init__(self, game_name, site_name, price, currency, type, url):
        self.game_name = game_name
        self.site_name = site_name
        self.price = price
        self.currency = currency # валюта
        self.type = type # здесь указан какой тип продукта (гифт, аренда аккаунта и тд)
        self.url = url # ссылка на кокнретную игру на сайте
        
    def to_dict(self):
        return {
            "game": self.game_name,
            "site": self.site_name,
            "price": self.price,
            "currency": self.currency,
            "type": self.type,
            "url": self.url
        }
