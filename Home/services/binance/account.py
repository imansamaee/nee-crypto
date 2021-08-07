import asyncio

from Home.services.binance.crypto import Create_Crypto


class Account:
    def __init__(self):
        loop = get_or_create_event_loop()
        self.ETH = loop.run_until_complete(Create_Crypto('ETH'))
        self.BTC = loop.run_until_complete(Create_Crypto('BTC'))


def get_or_create_event_loop():
    try:
        return asyncio.get_event_loop()
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return asyncio.get_event_loop()


if __name__ == "__main__":
    account = Account()
    print(account.ETH.fiat_balance.AUD)
