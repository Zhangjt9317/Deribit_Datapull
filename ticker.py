# ticker.py
# This method is used to call for ticker data every 3 seconds

import threading
import multiprocessing
import time
import asyncio
import websockets
import json
import functools
import datetime

# function to add to JSON
def write_json(data, filename='data.json'):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)

async def call_api(msg):
    async with websockets.connect('wss://test.deribit.com/ws/api/v2') as websocket:
        await websocket.send(msg)
        while websocket.open:
            response = await websocket.recv()
            print(response)
            return response

async def main(msg,loop):
    start = loop.time() # print the start loop time

    await asyncio.sleep(3)
    await call_api(msg)

    end = loop.time()
    exe_time = end-start
    print(exe_time)
    return (await main(msg, loop))

if __name__ ==  '__main__':
    instrument = input('name of the instrument: ')

    msg = \
        {
            "jsonrpc": "2.0",
            "id": 8106,
            "method": "public/ticker",
            "params": {
                "instrument_name": instrument
            }
        }

    msg = json.dumps(msg)

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(msg, loop))
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())  # Python 3.6 only
        loop.close()
