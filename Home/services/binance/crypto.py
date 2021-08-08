from Home.services.binance.bounce import Bounce


class Crypto:

    def __init__(self, crypto_symbol):
        self._symbol = crypto_symbol
        self.bounce = Bounce()
        self._current_price = None
        self.start_price = 1
        self.delta = 1
        self.balance = 0  # float(client.get_asset_balance(asset=crypto_name)['free'])
        self.fiat_balance = None
        self.acceptable_profit = 0.005
        self.binance_percent = 0.001



    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, text):
        if type(text) != str:
            raise ValueError("Value must be string")
        self._symbol = text

    @property
    def current_price(self):
        return self._current_price

    @current_price.setter
    def current_price(self, USD_price):
        self.delta = USD_price / self.start_price
        _trajectory = 0
        if (self.delta - 1) < - self.acceptable_profit:
            _trajectory = -1
        if (self.delta - 1) >  self.acceptable_profit:
            _trajectory = 1
        self.bounce.trajectory  = (self.delta - 1) < - self.acceptable_profit
        self._current_price = USD_price


    def update_bounce(self):
        pass
