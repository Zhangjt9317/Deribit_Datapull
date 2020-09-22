import json
import pandas as pd
import sys
import os
import tkinter
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

cwd = os.getcwd()

# This function will be used to open
# file in read mode and only Python files
# will be opened
def open_file():
    file = filedialog.askopenfile(initialdir=cwd,mode ='r',filetypes =[('JSON Files', '*.json')])
    if file is not None:
        content = file.read()
        print(content)

file = open_file()

df = pd.read_json(file)
print(df)

df.to_csv("Data/last_trades.csv")