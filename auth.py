import asyncio
import websockets
import json
from config import client_id, client_secret, test

# do auth before making private requests
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

async def call_api(msg):
   async with websockets.connect(test) as websocket:
       await websocket.send(msg)
       while websocket.open:
           response = await websocket.recv()
           # do something with the response...
           print(response)

           response = json.loads(response)
           # get trades data from json result
           value = response['result']
           with open("Data/auth.json","w") as fp:
               json.dump(value, fp)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(call_api(json.dumps(msg)))