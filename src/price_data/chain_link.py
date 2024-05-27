# https://docs.chain.link/data-feeds/price-feeds/addresses?network=ethereum&page=1&search=ca
from web3 import Web3
from abi_chainlink import abi

w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.g.alchemy.com/v2/c8VW6jhdLbvoyh3bEMkEfPEcSUzdezIO'))

addr = w3.to_checksum_address('0x72AFAECF99C9d9C8215fF44C77B94B99C28741e8')

contract = w3.eth.contract(address=addr, abi=abi)

latestData = contract.functions.latestRoundData().call()
print(latestData)
# print(latestData)
get_round_data = contract.functions.getRoundData(36893488147419103233).call()
# 36893488147419103233
block_num = w3.eth.get_block_number(1716752147)
print(block_num)
# 19956177
# https://coins.llama.fi/block/ethereum/1716752147
