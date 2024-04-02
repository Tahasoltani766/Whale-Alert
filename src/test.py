from web3.types import HexBytes
import pandas as pd
import numpy as np

a = {'args': {'from': '0x9a719029eDC50A1eEb12e8bdf31ad85863199488', 'to': '0x11b815efB8f581194ae79006d24E0d814B7697F6',
              'value': 5000000000}, 'event': 'Transfer', 'logIndex': 267, 'transactionIndex': 132,
     'transactionHash': HexBytes('0xda351a6253eceb0ab68e9920535f0be0ef712ec65f4915e2622f7959082500dc'),
     'address': '0xdAC17F958D2ee523a2206206994597C13D831ec7',
     'blockHash': HexBytes('0xfd79f8784fea538105f528603c75348dbbb44c8bf13fc95e876c2676d7c97531'),
     'blockNumber': 19567045}
b = {'args': {'from': '0x5D39036947e83862cE5f3DB351cC64E3D4592cD5', 'to': '0x11b815efB8f581194ae79006d24E0d814B7697F6',
              'value': 3500000000}, 'event': 'Transfer', 'logIndex': 312, 'transactionIndex': 157,
     'transactionHash': HexBytes('0x6bd3c5f1e2d33beb9e2d7d37d130d94e6656fbd34858bffc6e36e040f751d773'),
     'address': '0xdAC17F958D2ee523a2206206994597C13D831ec7',
     'blockHash': HexBytes('0xfd79f8784fea538105f528603c75348dbbb44c8bf13fc95e876c2676d7c97531'),
     'blockNumber': 19567045}
c = {'args': {'from': '0x121671AE76BCF934247c17334F4a42B620Da869A', 'to': '0x1689a089AA12d6CbBd88bC2755E4c192f8702000',
              'value': 29440000000}, 'event': 'Transfer', 'logIndex': 72, 'transactionIndex': 18,
     'transactionHash': HexBytes('0x65d2204b5f1b3c6b320cec47da070a48dbec7c34f56c66b1c2568724b6b61d73'),
     'address': '0xdAC17F958D2ee523a2206206994597C13D831ec7',
     'blockHash': HexBytes('0x73713b6f40d641e74e3994bddc3381299c7ac51bf4e2715e5772f767ac11680d'),
     'blockNumber': 19567046}
d = {'args': {'from': '0x6c1aAFCB90bc4c8ec52ff3e135B4E1C1150C7C5f', 'to': '0x81752746F87153a72cd4b8911a8BbE6e3321Fd25',
              'value': 1250000000}, 'event': 'Transfer', 'logIndex': 73, 'transactionIndex': 20,
     'transactionHash': HexBytes('0x28b9f1279960e7b838879029d3c92ae9877688658993da29e508c69a48da5e02'),
     'address': '0xdAC17F958D2ee523a2206206994597C13D831ec7',
     'blockHash': HexBytes('0x73713b6f40d641e74e3994bddc3381299c7ac51bf4e2715e5772f767ac11680d'),
     'blockNumber': 19567046}
e = {'args': {'from': '0x34fd698C00bD9eCF3cd07C29D0f49e7b0f7702D6', 'to': '0x1689a089AA12d6CbBd88bC2755E4c192f8702000',
              'value': 150000000}, 'event': 'Transfer', 'logIndex': 74, 'transactionIndex': 21,
     'transactionHash': HexBytes('0xef519331add30f569e0f908b54288f39af5eba0d411f74353f3259494e5a3588'),
     'address': '0xdAC17F958D2ee523a2206206994597C13D831ec7',
     'blockHash': HexBytes('0x73713b6f40d641e74e3994bddc3381299c7ac51bf4e2715e5772f767ac11680d'),
     'blockNumber': 19567046}
f = {'args': {'from': '0x56Eddb7aa87536c09CCc2793473599fD21A8b17F', 'to': '0x1689a089AA12d6CbBd88bC2755E4c192f8702000',
              'value': 48044940000}, 'event': 'Transfer', 'logIndex': 85, 'transactionIndex': 31,
     'transactionHash': HexBytes('0xafbdba10be75f3922ca780ffe50578fb1d07c0a705839c46c53711f9996d66f1'),
     'address': '0xdAC17F958D2ee523a2206206994597C13D831ec7',
     'blockHash': HexBytes('0x73713b6f40d641e74e3994bddc3381299c7ac51bf4e2715e5772f767ac11680d'),
     'blockNumber': 19567046}

x = [a, b, c, d, e, f]

from web3 import Web3

rpc_url = 'https://eth-mainnet.g.alchemy.com/v2/kurV79OJ-CdKRuj6nc0Ua-JYhXGVdjcA'
w3 = Web3(Web3.HTTPProvider(rpc_url))

print(w3.is_connected())
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


def trx_transfer():
    while True:
        weth_contract = w3.eth.contract(address=adr_token, abi=abi_token)
        logs = weth_contract.events.Transfer().get_logs(fromBlock=19568106, toBlock='latest')
        d.handler_data(logs)


class dataFrame:
    def __init__(self):
        dt = {}
        index = []
        self.df = pd.DataFrame(dt, index=index)
        self.table = np.empty((0, 4), dtype=object)

    def handler_data(self, list_trx):
        if not self.table.size:
            for trx in list_trx:
                # print(i.args.to)
                _to = (trx.args.to)
                _from = (trx.args['from'])
                _value = (trx.args.value)
                _token = (trx.address)
                print()
                new_row = np.array([_to, _value, _from, _token])
                print(new_row)
                self.table = np.vstack([self.table, new_row])
        else:
            for trx in list_trx:
                _to = (trx.args.to)
                _from = (trx.args['from'])
                _value = (trx.args.value)
                _token = (trx.address)
                new_row = np.array([_to, _value, _from, _token])
                print(new_row)
                self.table = np.vstack([self.table, new_row[None, :]])
            # self.addr_checker(self.table)

    def addr_checker(self,table):
        _to = table[:, 0]
        values = table[:, 1]
        print(_to, values)
        unique_addresses, counts = np.unique(_to, return_counts=True)
        similar_addresses = unique_addresses[counts > 1]
        if len(similar_addresses) > 0:
            for address in similar_addresses:
                indices = np.where(_to == address)[0]
                val = values[indices]
                result = sum(map(int, val))
                print(result)
                similar_reps = self.table[indices]
                flattend = similar_reps.flatten()
                unique_values = set(flattend)
                merged_arr = np.array(list(unique_values))
                print(merged_arr)
                # self.counter_to(similar_reps)
        else:
            pass

    # def counter_from(self):
    # pass

    # def counter_to(self,similar):
    # print(similar)


d = dataFrame()
trx_transfer()
# d.addr_checker()
