from web3 import Web3
from abi_chainlink import abi_aave
import requests
import pandas as pd
import ccxt

w3 = Web3(Web3.HTTPProvider('https://polygon-mainnet.g.alchemy.com/v2/Jxjnw0BxIIax4t7xDraPNPSn9EDbYAGY'))
addr = w3.to_checksum_address('0xcAc8362649DaE2cc0a91e1d200A93E4CEf620be5')
contract = w3.eth.contract(address=addr, abi=abi_aave)
exchange = ccxt.binance()


class dataPrice:
    def __init__(self):
        self.df = pd.DataFrame()

    def latest_round(self, ):
        latest_round = contract.functions.latestRound().call()
        while latest_round >= 8151765:
            print(latest_round)
            self.get_round_data(latest_round)
            latest_round -= 1
        print(self.df)

    def get_round_data(self, number):
        # Chain Link
        get_data = contract.functions.getRoundData(number).call()
        block_number = self.convertor_timestamp(get_data[2])
        price_binance = self.price_binance(get_data[2])
        data = {
            block_number: [(get_data[1] * 0.00000001), price_binance]
        }
        print(data)
        self.creator_table(data)


    def price_binance(self, timestamp):
        print(timestamp)
        response = exchange.fetch_ohlcv('AAVE/USDT', '1m', timestamp * 1000, 1)
        return response[0][4]

    def convertor_timestamp(self, timestamp):
        res = requests.get(
            f'https://api.etherscan.io/api?module=block&action=getblocknobytime&timestamp={timestamp}&closest=before&apikey=PPNUMM5CUR6US9PWXNY6I79I94XD2WEAUN')
        return res.json()["result"]

    def creator_table(self, data):
        new_df = pd.DataFrame.from_dict(data, orient='index')
        if new_df.index.isin(self.df.index).any():
            pass
        else:
            self.df = pd.concat([self.df, new_df])


d = dataPrice()
d.latest_round()
