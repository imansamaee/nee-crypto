
from binance import BinanceSocketManager
from binance.client import Client

client = Client("ZHyp4Nfdygb9Gchz87POO9WGgEYm5Hh4VG7XmEBbqjF5VKbAVcQb4VWvThAT4HSi",
                "y5PVAA3CpETEVuHaTTDnBthAdrmOWRdqdMguFwkvvETkpijI8JVIdRHDK7sO5tv2")

bsm = BinanceSocketManager(client)
