#!/usr/bin/env python3

import requests

icon = ""
ticker = "bitcoin"
currency = "USD"
json = requests.get(f'https://api.coinmarketcap.com/v1/ticker/{ticker}').json()[0]
price = int(round(float(json[f'price_{currency.lower()}'])))
print(f'{icon} {price} {currency}')
