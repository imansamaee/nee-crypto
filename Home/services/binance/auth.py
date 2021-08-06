import asyncio

import pandas as pd
from binance import BinanceSocketManager
from binance.client import Client

client = Client("79AePaTdo4tbBePmO4dr6lRt0vZnDICGwP70uSRPTJPNb05gigAuViLd7RxGNHO2",
                "lCwtPoeP16DU5877megsAd0qoMLZWqKRoe1cx0FbWn9SlsJ1X0nPsh496DWllFT4", testnet=True)



async def get_trade_socket(ts):
    bsm = BinanceSocketManager(client)
    s = bsm.trade_socket(ts)
    await s.__aenter__()
    msg = await s.recv()
    print(create_frame(msg))


def create_frame(msg):
    df = pd.DataFrame([msg])
    df = df.loc[:, ["s", "E", "p"]]
    df.columns = ["Symbol", "Time", "Price"]
    df.Price = df.Price.astype(float)
    df.Time = pd.to_datetime(df.Time, unit="ms")
    return df


if __name__ == "__main__":
    asyncio.run(get_trade_socket("BTCUSDT"))