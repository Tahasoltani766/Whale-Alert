import json
from requests import Session

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
param = {'slug': 'bitcoin', 'convert': 'USD'}
headers = {'Accepts': 'application',
           'X-CMC_PRO_API_KEY': 'd9bbe037-fa5c-4e23-85cd-026129aff52a', }

session = Session()
session.headers.update(headers)
response = session.get(url, params=param)
final_price = json.loads(response.text)['data']['1']['quote']['USD']['price']
print(final_price)
