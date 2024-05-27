# from binance import ThreadedWebsocketManager
# twm = ThreadedWebsocketManager()
# twm.start()
#
#
# def handle_socket_message(msg):
#     c = msg['k']['c']
#     print(c)
#
#
# twm.start_kline_socket(callback=handle_socket_message, symbol='AAVEUSDT')
# twm.join()
import ccxt
from pprint import pprint
import datetime

print('CCXT Version:', ccxt.__version__)

exchange = ccxt.binance()
timestamp = 1716818528
# 1602730800000
response = exchange.fetch_ohlcv('AAVE/USDT', '1m', timestamp * 1000, 1)
pprint(response[0][4])
