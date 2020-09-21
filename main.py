# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import asyncio
import websockets
import json
import time

client_id = "dtzNFB-6"
client_secret = "15EGz-IQyJbKpkYLrk9w97MgN6UhupSXS22yWYPjrLo"

# auth is required before making private requests
msg = \
{
  "jsonrpc" : "2.0",
  "id" : 9929,
  "method" : "public/auth",
  "params" : {
    "grant_type" : "client_credentials",
    "client_id" : client_id,
    "client_secret" : client_secret
  }
}

msg = \
{
  "jsonrpc" : "2.0",
  "id" : 1469,
  "method" : "public/get_last_trades_by_currency_and_time",
  "params" : {
      "currency" : "BTC",
      "kind":"future",
      "start_timestamp" : 1590470022768,
      "end_timestamp" : 1590480022768,
      "count" : 20,
      "include_old":'true',
      "sorting":"asc"
  }
}

async def call_api(msg):
   async with websockets.connect('wss://test.deribit.com/ws/api/v2') as websocket:
       await websocket.send(msg)
       while websocket.open:
           response = await websocket.recv()
           # do something with the response...
           print(response)
           # print(type(response))

           response = json.loads(response)
           # print(response)
           # print(type(response))
           value = response['result']['trades']
           with open("Data/last_trades_by_time_and_currency_20.json","w") as fp:
               json.dump(value, fp)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(call_api(json.dumps(msg,indent=4,sort_keys=True)))
