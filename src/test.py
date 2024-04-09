# Import required libraries
import asyncio
import json
import websockets

eth_node_ws_url = 'wss://eth-mainnet.g.alchemy.com/v2/c8VW6jhdLbvoyh3bEMkEfPEcSUzdezIO'

async def subscribe_to_blocks(ws_url):
    while True:
        try:
            async with websockets.connect(ws_url) as websocket:
                await websocket.send(json.dumps({
                    "id": 1,
                    "method": "eth_subscribe",
                    "params": [
                        "newHeads"
                    ],
                    "jsonrpc": "2.0"
                }))
                subscription_response = await websocket.recv()
                while True:
                    log = await websocket.recv()
                    log_data = json.loads(log)
                    number_hex = log_data['params']['result']['number']
                    number_decimal = int(number_hex, 16)


        except Exception as e:
            print(f'Error: {e}')
            print('Reconnecting...')
            await asyncio.sleep(5)

asyncio.run(subscribe_to_blocks(eth_node_ws_url))