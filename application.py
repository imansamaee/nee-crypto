#import asyncio

from flask import Flask

#from Home.services.binance.auth import get_trade_socket

application = Flask(__name__)


@application.route('/')
def index():  # put application's code here
    return "hi"#asyncio.run(get_trade_socket("BTCUSDT"))
@application.route('/hello')
def hello():
    return 'Hello, World'

if __name__ == '__main__':
    application.run(debug=True)
