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
    file = filedialog.askopenfilename(initialdir=cwd,filetypes =[('JSON Files', '*.json')])
    return file

file = open_file()
# print(file)
# print(type(file))

with open(file, 'r') as outfile:
    data = json.load(outfile)

df = pd.json_normalize(data)
print(df)

df.to_csv("Data/ticker.csv")