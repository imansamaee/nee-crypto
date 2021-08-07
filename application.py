import asyncio
from threading import Lock

from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
from Home.services.binance.account import Account
from Home.services.binance.crypto import Crypto

async_mode = None

account = Account()
application = Flask(__name__)

application.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(application, async_mode=async_mode)
thread = None
thread_lock = Lock()


def background_thread():
    count = 0
    while True:
        socketio.sleep(2)
        count += 1
        socketio.emit('my_response',
                      {'data': account.BTC.current_price.AUD, 'count': count})



@application.route('/')
async def index():
    return render_template('index.html', async_mode=socketio.async_mode)


@socketio.on('message')
def handle_message(message):
    send(message, broadcast=True)


@socketio.event
def connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)
    emit('my_response', {'data': 'Connected. ETH balance: '+ str(account.ETH.fiat_balance.AUD), 'count': 0})
    emit('my_response', {'data': 'Connected. BTC balance: ' + str(account.BTC.fiat_balance.AUD), 'count': 0})
    emit('my_response', {'data': 'Connected. BTC price: ' + str(account.BTC.current_price.AUD), 'count': 0})

if __name__ == '__main__':
    socketio.run(application)
