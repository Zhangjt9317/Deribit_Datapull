import threading
import multiprocessing
import time
import asyncio
import websockets
import json
import functools
import datetime

msg = \
    {
        "jsonrpc" : "2.0",
        "id" : 8106,
        "method" : "public/ticker",
        "params" : {
          "instrument_name" : "BTC-PERPETUAL"
        }
    }

msg = json.dumps(msg)

async def call_api(msg):
    async with websockets.connect('wss://test.deribit.com/ws/api/v2') as websocket:
        await websocket.send(msg)
        while websocket.open:
            response = await websocket.recv()
            print(response)
            return response

async def main(msg,loop):
    print(loop.time())

    await asyncio.sleep(5)
    await call_api(msg)
    return (await main(msg, loop))

if __name__ ==  '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(msg, loop))
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())  # Python 3.6 only
        loop.close()
