import pandas as pd
import numpy as np
from web3 import Web3
import json
from abi import abi_token

rpc_url = 'https://mainnet.infura.io/v3/8cb9d441420b4009afa02ce71849560e'
w3 = Web3(Web3.HTTPProvider(rpc_url))

USDT = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
adr_token = w3.to_checksum_address(USDT)

erc20_contract = w3.eth.contract(address=adr_token, abi=abi_token)


class TokenTransactions(object):
    df: pd.DataFrame
    block_range: tuple[int, int]

    def __init__(self, block_rng: tuple[int, int], balance_initial_address, logs: list):
        self.block_range = block_rng
        self.logs = logs
        block_range = [i for i in range(int(block_rng[0]), int(block_rng[1]))]

        block_range.insert(0, int(block_rng[0]) - 1)
        block_range.insert(0, "address")

        self.df = pd.DataFrame(columns=block_range, data={
            "address": [i[0] for i in balance_initial_address],
            int(block_rng[0]) - 1: [i[1] for i in balance_initial_address]
        })
        for log in self.logs:
            self.calculate_from(log[0], log[1])
            self.final_completion(log[1])
        print(self.df.to_string())

    def calculate_from(self, log: list, block_num):
        for item in log:
            matching_index = self.df.index[self.df['address'] == item['from']].tolist()
            if matching_index:
                last_value = self.df.loc[matching_index[0], int(block_num) - 1]
                if last_value != np.nan:
                    self.df.loc[matching_index[0], int(block_num)] = last_value + item['value']
                    self.calculate_to(item['to'], item['value'], block_num)

    def calculate_to(self, addr_to, value, block_num):
        matching_index = self.df.index[self.df['address'] == addr_to].tolist()
        if matching_index:
            last_value = self.df.loc[matching_index[0], int(block_num) - 1]
            if last_value != np.nan:
                self.df.loc[matching_index[0], int(block_num)] = last_value - value

    def final_completion(self, block_num):
        self.df.loc[self.df[int(block_num)].isnull(), int(block_num)] = self.df.loc[self.df[int(block_num)].isnull(), int(block_num) - 1]


def handler_data_block_batch(logs, block_num, block_range, addresses: set):
    for log in logs:
        addresses.add(log['from'])
        addresses.add(log['to'])
    return addresses


def reader_json():
    with open('data.json', 'r') as file:
        return json.load(file)


def data_sorter(data):
    block_range = False
    addresses = set()
    logs = []
    for item in data['blocks'].items():
        if not block_range:
            block_range = (item[0], data['last_scanned_block'])
        logs.append([item[1], item[0]])
        addresses = handler_data_block_batch(item[1], item[0], block_range, addresses)
    return block_range, addresses, logs


def get_token_balance(block_number, address):
    return erc20_contract.functions.balanceOf(address).call(block_identifier=block_number)


if __name__ == '__main__':
    data = reader_json()
    block_rng, addresses, logs = data_sorter(data)
    balance_initial_address = []
    for address in addresses:
        balance = get_token_balance(int(block_rng[0]) - 1, address)
        balance_initial_address.append((address, balance))
        if len(balance_initial_address) == 20:
            my_tx = TokenTransactions(block_rng, balance_initial_address, logs)

