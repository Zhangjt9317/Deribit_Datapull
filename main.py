# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import asyncio
import websockets
import json
import time
import datetime

client_id = "dtzNFB-6"
client_secret = "15EGz-IQyJbKpkYLrk9w97MgN6UhupSXS22yWYPjrLo"

# currently only working on market data pulling
methods = [
    'get_book_summary_by_currency',
    'get_book_summary_by_instrument',
    'get_contract_size',
    'get_currencies',
    'get_funding_chart_data',
    'get_funding_rate_history',                 #time
    'get_funding_rate_value',                   #time
    'get_historical_volatility',
    'get_index',
    'get_instruments',
    'get_last_settlements_by_currency',         #time
    'get_last_settlements_by_instrument',       #time
    'get_last_trades_by_currency',
    'get_last_trades_by_currency_and_time',     #time
    'get_last_trades_by_instrument',
    'get_last_trades_by_instrument_and_time',   #time
    'get_order_book',
    'get_trade_volumes',
    'get_tradingview_chart_data',               #time
    'ticker'
]
time_methods=[
    methods[6],
    methods[7],
    methods[-2],
    methods[-5],
    methods[-7],
    methods[-9],
    methods[-10]
]

currencies = ["BTC","ETH"]
kinds = ['future','option']
types = ["settlement", "delivery", "bankruptcy"]
sortings = ['asc','desc','default']
lengths = ['8h','24h','1m']
resolutions = ['1','3','5','10','15','30','60','120','180','360','720','1D']

def let_user_pick(options):
    print("Please choose:")
    for idx, element in enumerate(options):
        print("{}) {}".format(idx+1,element))
    i = input("Enter number: ")
    try:
        if 0 < int(i) <= len(options):
            choice = str(options[int(i)-1])
            print(choice)
    except:
        pass
    return choice

def timestamp():
    """
    :return: datetime to timestamp
    """
    # ask for the expiration date for option and convert to timestamp
    start_date_string = input("Input the start date: ")
    if not start_date_string:
        pass
    else:
        start_date = datetime.datetime.strptime(start_date_string, "%m/%d/%Y")
        start_timestamp = int(datetime.datetime.timestamp(start_date))

    # ask for the expiration date for option and convert to timestamp
    end_date_string = input("Input the end date: ")
    if not end_date_string:
        pass
    else:
        end_date = datetime.datetime.strptime(end_date_string, "%m/%d/%Y")
        end_timestamp = int(datetime.datetime.timestamp(end_date))

    return start_timestamp, end_timestamp

def process_msg(msg):
    """
    :param msg: dict
    :return: shortened dict
    """
    msg = json.dumps(msg, indent=4, sort_keys=True)
    msg = json.loads(msg)
    print(type(msg))

    ls = []
    ignored_values = set(["null", "", None])
    for key in msg['params']:
        if msg['params'][key] in ignored_values:
            print(key)
            ls.append(key)

    for key in ls:
        del(msg['params'][key])
    return msg

async def call_api(msg):
   async with websockets.connect('wss://test.deribit.com/ws/api/v2') as websocket:
       await websocket.send(msg)
       while websocket.open:
           response = await websocket.recv()
           print(response)

           response = json.loads(response)
           # get trades data from json result
           value = response['result']['trades']
           with open("Data/methods.json","w") as fp:
               json.dump(value, fp)

if __name__ == "__main__":
    choice = let_user_pick(methods)

    if choice in time_methods:
        start = timestamp()[0]
        end = timestamp()[1]
    else:
        start = None
        end = None

    # ask for market method inputs
    currency = let_user_pick(currencies)
    kind = let_user_pick(kinds)
    count = input("count of trades? ")
    # instrument = input('name of the instrument: ')
    # old = input("Include old trades (ture or false)? ")
    # sorting = let_user_pick(sortings)
    # length = let_user_pick(lengths)
    # resolution = let_user_pick(resolutions)
    # what_type = let_user_pick(types)

    msg = \
        {
            "jsonrpc": "2.0",
            "id": 1469,
            "method": "public/{}".format(choice),
            "params": {
                "currency": currency,
                "kind": kind,
                "start_timestamp": start,
                "end_timestamp": end,
                "count": count,
                "instrument_name": None,
                "length": None,
                "type" : None,
                "expired": False,
                "resolution" : None,
                "include_old": "false",
                "sorting": "asc",
            }
        }

    msg = process_msg(msg)

    asyncio.get_event_loop().run_until_complete(call_api(json.dumps(msg)))
