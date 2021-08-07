from Home.services.binance.auth import *
from Home.services.binance.currency import Currency


class Crypto:

    def __init__(self, crypto_name):
        self._crypto_name = crypto_name
        self._current_price = None
        self.trade_socket = bsm.trade_socket(crypto_name + "USDT")
        self.balance = float(client.get_asset_balance(asset=crypto_name)['free'])
        self.fiat_balance = None

    @property
    def crypto_name(self):
        return self._crypto_name

    @crypto_name.setter
    def crypto_name(self, text):
        if type(text) != str:
            raise ValueError("Value must be string")
        self._crypto_name = text

    @property
    def current_price(self):
        return Currency(self._current_price)

    @current_price.setter
    def current_price(self, price):
        self.fiat_balance = Currency(self.balance * price)
        self._current_price = price

    @classmethod
    async def create(cls, crypto_name):
        self = Crypto(crypto_name)
        await self.trade_socket.__aenter__()
        msg_dict = await self.trade_socket.recv()
        self.current_price = float(msg_dict['p'])
        return self


async def Create_Crypto(crypto_name):
    crypto = await Crypto.create(crypto_name)
    return crypto

#
