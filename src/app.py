# import csv
#
# # Open the CSV file
# with open('export-tokenholders.csv', 'r') as file:
#     csv_reader = csv.DictReader(file)
#     list_dict_cexs = []
#     list_dict_private = []
#     for row in csv_reader:
#         if row['CEX'] == 'None':
#             list_dict_private.append(row['HolderAddress'])
#         elif row['CEX'] == 'Blocked':
#             pass
#         else:
#             x = row['HolderAddress']
#             y = row['CEX']
#             list_dict_cexs.append({'HolderAddress': x, 'CEX':y})
# print(list_dict_private)
from pprint import pprint

import pandas as pd

#
# new_blocks = []
# new_balances = []
# for i in range(len(data['block']) - 1):
#     new_blocks.append(data['block'][i])
#     new_balances.append(data['balance'][i])
#     if data['block'][i + 1] - data['block'][i] > 1:
#         for j in range(data['block'][i] + 1, data['block'][i + 1]):
#             new_blocks.append(j)
#             new_balances.append(data['balance'][i])
#
# # Add the last block and its balance
# new_blocks.append(data['block'][-1])
# new_balances.append(data['balance'][-1])
#
# # Update the data dictionary with new blocks and balances
# data['block'] = new_blocks
# data['balance'] = new_balances
#
# print(data)

data = {'address': '0x235d3afAc42f5e5fF346Cb6C19AF13194988551F',
        'balance': [51765735, 51765733, 51765740], 'block': [19717698, 19717701, 19717705]}

addr = data['address']
balances = data['balance']
balance_new = balances.copy()
balance_new.insert(0, addr)
blocks = data['block']
new_blocks = blocks.copy()
new_blocks.insert(0,"address")
df = pd.DataFrame([balance_new], columns=new_blocks)
print(df)

# table = {}
# table["usdt"] = []
# for i in range(len(blocks)):
#     if i > 0:
#         diff_block = blocks[i] - blocks[i - 1]
#         if diff_block > 1:
#         print("ddd")
#         for j in range(diff_block-1):
#             table["usdt"].append({
#                 blocks[i-1] + j+1: {addr: balances[i]},
#             })
# table["usdt"].append({
# blocks[i]: {addr: balances[i]},
# })
