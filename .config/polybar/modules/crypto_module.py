#!/usr/bin/env python3

import requests


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

currency='USD'
icon = ""
url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD'
headers = {
  'Accepts': 'application/json',
  'Apikey': '5b0fc806257a77e2b39d28765f5a72d030e2e470ec3250cf5723f9306e889968',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url)
  data = json.loads(response.text)
  price = int(data[currency])
  print(f'{icon} {price} {currency}')
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print('Error')
