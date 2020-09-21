import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

import json
import aiohttp
import websockets
import asyncio

from datetime import timezone


# client id and secret for testing
client_id = "dtzNFB-6"
client_secret = "15EGz-IQyJbKpkYLrk9w97MgN6UhupSXS22yWYPjrLo"

categories = ['Authentication','Session Management','Supporting','Subscription Management',
              'Account Management', 'Block Trade', 'Trading', 'Market Data', 'Wallet']
market = [
    'get_book_summary_by_currency',
    'get_book_summary_by_instrument',
    'get_contract_size',
    'get_currencies',
    'get_funding_chart_data',
    'get_funding_rate_value',
    'get_historical_volatility',
    'get_index',
    'get_instrument',
    'get_last_settlement_by_currency',
    'get_last_settlement_by_instrument',
    'get_last_trades_by_currency',
    'get_last_trades_by_currency_and_time',
    'get_last_trades_by_instrument',
    'get_last_trades_by_instrument_and_time',
    'get_order_book',
    'get_trade_volume',
    'get_tradingview_chart_data',
    'ticker'
]

# only show public auth actions, 'logout' is not here
auth = [
    'auth',
    'exchange_token',
    'fork_token'
]

# plotly
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Dropdown(
        id='demo-dropdown',
        options=[{'label': i, 'value': i} for i in set(market)],
        value='get_book_summary_by_currency'
    ),
    html.Div(id='dd-output-container')
])

# callbacks
@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('demo-dropdown', 'value')]
)
# update output and display
def update_output(value):
    return 'You have selected "{}"'.format(value)



# only for authentication
async def call_auth(msg):
   async with websockets.connect('wss://test.deribit.com/ws/api/v2') as websocket:
       await websocket.send(msg)
       while websocket.open:
           response = await websocket.recv()
           # do something with the response...
           print(response)
           print(type(response))

           response = json.loads(response)
           with open("Data/auth.json","w"):
               json.dumps(response,indent=4,sort_keys=True)

# call api actions
async def call_api(msg):
   async with websockets.connect('wss://test.deribit.com/ws/api/v2') as websocket:
       await websocket.send(msg)
       while websocket.open:
           response = await websocket.recv()
           # do something with the response...
           print(response)
           # print(type(response))

async def main():
    call_api()


if __name__ == '__main__':
    app.run_server(debug=True)