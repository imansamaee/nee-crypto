from Home.services.binance.auth import *
from binance.enums import *


def BTC_to_EHT():
    order = client.create_order(
        symbol="ETHBTC",
        side = SIDE_BUY,
        type = ORDER_TYPE_MARKET,
        quantity = 0.005,
    )
def ETH_to_BTC():
    order = client.create_order(
        symbol="ETHBTC",
        side = SIDE_SELL,
        type = ORDER_TYPE_MARKET,
        quantity = 0.005,
    )
if __name__ == "__main__":
    info = client.get_symbol_info("ETHBTC")
    print(info)
    BTC_to_EHT()