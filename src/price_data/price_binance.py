from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

twm = ThreadedWebsocketManager()
twm.start()


def handle_socket_message(msg):
    o = msg['k']['o']
    h = msg['k']['h']
    l = msg['k']['l']
    c = msg['k']['c']
    v = msg['k']['v']
    print(o, h, l, c, v)


twm.start_kline_socket(callback=handle_socket_message, symbol='SHIBUSDT')

twm.join()
