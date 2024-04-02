from web3 import Web3
import numpy as np
import pandas as pd

# rpc_url = " https://lingering-neat-daylight.quiknode.pro/558e705b7d888b9d1b55741d6adf78154cfcd2a8/"
# rpc_url = "https://wiser-frequent-spree.quiknode.pro/123695138b0af6d1eaf84c03c04d5a54353343bc/"
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
        logs = weth_contract.events.Transfer().get_logs(fromBlock=19567721, toBlock='latest')
        data_frame(logs)


# AttributeDict({'args': AttributeDict({'from': '0x9acbB72Cf67103A30333A32CD203459c6a9c3311', 'to': '0xDBeacf4672094Dc83e3e65402fc8fF11628C688c', 'value': 1502580000}), 'event': 'Transfer', 'logIndex': 0, 'transactionIndex': 0, 'transactionHash': HexBytes('0x281260c670959681391f0377f2b52d2b8717bbae6a6ed405984cef3db02d6ba2'), 'address': '0xdAC17F958D2ee523a2206206994597C13D831ec7', 'blockHash': HexBytes('0xf23c41e9e353aed56db1c7514bf966d6ce01a6d9ad6ff82bd80052ddaad86b1b'), 'blockNumber': 19566720})
# AttributeDict({'args': AttributeDict({'from': '0x9dFC38E64A65782CAb480249adE0975Ea80b3e73', 'to': '0x663DC15D3C1aC63ff12E45Ab68FeA3F0a883C251', 'value': 1840046718}), 'event': 'Transfer', 'logIndex': 32, 'transactionIndex': 6, 'transactionHash': HexBytes('0xebe93bea06e7a5319fed4840eca0aeda45382fc8ef4503f5e32909196db5881d'), 'address': '0xdAC17F958D2ee523a2206206994597C13D831ec7', 'blockHash': HexBytes('0x4edd38d3014d24e6fff15f1fbb4596e4e4c81cab9dc964476c81762f93584d60'), 'blockNumber': 19566776})
def data_frame(logs):
    data = {None: None}
    index = [None]
    df = pd.DataFrame(data, index=index)
    for trx in logs:
        _to = trx.args.to
        # _from = trx.args.from
        _value = trx.args.value
        _token = trx.address
        print(_to, _value, _token)


trx_transfer()
