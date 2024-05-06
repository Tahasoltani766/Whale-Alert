# https://docs.chain.link/data-feeds/price-feeds/addresses?network=ethereum&page=1&search=ca
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.g.alchemy.com/v2/c8VW6jhdLbvoyh3bEMkEfPEcSUzdezIO'))

abi = ('[{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],'
       '"stateMutability":"view","type":"function"},{"inputs":[],"name":"description","outputs":[{'
       '"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{'
       '"internalType":"uint80","name":"_roundId","type":"uint80"}],"name":"getRoundData","outputs":[{'
       '"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer",'
       '"type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256",'
       '"name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],'
       '"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestRoundData","outputs":[{'
       '"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer",'
       '"type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256",'
       '"name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],'
       '"stateMutability":"view","type":"function"},{"inputs":[],"name":"version","outputs":[{'
       '"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]')
addr = w3.to_checksum_address('0x72AFAECF99C9d9C8215fF44C77B94B99C28741e8')

contract = w3.eth.contract(address=addr, abi=abi)

latestData = contract.functions.latestRoundData().call()
price = latestData[1]