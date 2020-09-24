import sys
import os
import json
import datetime

import asyncio
import websockets
import json

msg = \
{
  "jsonrpc" : "2.0",
  "id" : 8106,
  "method" : "public/ticker",
  "params" : {
      "instrument_name" : "BTC-PERPETUAL",
  }
}

async def call_api(msg):
   async with websockets.connect('wss://test.deribit.com/ws/api/v2') as websocket:
       await websocket.send(msg)
       while websocket.open:
           response = await websocket.recv()
           # do something with the response...
           print(response)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    asyncio.get_event_loop().run_until_complete(call_api(json.dumps(msg)))
