import json
import pandas as pd
import numpy as np

file = "Data/last_trades_by_time_and_currency_20.json"

df = pd.read_json(file)

print(df)

df.to_csv("Data/last_trades.csv")