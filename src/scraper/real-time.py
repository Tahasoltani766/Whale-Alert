import time
import pandas as pd
import numpy as np
from web3 import Web3
import asyncio
import json
import websockets

# rpc_url = 'https://mainnet.infura.io/v3/8cb9d441420b4009afa02ce71849560e'
rpc_url = 'https://eth-mainnet.g.alchemy.com/v2/kurV79OJ-CdKRuj6nc0Ua-JYhXGVdjcA'
w3 = Web3(Web3.HTTPProvider(rpc_url))
adr_token = w3.to_checksum_address("0xdAC17F958D2ee523a2206206994597C13D831ec7")
abi_token = """[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,
"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_upgradedAddress",
"type":"address"}],"name":"deprecate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},
{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],
"name":"approve","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,
"inputs":[],"name":"deprecated","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view",
"type":"function"},{"constant":false,"inputs":[{"name":"_evilUser","type":"address"}],"name":"addBlackList",
"outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],
"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view",
"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},
{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,
"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"upgradedAddress","outputs":[{
"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{
"name":"","type":"address"}],"name":"balances","outputs":[{"name":"","type":"uint256"}],"payable":false,
"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"",
"type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],
"name":"maximumFee","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view",
"type":"function"},{"constant":true,"inputs":[],"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],
"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"unpause",
"outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{
"name":"_maker","type":"address"}],"name":"getBlackListStatus","outputs":[{"name":"","type":"bool"}],"payable":false,
"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"",
"type":"address"}],"name":"allowed","outputs":[{"name":"","type":"uint256"}],"payable":false,
"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"",
"type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"who",
"type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,
"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[],
"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getOwner",
"outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,
"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"",
"type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{
"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,
"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"newBasisPoints",
"type":"uint256"},{"name":"newMaxFee","type":"uint256"}],"name":"setParams","outputs":[],"payable":false,
"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],
"name":"issue","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,
"inputs":[{"name":"amount","type":"uint256"}],"name":"redeem","outputs":[],"payable":false,
"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},
{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],
"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"basisPointsRate",
"outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},
{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"isBlackListed","outputs":[{"name":"",
"type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{
"name":"_clearedUser","type":"address"}],"name":"removeBlackList","outputs":[],"payable":false,
"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"MAX_UINT","outputs":[{
"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,
"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,
"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_blackListedUser",
"type":"address"}],"name":"destroyBlackFunds","outputs":[],"payable":false,"stateMutability":"nonpayable",
"type":"function"},{"inputs":[{"name":"_initialSupply","type":"uint256"},{"name":"_name","type":"string"},
{"name":"_symbol","type":"string"},{"name":"_decimals","type":"uint256"}],"payable":false,
"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"amount",
"type":"uint256"}],"name":"Issue","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"amount",
"type":"uint256"}],"name":"Redeem","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"newAddress",
"type":"address"}],"name":"Deprecate","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,
"name":"feeBasisPoints","type":"uint256"},{"indexed":false,"name":"maxFee","type":"uint256"}],"name":"Params",
"type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_blackListedUser","type":"address"},
{"indexed":false,"name":"_balance","type":"uint256"}],"name":"DestroyedBlackFunds","type":"event"},
{"anonymous":false,"inputs":[{"indexed":false,"name":"_user","type":"address"}],"name":"AddedBlackList",
"type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_user","type":"address"}],
"name":"RemovedBlackList","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner",
"type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value",
"type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from",
"type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],
"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,
"inputs":[],"name":"Unpause","type":"event"}]"""

eth_node_ws_url = 'wss://eth-mainnet.g.alchemy.com/v2/c8VW6jhdLbvoyh3bEMkEfPEcSUzdezIO'


class dataFrame:
    def __init__(self):
        dt = {}
        index = []
        self.df = pd.DataFrame(dt, index=index)
        self.table = np.empty((0, 4), dtype=object)
        self.to = self.table[:, 0]
        self.values = self.table[:, 1]
        self.from_ = self.table[:, 2]
        self.token = self.table[:, 3]
        self.dataframe = pd.DataFrame()

    def handler_data(self, trx, number_trx):
        if not self.table.size:
            _to = (trx.args.to)
            _from = (trx.args['from'])
            _value = (trx.args.value)
            _token = (trx.address)
            new_row = np.array([_to, _value, _from, _token])
            self.table = np.vstack([self.table, new_row])
        else:
            _to = (trx.args.to)
            _from = (trx.args['from'])
            _value = (trx.args.value)
            _token = (trx.address)
            new_row = np.array([_to, _value, _from, _token])
            self.table = np.vstack([self.table, new_row[None, :]])
            if len(self.table) == number_trx:
                self.addr_to_checker()
                self.addr_from_checker()
                self.table = np.empty((0, 4), dtype=object)

    def similar_checker(self, addr):
        unique_addresses, counts = np.unique(addr, return_counts=True)
        similar_addresses = unique_addresses[counts > 1]
        indices_to_remove = np.where(np.isin(addr, similar_addresses))
        different_addresses = np.delete(addr, indices_to_remove)
        return similar_addresses, different_addresses

    def addr_handler(self, from_addr=False):
        list_increase = []
        _values = self.table[:, 1]
        _token = self.table[:, 3]

        addr_check = self.table[:, 0]
        multiplier = 1
        if from_addr:
            addr_check = self.table[:, 2]
            multiplier = -1
        similar_addresses, different_addresses = self.similar_checker(addr_check)

        for addr in different_addresses:
            tr = np.where(addr_check == addr)
            val = int(_values[tr][0])
            tok = _token[tr][0]
            decrease_different = [addr, multiplier * val, tok]
            list_increase.append(decrease_different)
        if len(similar_addresses) > 0:
            for address in similar_addresses:
                indices = np.where(addr_check == address)[0]
                val = _values[indices]
                tk = _token[indices][0]
                result_val = sum(map(int, val))
                addr_from = addr_check[indices][0]
                similar_decrease = [addr_from, multiplier * result_val, tk]
                list_increase.append(similar_decrease)
        self.generator_dataframe(list_increase)

    def addr_to_checker(self):
        self.addr_handler(False)

    def addr_from_checker(self):
        self.addr_handler(True)

    def generator_dataframe(self, list_dt):
        for i in list_dt:
            address = f'{i[0]}'
            value = i[1]
            category = f'{i[2]}'
            if address in self.dataframe.index:
                self.dataframe.at[address, category] = self.dataframe.at[address, category] + value
            else:
                data = {category: [value]}
                new_df = pd.DataFrame(data, index=[address])
                self.dataframe = pd.concat([self.dataframe, new_df])
        self.dataframe.to_excel('MarksData.xlsx')
        print('END')


d = dataFrame()

def trx_transfer(blc_num: int):
    weth_contract = w3.eth.contract(address=adr_token, abi=abi_token)
    logs = weth_contract.events.Transfer().get_logs(fromBlock=blc_num, toBlock='latest')
    number_trx = len(logs)
    print(number_trx)
    for trx in logs:
        d.handler_data(trx, number_trx)


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
                await websocket.recv()
                while True:
                    log = await websocket.recv()
                    log_data = json.loads(log)
                    number_hex = log_data['params']['result']['number']
                    number_decimal = int(number_hex, 16)
                    trx_transfer(number_decimal)

        except Exception as e:
            print(f'Error: {e}')
            print('Reconnecting...')
            await asyncio.sleep(5)

asyncio.run(subscribe_to_blocks(eth_node_ws_url))

