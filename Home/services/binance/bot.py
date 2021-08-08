import asyncio
import os
from binance.enums import SIDE_SELL, ORDER_TYPE_MARKET
from Home.services.binance.auth import *
from Home.services.binance.crypto import Crypto
from Home.services.binance.trade import Trade


class TradeBot:
    def __init__(self):
        self.trade = Trade()
        self.init_crypto_list()
        self.current_symbol = "BTC"
        self.highest_delta = -1000000.0
        self.highest_crypto = None
        self.lowest_delta = 1000000.0
        self.lowest_crypto = None

        # self.current_deals = self.get_current_deals()
        # self.current_profitable_deals = None

    def init_crypto_list(self):
        self.crypto_list = []
        _price_list = self.trade.jason
        for price_dict in _price_list:
            if "USDT" in price_dict['symbol']:
                crypto_symbol = price_dict['symbol'].replace("USDT", "")
                if crypto_symbol in self.trade.ignore_symbols:
                    continue
                crypto = Crypto(crypto_symbol)
                crypto.current_price = float(price_dict['price'])
                crypto.start_price = float(price_dict['price'])
                self.crypto_list.append(crypto)
        return _price_list

    def get_crypto_by_symbol(self, symbol):
        return list(filter(lambda c: c.symbol == symbol, self.crypto_list))[0]

    def update_crypto(self):
        _price_list = self.trade.jason
        for crypto in self.crypto_list:
            symbol = crypto.symbol + "USDT"
            # print(symbol)
            try:
                _current_price = float(list(filter(lambda new_price: new_price['symbol']
                                                                     == symbol, _price_list))[0]['price'])
                crypto.current_price = _current_price
                crypto.delta = _current_price / crypto.start_price
                if crypto.delta > self.highest_delta:
                    self.highest_delta = crypto.delta
                    self.highest_crypto = crypto
                if crypto.delta < self.lowest_delta:
                    self.lowest_delta = crypto.delta
                    self.lowest_crypto = crypto

                if crypto.bounce.ready_to_trade:
                    self.trade_buy_nominee = crypto
                    self.ready_to_trade = True

                    print(crypto.symbol)
                # if crypto.drop:
                #     print(crypto.delta)
            except IndexError as e:
                pass
                # print(symbol)

    # def trade(self,trade_type , trade_symbol, quantity):
    #     client.create_order(
    #         symbol=trade_symbol,
    #         side=SIDE_BUY,
    #         type=ORDER_TYPE_MARKET,
    #         quantity=quantity,
    #     )

    # self.current_deals = self.get_current_deals()
    # self.current_profitable_deals = self.get_current_deals(1.01)

    # def get_current_deals(self, delta = 1.0):
    #     _current_deals = [p for p in self.price_list if self.current_symbol in p["symbol"] and p["delta"] > delta]
    #     _current_deals = sorted(_current_deals, key=lambda k: k['delta'], reverse=False)
    #     return _current_deals


def ETH_to_BTC():
    client.create_order(
        symbol="ETHBTC",
        side=SIDE_SELL,
        type=ORDER_TYPE_MARKET,
        quantity=0.002,
    )


async def update_prices(bot: TradeBot, sleet_time=1.0):
    while True:
        await asyncio.sleep(sleet_time)
        bot.update_crypto()
        # if bot.ready_to_trade:
        #     client.create_order(
        #         symbol=trade_symbol,
        #         side=SIDE_BUY,
        #         type=ORDER_TYPE_MARKET,
        #         quantity=quantity,

        clear_screen()
        # print(bot.highest_crypto.symbol + " => High Delta: " + str(bot.highest_crypto.delta))
        # print(bot.lowest_crypto.symbol + " => Low Delta: " + str(bot.lowest_crypto.delta))
        # print(bot.get_crypto_by_symbol("BTC").delta)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    bot = TradeBot()
    sleep_time = 1.0  # float(input ("Please inter time interval: "))
    print(bot.trade.sell_nominee.balance)
    asyncio.run(update_prices(bot, sleep_time))
