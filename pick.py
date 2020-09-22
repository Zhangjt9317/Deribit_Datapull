import sys
import os
import json
import datetime

msg = \
    {
        "jsonrpc": "2.0",
        "id": 1469,
        "params": {
            "currency": "BTC",
            "kind": "Future",
            "start_timestamp": None,
            "end_timestamp": None,
            "count": 2,
            "instrument_name": None,
            "length": None,
            "type": None,
            "expired": None,
            "include_old": "false",
            "sorting": "asc",
        }
    }
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

if __name__ == "__main__":
    m = process_msg(msg)
    print(m)