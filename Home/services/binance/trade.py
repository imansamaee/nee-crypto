import json

import requests

from Home.services.binance.auth import client
from Home.services.binance.crypto import Crypto


class Trade:
    def __init__(self):
        self.ignore_symbols = ['BKRW']
        self.is_trade_authorized = False
        self.ready_to_trade = False
        self.buy_nominee = None
        self.trade_symbols = self.init_trade_symbols()

    def init_trade_symbols(self):
        trade_symbols = []
        for trade_dict in self.jason:
            trade_symbol = trade_dict['symbol']
            if trade_symbol not in trade_symbols and trade_symbol not in self.ignore_symbols:
                trade_symbols.append(trade_symbol)
        return trade_symbols

    @property
    def sell_nominee(self):
        with open('data/sell_history.txt', 'r') as f:
            lines = f.read().splitlines()
            symbol = lines[-1]
            crypto = Crypto(symbol)
            crypto.balance = client.get_asset_balance(asset=symbol)["free"]
        return crypto

    @property
    def jason(self):
        url = "https://api.binance.com/api/v3/ticker/price"
        response = requests.get(url)
        return json.loads(response.text)

    def get_trade_symbol(self, symbol1, symbol2):
        for trade_symbol in self.trade_symbols:
            if symbol1 in trade_symbol and symbol2 in trade_symbol and len(trade_symbol) == (
                    len(symbol1) + len(symbol2)):
                return trade_symbol
        return None
