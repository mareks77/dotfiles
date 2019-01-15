#!/bin/bash
icon=
json=$(curl -s 'https://api.coinmarketcap.com/v1/ticker/bitcoin/')
if [ ! -z "$json" ]
then
  price=$(echo "$json" | jq '.[0].price_usd|tonumber' | awk '{printf("%.2f", $0)}')
  echo "$icon $price USD"
else
  echo "Failed to retrieve JSON"
fi
